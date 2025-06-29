package solutions;

import java.util.Scanner;

public class RightAngleTriangle {
	
	private static void displayTriangle(int r) {
		for(int i=1; i<=r; i++) {
			for(int j=0;j<i-1;j++)
				System.out.print("* ");
			System.out.println("*");
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int r = in.nextInt();
		displayTriangle(r);
		in.close();
	}

}
