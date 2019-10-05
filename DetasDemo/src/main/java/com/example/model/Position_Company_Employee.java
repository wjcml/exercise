package com.example.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

/*
 * 职位，公司，职员关联表
 * bean
 * */
@Entity
public class Position_Company_Employee {
	@Id
	@GeneratedValue(strategy= GenerationType.IDENTITY)
	private int id;
	private int employeeId;
	private int companyId;
	private int positonId;

	public Position_Company_Employee() {
	}

	public Position_Company_Employee(int employeeId, int companyId, int positonId) {
		this.employeeId = employeeId;
		this.companyId = companyId;
		this.positonId = positonId;
	}

	@Override
	public String toString() {
		return "Position_Company_Employee{" +
				"id=" + id +
				", employeeId=" + employeeId +
				", companyId=" + companyId +
				", positonId=" + positonId +
				'}';
	}

	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public int getEmployeeId() {
		return employeeId;
	}
	public void setEmployeeId(int employeeId) {
		this.employeeId = employeeId;
	}
	public int getCompanyId() {
		return companyId;
	}
	public void setCompanyId(int companyId) {
		this.companyId = companyId;
	}
	public int getPositonId() {
		return positonId;
	}
	public void setPositonId(int positonId) {
		this.positonId = positonId;
	}
}
