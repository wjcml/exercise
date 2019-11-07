package com.cdgeekcamp.redas.api.core.websocket;

import com.cdgeekcamp.redas.db.model.PositionUrl;
import com.cdgeekcamp.redas.db.model.PositionUrlRepository;
import com.cdgeekcamp.redas.lib.core.api.ApiResponseMap;
import com.cdgeekcamp.redas.lib.core.api.ApiResponseX;
import com.cdgeekcamp.redas.lib.core.api.ResponseCode;
import com.google.gson.Gson;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import javax.websocket.*;
import javax.websocket.server.ServerEndpoint;
import java.io.IOException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.sql.Timestamp;
import java.util.Date;
import java.util.List;
import java.util.Optional;
import java.util.concurrent.CopyOnWriteArrayList;

@ServerEndpoint(value = "/")
@Component
public class PosUrlWebSocket {
    //在线人数
    private static int count = 0;
    //所有的对象，用于群发
    public static List<PosUrlWebSocket> webSockets = new CopyOnWriteArrayList<>();
    //会话
    private Session session;
    //正在处理URL
    private String handling = "";
    private String url;

    private Logger log = LoggerFactory.getLogger(this.getClass());

    private static PositionUrlRepository positionUrlRepository;
    @Autowired
    public void setPositionUrlRepository(PositionUrlRepository positionUrlRepository) {
        PosUrlWebSocket.positionUrlRepository = positionUrlRepository;
    }

    public String getHandling() {
        return handling;
    }

    //建立连接
    @OnOpen
    public void onOpen(Session session) {
        webSockets.add(this);
        this.session = session;
        addCount();
        log.info("新的连接加入id:{}",session.getId());
    }

    //连接关闭
    @OnClose
    public void onClose() {
        webSockets.remove(this);
        reduceCount();
        log.info("连接关闭id:{}",this.session.getId());
    }

    //收到客户端的消息
    @OnMessage
    public void onMessage(String jsonString, Session session) throws IOException, InvalidKeyException, NoSuchAlgorithmException {
        Gson gson = new Gson();
        SocketApi socketMsg = gson.fromJson(jsonString, SocketApi.class);
        MessageHandle messageHandle = new MessageHandle();

        ApiResponseMap<String, Object> apiResponseMap = new ApiResponseMap<>();
        //socket连接
        if ("login".equals(socketMsg.getUrl())){
            boolean is_true = messageHandle.LoginHandle(socketMsg);
            if (is_true){
                apiResponseMap.setCode(ResponseCode.LOGIN_SUCCESS);
                apiResponseMap.setMessage("连接成功");
                this.session.getBasicRemote().sendText(gson.toJson(apiResponseMap));

                this.handling = "NOT_HANDLING";
            }else {
                apiResponseMap.setCode(ResponseCode.LOGIN_FAILED);
                apiResponseMap.setMessage("连接失败");
                this.session.getBasicRemote().sendText(gson.toJson(apiResponseMap));

                onClose();
            }
        }

        //spider处理URL结果
        if ("spiderReport".equals(socketMsg.getUrl())){
            SocketArgsSpiderReport socketArgsSpiderReport = gson.fromJson(
                    gson.toJson(socketMsg.getArgs()), SocketArgsSpiderReport.class);
            if ("SUCCESS".equals(socketArgsSpiderReport.getCode())){
                //更新URL状态和爬取时间
                Optional<PositionUrl> positionUrl = positionUrlRepository.findByUrl(this.url);

                PositionUrl posUrl = positionUrl.get();
                posUrl.setState(true);

                Date date = new Date();
                posUrl.setCrawlTime(new Timestamp(date.getTime()));

                positionUrlRepository.save(posUrl);

                this.handling = "NOT_HANDLING";
            }else {
                sendMessage(this.url);
            }
        }
    }

    //连接错误时执行
    @OnError
    public void onError(Session session, Throwable error){
        log.info("发生错误id:{},msg:{}", session.getId(), error.getMessage());
    }

    //获取在线连接数目
    public static int getCount(){
        return count;
    }

    //操作count，使用synchronized确保线程安全
    public static synchronized void addCount(){
        PosUrlWebSocket.count++;
    }

    public static synchronized void reduceCount(){
        PosUrlWebSocket.count--;
    }

    //发送消息
    public void sendMessage(String message) throws IOException {
        Gson gson = new Gson();
        ApiResponseX<String> apiResponseX = new ApiResponseX<>(
                ResponseCode.GET_URL_SUCCESS, "获取URL成功", message);

        this.handling = "IS_HANDLING";
        this.url = message;

        this.session.getBasicRemote().sendText(gson.toJson(apiResponseX));
    }
}
