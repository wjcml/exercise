package com.cdgeekcamp.redas.api.core.websocket;

public class SocketArgsLogin {
    private String version;

    public SocketArgsLogin() {
    }

    public SocketArgsLogin(String version) {
        this.version = version;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    @Override
    public String toString() {
        return "version=" + version;
    }
}
