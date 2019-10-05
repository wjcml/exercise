package com.example.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

/*
 * 职位
 * bean
 * */
@Entity
public class Position {
	@Id
	@GeneratedValue(strategy= GenerationType.IDENTITY)
	private int id;
	private String edu;
	private String exp;
	private String location;
	private String salary;
	private String postionDesc;
	private String position;
	private String publishTime;

	public Position() {
	}

	public Position(String edu, String exp, String location, String salary, String postionDesc, String position, String publishTime) {
		this.edu = edu;
		this.exp = exp;
		this.location = location;
		this.salary = salary;
		this.postionDesc = postionDesc;
		this.position = position;
		this.publishTime = publishTime;
	}

	@Override
	public String toString() {
		return "Position{" +
				"id=" + id +
				", edu='" + edu + '\'' +
				", exp='" + exp + '\'' +
				", location='" + location + '\'' +
				", salary='" + salary + '\'' +
				", postionDesc='" + postionDesc + '\'' +
				", position='" + position + '\'' +
				", publishTime='" + publishTime + '\'' +
				'}';
	}

	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getEdu() {
		return edu;
	}
	public void setEdu(String edu) {
		this.edu = edu;
	}
	public String getExp() {
		return exp;
	}
	public void setExp(String exp) {
		this.exp = exp;
	}
	public String getLocation() {
		return location;
	}
	public void setLocation(String location) {
		this.location = location;
	}
	public String getSalary() {
		return salary;
	}
	public void setSalary(String salary) {
		this.salary = salary;
	}
	public String getPostionDesc() {
		return postionDesc;
	}
	public void setPostionDesc(String postionDesc) {
		this.postionDesc = postionDesc;
	}
	public String getPosition() {
		return position;
	}
	public void setPosition(String position) {
		this.position = position;
	}
	public String getPublishTime() {
		return publishTime;
	}
	public void setPublishTime(String publishTime) {
		this.publishTime = publishTime;
	}
}
