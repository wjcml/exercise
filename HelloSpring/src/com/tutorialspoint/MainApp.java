package com.tutorialspoint;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainApp {
	public static void main(String[] args) {
		ApplicationContext context = new ClassPathXmlApplicationContext("Beans.xml");
//		HelloWorld obj = (HelloWorld) context.getBean("hello");
//		obj.setMessage("hello world!!!!");
		HelloWorld objA = (HelloWorld) context.getBean("hello");
		objA.getMessage1();
		objA.getMessage2();

		HelloIndia objB = (HelloIndia) context.getBean("helloIndia");
		objB.getMessage1();
		objB.getMessage2();
		objB.getMessage3();
//		����bean
//		context.registerShutdownHook();

		AbstractApplicationContext cont =
		new ClassPathXmlApplicationContext("Beans.xml");
		hello_init_destroy obj = (hello_init_destroy) cont.getBean("init_destroy");
		obj.getMessage1();
		obj.getMessage2();
		cont.registerShutdownHook();
	}
}
