package com.example.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

/*
 * 职位和职位诱惑关联表
 * bean
 * */
@Entity
public class Position_Position_Advantage {
	@Id
	@GeneratedValue(strategy= GenerationType.IDENTITY)
	private int id;
	private int advantageId;
	private int positionId;

	public Position_Position_Advantage() {
	}

	public Position_Position_Advantage(int advantageId, int positionId) {
		this.advantageId = advantageId;
		this.positionId = positionId;
	}

	@Override
	public String toString() {
		return "Position_Position_Advantage{" +
				"id=" + id +
				", advantageId=" + advantageId +
				", positionId=" + positionId +
				'}';
	}

	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public int getAdvantageId() {
		return advantageId;
	}
	public void setAdvantageId(int advantageId) {
		this.advantageId = advantageId;
	}
	public int getPositionId() {
		return positionId;
	}
	public void setPositionId(int positionId) {
		this.positionId = positionId;
	}
	
}
