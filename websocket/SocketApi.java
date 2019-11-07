package com.cdgeekcamp.redas.api.core.websocket;

public class SocketApi {
    private String url;
    private Object common;
    private Object args;

    public SocketApi() {
    }

    public SocketApi(String url, Object common, Object args) {
        this.url = url;
        this.common = common;
        this.args = args;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public Object getCommon() {
        return common;
    }

    public void setCommon(Object common) {
        this.common = common;
    }

    public Object getArgs() {
        return args;
    }

    public void setArgs(Object args) {
        this.args = args;
    }
}
