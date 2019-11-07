package com.cdgeekcamp.redas.api.core.websocket;

public class SocketCommon {
    private String secretId;
    private String signature;

    public SocketCommon() {
    }

    public SocketCommon(String secretId, String signature) {
        this.secretId = secretId;
        this.signature = signature;
    }

    public String getSecretId() {
        return secretId;
    }

    public void setSecretId(String secretId) {
        this.secretId = secretId;
    }

    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }
}
