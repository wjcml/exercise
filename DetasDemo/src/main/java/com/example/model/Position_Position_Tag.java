package com.example.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

/*
 * 职位和职位标签关联表
 * bean
 * */
@Entity
public class Position_Position_Tag {
	@Id
	@GeneratedValue(strategy= GenerationType.IDENTITY)
	private int id;
	private int tagId;
	private int positionId;

	public Position_Position_Tag() {
	}

	public Position_Position_Tag(int tagId, int positionId) {
		this.tagId = tagId;
		this.positionId = positionId;
	}

	@Override
	public String toString() {
		return "Position_Position_Tag{" +
				"id=" + id +
				", tagId=" + tagId +
				", positionId=" + positionId +
				'}';
	}

	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public int getTagId() {
		return tagId;
	}
	public void setTagId(int tagId) {
		this.tagId = tagId;
	}
	public int getPositionId() {
		return positionId;
	}
	public void setPositionId(int positionId) {
		this.positionId = positionId;
	}
}
