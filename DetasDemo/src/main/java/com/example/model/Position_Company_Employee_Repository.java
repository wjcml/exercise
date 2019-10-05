package com.example.model;

import com.example.model.Position_Company_Employee;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface Position_Company_Employee_Repository extends CrudRepository<Position_Company_Employee, Integer> {

    Position_Company_Employee findById(int id);
}
