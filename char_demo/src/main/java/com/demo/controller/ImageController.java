package com.demo.controller;

import com.demo.api.ApiResponse;
import com.demo.model.Image;
import com.demo.model.ImageRepository;
import com.google.common.hash.Hashing;
import net.sf.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.nio.charset.StandardCharsets;
import java.util.ArrayList;

@RestController
@RequestMapping("/img")
public class ImageController {
    @Autowired
    private ImageRepository imageRepository;

    @CrossOrigin
    @RequestMapping("/addImg")
    public ApiResponse addImg(@RequestParam(value = "image") String img){
        imageRepository.save(new Image(img));
        ApiResponse apiResponse = new ApiResponse("success", img);
        return apiResponse;
    }

    @CrossOrigin
    @RequestMapping("/toASCII")
    public ApiResponse toASCII(){
        ArrayList<Integer> list = new ArrayList<>();
        list.add(67);
        list.add(68);
        list.add(71);
        list.add(69);
        list.add(69);
        list.add(75);
        list.add(67);
        list.add(65);
        list.add(77);
        list.add(80);
        StringBuffer sbu = new StringBuffer();
        for(int l: list){
            sbu.append((char) l);
        }
        return new ApiResponse("success", sbu);
    }

    @CrossOrigin
    @RequestMapping("/getHash")
    public ApiResponse addImg(){
        String dataString = "{\n" +
                "\"advantage\": [\"五险一金\", \"团建\"],\n" +
                "\"companyMainPage\": \"https://www.lagou.com/gongsi/420697.html\",\n" +
                "\"companyName\": \"成都玛尔斯科技有限公司\",\n" +
                "\"companyNature\": [\"移动互联网\", \"社交\"],\n" +
                "\"edu\": \"本科及以上\",\n" +
                "\"exp\": \"经验3-5年\",\n" +
                "\"hrName\": \"黄小姐\",\n" +
                "\"hrPosition\": \"招聘专员\",\n" +
                "\"location\": \"成都\",\n" +
                "\"salary\": \"14k-18k\",\n" +
                "\"posDesc\": \"职位描述：\\n1.负责部门产品系统的服务器端架构，开发与维护工作\\n2.参与产品设计，与产品，运营和前端" +
                "工程师一同探讨技术方案\\n3.持续改进现有代码以应对日益增长的多样化需求\\n岗位要求：\\n1、3年以上python项目开发经验，" +
                "计算机相关专业背景\\n2、学习能力强，逻辑思维敏锐，积极主动\\n3、数据结构，算法基础扎实\\n4、熟悉Dja" +
                "ngo，drf，对前端知识有一定了解\\n5、熟悉mysql，redis\\n6、熟悉Linux的使用和管理\\n7. 熟悉Git\",\n" +
                "\"position\": \"Python开发工程师\",\n" +
                "\"scale\": \"15-50人\",\n" +
                "\"stage\": \"未融资\",\n" +
                "\"tagList\": [\"证券/期货\", \"基金\", \"Python\", \"MySQL\", \"区块链\", \"前端开发\"],\n" +
                "\"publishTime\": \"2019-09-28 17:00:10\",\n" +
                "\"spiderUuid\": \"afe737ef-2e14-472e-80d7-af9f9f8c5cab\"\n" +
                "}\n";
        String sha256hex = Hashing.sha256().hashString(dataString, StandardCharsets.UTF_8).toString();

        return new ApiResponse("success", sha256hex);
    }
}
