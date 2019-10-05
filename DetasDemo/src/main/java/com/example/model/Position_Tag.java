package com.example.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

/*
 * 职位标签表
 * bean
 * */
@Entity
public class Position_Tag {
	@Id
	@GeneratedValue(strategy= GenerationType.IDENTITY)
	private int id;
	private String tag;

	public Position_Tag() {
	}

	public Position_Tag(String tag) {
		this.tag = tag;
	}

	@Override
	public String toString() {
		return "Position_Tag{" +
				"id=" + id +
				", tag='" + tag + '\'' +
				'}';
	}

	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getTag() {
		return tag;
	}
	public void setTag(String tag) {
		this.tag = tag;
	}
}
