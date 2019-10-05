package com.example.test;

import com.example.model.MetaData;
import com.example.model.MetaData_Repository;
import net.sf.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Collections;
import java.util.Properties;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringDeserializer;

@Service
public class ToMetaData {

    @Autowired
    private MetaData_Repository metadataRes;

    public void saveMeta(){
        String dataStr = "{\"position\": \"python开发工程师\", \"money\": \"10k-14k \", \"location\": \"/成都 /\", \"exp\": \"经验3-5年 /\", \"edu\": \"本科及以上 /\", \"tag_list\": [\"MySQL\"], \"advantage\": \"五险一金 专业培训 晋升 良好薪资\", \"pos_desc_list\": [\"1、具备银联支付行业务开发经验；\", \"2、良好的沟通合作能力、文档编写能力，协调组织能力。\", \"3、熟悉软件开发流程，精通python开发。\", \"4、掌握Linux 操作系统和大型数据库（Oracle）；对sql优化有丰富的经验；精通Oracle存储过程开发者优先； \", \"5、熟悉统一支付平台者优先；\", \"6.面试时须提供项目案例；\"], \"hr_name\": \"chen\", \"hr_position\": \"HR\", \"company_name\": \"南天信息\", \"company_nature\": \"其他\", \"stage\": \"上市公司\", \"scale\": \"50-150人\", \"company_main_page\": \"http://www.lagou.com/gongsi/260435.html\", \"publish_time\": \"2019-09-27\", \"work_place\": \"成都-高新区-玉林\", \"uuid\": \"8b24154a-e0d8-11e9-a33c-b8868799fb3c\", \"spider_location\": \"192.168.189.1\"}";
        JSONObject json = JSONObject.fromObject(dataStr);
        String uuid = json.getString("uuid");

        //通过调用Session的save方法把对象保存到数据库,插入一条数据
        MetaData metadata = new MetaData();
        metadata.setUuid(uuid);
        metadata.setMeta(dataStr);
        this.metadataRes.save(metadata);

    }

}
