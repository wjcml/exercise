package com.demo.api;

public class ApiResponse {
    private String code;
    private Object result;

    public ApiResponse(String code, Object result) {
        this.code = code;
        this.result = result;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public Object getResult() {
        return result;
    }

    public void setResult(Object result) {
        this.result = result;
    }
}
