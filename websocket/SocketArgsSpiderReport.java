package com.cdgeekcamp.redas.api.core.websocket;

public class SocketArgsSpiderReport {
    private String code;

    public SocketArgsSpiderReport() {
    }

    public SocketArgsSpiderReport(String code) {
        this.code = code;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
}
