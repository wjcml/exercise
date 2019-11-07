package com.cdgeekcamp.redas.api.core.websocket;

import com.cdgeekcamp.redas.db.model.PositionUrl;
import com.cdgeekcamp.redas.db.model.PositionUrlRepository;
import com.google.gson.Gson;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import javax.xml.bind.DatatypeConverter;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.sql.Timestamp;
import java.util.Date;
import java.util.Optional;

@Service
public class MessageHandle {

    @Autowired
    private PositionUrlRepository positionUrlRepository;

    public boolean LoginHandle(SocketApi socketMsg) throws InvalidKeyException, UnsupportedEncodingException, NoSuchAlgorithmException {
//        得到secretkey
        String secretKey = "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92";

        Gson gson = new Gson();
        SocketCommon socketCommon = gson.fromJson(gson.toJson(socketMsg.getCommon()), SocketCommon.class);
        SocketArgsLogin socketArgsLogin = gson.fromJson(gson.toJson(socketMsg.getArgs()), SocketArgsLogin.class);

        Mac mac = Mac.getInstance("HmacSHA256");
        SecretKeySpec secretKeySpec = new SecretKeySpec(secretKey.getBytes(StandardCharsets.UTF_8), mac.getAlgorithm());
        mac.init(secretKeySpec);
        byte[] hash = mac.doFinal(socketArgsLogin.toString().getBytes(StandardCharsets.UTF_8));
        String socketHash = DatatypeConverter.printBase64Binary(hash);

        if (socketHash.equals(socketCommon.getSignature())){
            return true;
        }else {
            return false;
        }

    }

}
