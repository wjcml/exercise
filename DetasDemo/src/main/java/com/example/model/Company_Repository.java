package com.example.model;
import java.util.List;

import com.example.model.Company;
import org.springframework.data.repository.CrudRepository;

public interface Company_Repository extends CrudRepository<Company, Integer> {

        List<Company> findByName(String name);

        Company findById(int id);
}
