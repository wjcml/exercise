package com.example.model;

import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface MetaData_Repository extends CrudRepository<MetaData, Integer> {

    List<MetaData> findByUuid(String uuid);

    MetaData findById(int id);
}
