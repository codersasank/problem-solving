package solutions;

import java.util.Scanner;

public class Fibonacci {
	private static void printFibonacci(int n) {
		int cur = 1, nxt = 1, cnt = 0;
		for(cnt = 0; cnt<n; cnt++) {
			System.out.print(cur + " ");
			int tmp = cur + nxt;
			cur = nxt;
			nxt = tmp;
		}
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		printFibonacci(n);
	}

}
