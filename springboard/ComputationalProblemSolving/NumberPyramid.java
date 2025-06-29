package solutions;

import java.util.Scanner;

public class NumberPyramid {
	private static void displayPyramid(int r) {
		int spaces = 2*(r-1);
		for(int i=0; i<=r-1; i++) {
			for(int j=0; j<spaces; j++)
				System.out.print(" ");
			spaces-= 2;
			int tmp = (i+1);
			for(int j=0;j<i;j++)
				System.out.print((tmp++)+" ");
			for(int j=i;j<2*i;j++)
				System.out.print((tmp--)+" ");
		//	for(int j=0;j<2*i;j++)
		//		System.out.print((i+1)+" ");
			System.out.println(tmp--);
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int r = in.nextInt();
		displayPyramid(r);
		in.close();
	}

}
