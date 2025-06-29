package solutions;

import java.util.Scanner;

public class FloydsTriangle {
	private static void displayTriangle(int r) {
		int cnt = 1;
		for(int i=1; i<=r; i++) {
			for(int j=1;j<i;j++)
				System.out.print( (cnt++) + " ");
			System.out.println(cnt++);
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
