package firstpackage;

public class TestArray {
	public static void main(String[] args) {
	      // �����С
	      int size = 10;
	      // ��������
	      double[] myList = new double[size];
	      myList[0] = 5.6;
	      myList[1] = 4.5;
	      myList[2] = 3.3;
	      myList[3] = 13.2;
	      myList[4] = 4.0;
	      myList[5] = 34.33;
	      myList[6] = 34.0;
	      myList[7] = 45.45;
	      myList[8] = 99.993;
	      myList[9] = 11123;
	      // ��������Ԫ�ص��ܺ�
	      double total = 0;
	      for (int i = 0; i < size; i++) {
	         total += myList[i];
	      }
	      System.out.println("�ܺ�Ϊ�� " + total);
//	      System.out.println(myList);
	      
	      name();
	      forEach();
	      printArray(myList);
	      
	   }
	
	public static void name() {
		double[] myList = {1.9, 2.9, 3.4, 3.5};
		 
	      // ��ӡ��������Ԫ��
	      for (int i = 0; i < myList.length; i++) {
	         System.out.println(myList[i] + " ");
	      }
	      // ��������Ԫ�ص��ܺ�
	      double total = 0;
	      for (int i = 0; i < myList.length; i++) {
	         total += myList[i];
	      }
	      System.out.println("Total is " + total);
	      // �������Ԫ��
	      double max = myList[0];
	      for (int i = 1; i < myList.length; i++) {
	         if (myList[i] > max) max = myList[i];
	      }
	      System.out.println("Max is " + max);
	}
	
	public static void forEach() {
		double[] myList = {1.9, 2.9, 3.4, 3.5};
		 
	      // ��ӡ��������Ԫ��
	      for (double element: myList) {
	         System.out.println(element);
	      }
	}
	
	public static void printArray(double[] myList) {
		  for (int i = 0; i < myList.length; i++) {
		    System.out.print(myList[i] + " ");
		  }
		}
}


