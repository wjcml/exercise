package com.example.model;

import com.example.model.Position_Tag;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface Position_Tag_Repository extends CrudRepository<Position_Tag, Integer> {

    List<Position_Tag> findByTag(String tag);

    Position_Tag findById(int id);
}
