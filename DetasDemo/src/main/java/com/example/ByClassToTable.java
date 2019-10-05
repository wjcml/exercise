package com.example;

import com.example.model.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class ByClassToTable {

    private static final Logger log = LoggerFactory.getLogger(ByClassToTable.class);

    public static void main(String[] args) {
        SpringApplication.run(ByClassToTable.class);
    }

//    公司表
    @Bean
    public CommandLineRunner company_demo(Company_Repository companyRes) {
        return (args) -> {
            // 增
            log.info("");
            log.info("Company insert record:");
            companyRes.save(new Company("https://www.baidu.com", "baidu", "fuli", "fuli"));
            companyRes.save(new Company("https://www.taobao.com", "taobao", "fuli", "fuli"));
            companyRes.save(new Company("https://www.tianmao.com", "tianmao", "fuli", "fuli"));
            companyRes.save(new Company("https://www.jingdong.com", "jingdong", "fuli", "fuli"));
            log.info("");

            // 查,all
            log.info("Company found with findAll():");
            log.info("-------------------------------");
            for (Company companys : companyRes.findAll()) {
                log.info(companys.toString());
            }
            log.info("");

//            删
//            companyRes.deleteById(1);

            // 查，根据 ID
            Company company  = companyRes.findById(2);
            log.info("Company found with findById(2):");
            log.info("--------------------------------");
            log.info(company.toString());
            log.info("");

//            改
            company.setMainPage("google");
            company.setName("guge");
            companyRes.save(company);

            // 查,all
            log.info("Company found with findAll():");
            log.info("-------------------------------");
            for (Company companys : companyRes.findAll()) {
                log.info(companys.toString());
            }
            log.info("");

        };
    }

//    员工表
    @Bean
    public CommandLineRunner employee_demo(Employee_Repository employeeRes){
        return (args) -> {
            // 增
            log.info("");
            log.info("Employee insert record:");
            employeeRes.save(new Employee("hr", "hr"));
            employeeRes.save(new Employee("hr", "hr"));
            employeeRes.save(new Employee("hr", "hr"));
            employeeRes.save(new Employee("hr", "hr"));
            log.info("");

//             查,all
            log.info("Employee found with findAll():");
            log.info("-------------------------------");
            for (Employee employees : employeeRes.findAll()) {
                log.info(employees.toString());
            }
            log.info("");

//            删
//            companyRes.deleteById(1);

            // 查，根据 ID
            Employee employee  = employeeRes.findById(2);
            log.info("employee found with findById(2):");
            log.info("--------------------------------");
            log.info(employee.toString());
            log.info("");

//            改
            employee.setName("google");
            employeeRes.save(employee);

            // 查,all
            log.info("employee found with findAll():");
            log.info("-------------------------------");
            for (Employee employees : employeeRes.findAll()) {
                log.info(employees.toString());
            }
            log.info("");

        };
    }

//    职位
    @Bean
    public CommandLineRunner position_demo(Position_Repository positionRes){
        return (args) -> {
            // 增
            log.info("");
            log.info("Position insert record:");
            positionRes.save(new Position("ben", "1-3", "cd", "12000-15000", "asd", "kaifa", "3tianqian"));
            positionRes.save(new Position("ben", "1-3", "cd", "12000-15000", "asd", "kaifa", "3tianqian"));
            positionRes.save(new Position("ben", "1-3", "cd", "12000-15000", "asd", "kaifa", "3tianqian"));
            positionRes.save(new Position("ben", "1-3", "cd", "12000-15000", "asd", "kaifa", "3tianqian"));
            log.info("");

//             查,all
            log.info("Position found with findAll():");
            log.info("-------------------------------");
            for (Position positions : positionRes.findAll()) {
                log.info(positions.toString());
            }
            log.info("");

        };
    }

//    职位标签
    @Bean
    public CommandLineRunner position_tag_demo(Position_Tag_Repository positionTagRes){
        return (args) -> {
            // 增
            log.info("");
            log.info("PositionTag insert record:");
            positionTagRes.save(new Position_Tag("fjaks"));
            positionTagRes.save(new Position_Tag("fjaks"));
            positionTagRes.save(new Position_Tag("fjaks"));
            positionTagRes.save(new Position_Tag("fjaks"));
            log.info("");

    //             查,all
            log.info("PositionTag found with findAll():");
            log.info("-------------------------------");
            for (Position_Tag positiontags : positionTagRes.findAll()) {
                log.info(positiontags.toString());
            }
            log.info("");

        };
    }

//    职位诱惑
    @Bean
    public CommandLineRunner position_adv_demo(Position_Advantage_Repository positionAdvRes){
        return (args) -> {
            // 增
            log.info("");
            log.info("PositionAdv insert record:");
            positionAdvRes.save(new Position_Advantage("fas"));
            positionAdvRes.save(new Position_Advantage("fas"));
            positionAdvRes.save(new Position_Advantage("fas"));
            positionAdvRes.save(new Position_Advantage("fas"));
            log.info("");

            //             查,all
            log.info("PositionAdv found with findAll():");
            log.info("-------------------------------");
            for (Position_Advantage positionadvs : positionAdvRes.findAll()) {
                log.info(positionadvs.toString());
            }
            log.info("");

        };
    }

//    员工公司关联表
    @Bean
    public CommandLineRunner employee_company_demo(Employee_Company_Repository employeeCompanyRes){
        return (args) -> {
            // 增
            log.info("");
            log.info("EmployeeCompany insert record:");
            employeeCompanyRes.save(new Employee_Company(1, 1));
            employeeCompanyRes.save(new Employee_Company(2, 1));
            employeeCompanyRes.save(new Employee_Company(3, 1));
            employeeCompanyRes.save(new Employee_Company(4, 1));
            log.info("");

            //             查,all
            log.info("EmployeeCompany found with findAll():");
            log.info("-------------------------------");
            for (Employee_Company employeecompanys : employeeCompanyRes.findAll()) {
                log.info(employeecompanys.toString());
            }
            log.info("");

        };
    }

//    职位，公司，招聘者关联表
    @Bean
    public CommandLineRunner position_company_employee_demo(Position_Company_Employee_Repository positionCompanyEmpRes){
        return (args) -> {
            // 增
            log.info("");
            log.info("PositionCompanyEmployee insert record:");
            positionCompanyEmpRes.save(new Position_Company_Employee(1, 1, 1));
            log.info("");

            //             查,all
            log.info("PositionCompanyEmployee found with findAll():");
            log.info("-------------------------------");
            for (Position_Company_Employee pos_com_emp : positionCompanyEmpRes.findAll()) {
                log.info(pos_com_emp.toString());
            }
            log.info("");

        };
    }

//职位，职位诱惑关联
    @Bean
    public CommandLineRunner position_position_adv_demo(Position_Position_Advantage_Repository positionPosAdvRes){
        return (args) -> {
            // 增
            log.info("");
            log.info("PositionPositionAdv insert record:");
            positionPosAdvRes.save(new Position_Position_Advantage(1, 1));
            log.info("");

            //             查,all
            log.info("PositionPositionAdv found with findAll():");
            log.info("-------------------------------");
            for (Position_Position_Advantage pos_pos_adv : positionPosAdvRes.findAll()) {
                log.info(pos_pos_adv.toString());
            }
            log.info("");

        };
    }

//    职位，职位标签关联表
    @Bean
    public CommandLineRunner position_position_tag_demo(Position_Position_Tag_Repository positionPosTagRes){
        return (args) -> {
            // 增
            log.info("");
            log.info("PositionPositionTag insert record:");
            positionPosTagRes.save(new Position_Position_Tag(1, 1));
            log.info("");

            //             查,all
            log.info("PositionPositionTag found with findAll():");
            log.info("-------------------------------");
            for (Position_Position_Tag pos_pos_tag : positionPosTagRes.findAll()) {
                log.info(pos_pos_tag.toString());
            }
            log.info("");

        };
    }

//    元数据
    @Bean
    public CommandLineRunner metadata_demo(MetaData_Repository metadataRes){
        return (args) -> {
            // 增
            log.info("");
            log.info("PositionPositionTag insert record:");
            String metastr = "{'advantage': '五险一金 专业培训 晋升 良好薪资',\n" +
                    " 'company_main_page': 'http://www.lagou.com/gongsi/260435.html',\n" +
                    " 'company_name': '南天信息',\n" +
                    " 'company_nature': '其他',\n" +
                    " 'edu': '本科及以上 /',\n" +
                    " 'exp': '经验3-5年 /',\n" +
                    " 'hr_name': 'chen',\n" +
                    " 'hr_position': 'HR',\n" +
                    " 'location': '/成都 /',\n" +
                    " 'money': '10k-14k ',\n" +
                    " 'pos_desc_list': ['1、具备银联支付行业务开发经验；',\n" +
                    "                   '2、良好的沟通合作能力、文档编写能力，协调组织能力。',\n" +
                    "                   '3、熟悉软件开发流程，精通python开发。',\n" +
                    "                   '4、掌握Linux '\n" +
                    "                   '操作系统和大型数据库（Oracle）；对sql优化有丰富的经验；精通Oracle存储过程开发者优先；\\xa0',\n" +
                    "                   '5、熟悉统一支付平台者优先；',\n" +
                    "                   '6.面试时须提供项目案例；'],\n" +
                    " 'position': 'python开发工程师',\n" +
                    " 'publish_time': '2019-09-23',\n" +
                    " 'scale': '50-150人',\n" +
                    " 'spider_location': '192.168.189.1',\n" +
                    " 'stage': '上市公司',\n" +
                    " 'tag_list': ['MySQL'],\n" +
                    " 'uuid': UUID('ffd91148-df65-11e9-bce0-b8868799fb3c'),\n" +
                    " 'work_place': '成都-高新区-玉林'}";

            metadataRes.save(new MetaData("alksflasjflaj",  metastr));
            log.info("");

            //             查,all
            log.info("PositionPositionTag found with findAll():");
            log.info("-------------------------------");
            for (MetaData metadatas : metadataRes.findAll()) {
                log.info(metadatas.toString());
            }
            log.info("");

        };
    }
}
