package com.example.model;

import com.example.model.Employee_Company;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface Employee_Company_Repository extends CrudRepository<Employee_Company, Integer> {

    List<Employee_Company> findByEmployeeId(int employeeId);

    Employee_Company findById(int id);
}
