package com.example.model;

import com.example.model.Employee;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface Employee_Repository extends CrudRepository<Employee, Integer> {

    List<Employee> findByName(String name);

    Employee findById(int id);
}
