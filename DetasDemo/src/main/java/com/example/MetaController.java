package com.example;

import com.example.test.ToMetaData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MetaController {
    @Autowired
    private ToMetaData toMetaData;

    @RequestMapping("/meta")
    public String saveMetaData(ModelMap model){
        toMetaData.saveMeta();
        return "hello";
    }
}
