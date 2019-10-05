package com.example.model;

import com.example.model.Position;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface Position_Repository extends CrudRepository<Position, Integer> {

    List<Position> findByPosition(String position);

    Position findById(int id);
}
