package com.example.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

/*
 * 职位诱惑
 * bean
 * */
@Entity
public class Position_Advantage {
	@Id
	@GeneratedValue(strategy= GenerationType.IDENTITY)
	private int id;
	private String describ;

	public Position_Advantage() {
	}

	public Position_Advantage(String describ) {
		this.describ = describ;
	}

	@Override
	public String toString() {
		return "Position_Advantage{" +
				"id=" + id +
				", describ='" + describ + '\'' +
				'}';
	}

	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getDescrib() {
		return describ;
	}
	public void setDescrib(String describ) {
		this.describ = describ;
	}
}
