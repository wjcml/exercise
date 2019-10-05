package com.example.model;

import com.example.model.Position_Advantage;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface Position_Advantage_Repository extends CrudRepository<Position_Advantage, Integer> {

    List<Position_Advantage> findByDescrib(String describ);

    Position_Advantage findById(int id);
}
