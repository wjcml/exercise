package com.demo.model;

import javax.persistence.*;

@Entity(name = "tb_img")
public class Image {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    @Column(columnDefinition = "text")
    private String img;

    protected Image() {
    }

    public Image(String img) {
        this.img = img;
    }

    public Integer getId() {
        return id;
    }

    public String getImg() {
        return img;
    }

    public void setImg(String img) {
        this.img = img;
    }
}
