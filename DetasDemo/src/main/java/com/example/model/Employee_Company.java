package com.example.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

/*
 * 公司和职员关联表
 * bean
 * */
@Entity
public class Employee_Company {
	@Id
	@GeneratedValue(strategy= GenerationType.IDENTITY)
	private int id;
	private int employeeId;
	private int companyId;

	public Employee_Company() {
	}

	public Employee_Company(int employeeId, int companyId) {
		this.employeeId = employeeId;
		this.companyId = companyId;
	}

	@Override
	public String toString() {
		return "Employee_Company{" +
				"id=" + id +
				", employeeId=" + employeeId +
				", companyId=" + companyId +
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
}
