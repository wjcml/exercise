package firstpackage;

import java.io.*;

public class BRRead {
    public static void main(String args[]) throws IOException {
    	
    	BRReadlines();
    	
        char c;
        // ʹ�� System.in ���� BufferedReader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("�����ַ�, ���� 'q' ���˳���");
        // ��ȡ�ַ�
        do {
            c = (char) br.read();
            System.out.println(c);
        } while (c != 'q');
    }
    
    public static void BRReadlines() throws IOException {
        // ʹ�� System.in ���� BufferedReader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str;
        System.out.println("Enter lines of text.");
        System.out.println("Enter 'end' to quit.");
        do {
            str = br.readLine();
            System.out.println(str);
        } while (!str.equals("end"));
    }
}