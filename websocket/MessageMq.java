package com.cdgeekcamp.redas.api.core.websocket;

import com.cdgeekcamp.redas.lib.core.mqConfig.PositionUrlMqConfig;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import javax.servlet.http.PushBuilder;
import java.time.Duration;
import java.util.Collections;
import java.util.Properties;

@Component
public class MessageMq implements CommandLineRunner {
    @Autowired
    private PositionUrlMqConfig positionUrlMqConfig;

    private PosUrlWebSocket posUrlWebSocket;

    private static Boolean is_record = false;

    @Override
    public void run(String... args) throws Exception {
        Properties p = new Properties();
        p.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, positionUrlMqConfig.getHost());
        p.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
        p.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
        p.put(ConsumerConfig.GROUP_ID_CONFIG, positionUrlMqConfig.getGroup());

        KafkaConsumer<String, String> kafkaConsumer = new KafkaConsumer<>(p);

        try (kafkaConsumer) {
            kafkaConsumer.subscribe(Collections.singletonList(positionUrlMqConfig.getTopic()));

            // 以下注释用来消除 while 语句警告提示
            //noinspection InfiniteLoopStatement
            while (true) {
                //做限制，防止一直从队列中拿消息
                if (MessageMq.is_record){
                    continue;
                }

                ConsumerRecords<String, String> records = kafkaConsumer.poll(Duration.ofMillis(1000));
                MessageMq.is_record = true;

                for (ConsumerRecord<String, String> record : records) {
                    System.out.println(
                            String.format("topic:%s,offset:%d,消息:%s",
                                    record.topic(), record.offset(), record.value()));
                    while (true){
                        //做限制，防止一次将拿到的消息发送出去
                        if (PosUrlWebSocket.webSockets.isEmpty()){
                            continue;
                        }

                        for(PosUrlWebSocket posUrlWebSockets: PosUrlWebSocket.webSockets){
                            if(posUrlWebSockets.getHandling().equals("NOT_HANDLING")){
                                posUrlWebSocket = posUrlWebSockets;
                                break;
                            }else {
                                posUrlWebSocket = null;
                            }
                        }

                        if(posUrlWebSocket == null){
                            continue;
                        }
                        posUrlWebSocket.sendMessage(record.value());
                        break;
                    }

                }

                MessageMq.is_record = false;
            }
        }
    }
}
