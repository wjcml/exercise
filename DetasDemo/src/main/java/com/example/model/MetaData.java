package com.example.model;

import javax.persistence.*;

@Entity
public class MetaData {
    @Id
    @GeneratedValue(strategy= GenerationType.IDENTITY)
    private int id;
    private String uuid;
    @Column(length = 2000)
    private String meta;

    public MetaData(String uuid, String meta) {
        this.uuid = uuid;
        this.meta = meta;
    }

    public MetaData() {
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }

    public String getMeta() {
        return meta;
    }

    public void setMeta(String meta) {
        this.meta = meta;
    }

    @Override
    public String toString() {
        return "MetaData{" +
                "id=" + id +
                ", uuid='" + uuid + '\'' +
                ", meta='" + meta + '\'' +
                '}';
    }
}
