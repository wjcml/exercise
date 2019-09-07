package com.tutorialspoint;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainApp {
	public static void main(String[] args) {
		ApplicationContext context = new ClassPathXmlApplicationContext("Beans.xml");
	      HelloWorld obj = (HelloWorld) context.getBean("hello");
//	      obj.setMessage("hello world!!!!");
	      HelloWorld objA = (HelloWorld) context.getBean("hello");
	      objA.getMessage1();
	      objA.getMessage2();

	      HelloIndia objB = (HelloIndia) context.getBean("helloIndia");
	      objB.getMessage1();
	      objB.getMessage2();
	      objB.getMessage3();
	      //	      Ïú»Ùbean
//	      context.registerShutdownHook();
	}
}
