package com.example.model;

/*
 * 公司company
 * bean
 * */

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class Company {
	@Id
	@GeneratedValue(strategy= GenerationType.IDENTITY)
	private int id;
	private String mainPage;
	private String name;
	private String nature;
	private String scale;

	protected Company(){}

	public Company(String mainPage, String name, String nature, String scale){
		this.mainPage = mainPage;
		this.name = name;
		this.nature = nature;
		this.scale = scale;
	}
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getMainPage() {
		return mainPage;
	}
	public void setMainPage(String mainPage) {
		this.mainPage = mainPage;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getNature() {
		return nature;
	}
	public void setNature(String nature) {
		this.nature = nature;
	}
	public String getScale() {
		return scale;
	}
	public void setScale(String scale) {
		this.scale = scale;
	}

	@Override
	public String toString() {
		return String.format(
				"Company[%d, %s, %s, %s, %s]",
				id, mainPage, name, nature, scale);
	}
}
