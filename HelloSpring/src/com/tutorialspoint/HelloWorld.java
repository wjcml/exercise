package com.tutorialspoint;

import org.springframework.beans.factory.annotation.Required;

public class HelloWorld {
	private String message1;
	   private String message2;
	   @Required
	   public void setMessage1(String message){
	      this.message1  = message;
	   }
	   @Required
	   public void setMessage2(String message){
	      this.message2  = message;
	   }
	   public void getMessage1(){
	      System.out.println("World Message1111 : " + message1);
	   }
	   public void getMessage2(){
	      System.out.println("World Message2222 : " + message2);
	   }
}
