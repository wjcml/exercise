package com.example.model;

import com.example.model.Position_Position_Advantage;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface Position_Position_Advantage_Repository extends CrudRepository<Position_Position_Advantage, Integer> {

    Position_Position_Advantage findById(int id);
}
