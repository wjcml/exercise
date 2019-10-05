package com.example.model;

import com.example.model.Position_Position_Tag;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface Position_Position_Tag_Repository extends CrudRepository<Position_Position_Tag, Integer> {

    Position_Position_Tag findById(int id);
}
