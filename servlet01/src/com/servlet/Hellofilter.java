package com.servlet;

import java.io.IOException;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;

public class Hellofilter implements Filter {

	@Override
	public void destroy() {
		// TODO Auto-generated method stub

	}

	@Override
	public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
			throws IOException, ServletException {
		// TODO Auto-generated method stub
		// ���վ������
        System.out.println("վ����ַ��http://www.runoob.com");

        // �����󴫻ع�����
        chain.doFilter(req,res);

	}

	@Override
	public void init(FilterConfig config) throws ServletException {
		// TODO Auto-generated method stub
		// ��ȡ��ʼ������
//        String site = config.getInitParameter("Site"); 

        // �����ʼ������
//        System.out.println("��վ����: " + site); 
		
		System.out.println("===============================");
		String initParam = config.getInitParameter("Site");
		System.out.println("Site ========" + initParam);

	}

}
