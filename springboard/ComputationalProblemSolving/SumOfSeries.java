package solutions;

import java.util.Scanner;

public class SumOfSeries {
	private static double getSeriesSum(int n) {
		double sum = 0;
		for(int i=1; i<=n; i++) {
			sum += 1.0/i;
		}
		return sum;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		double sum = getSeriesSum(n);
		System.out.println(sum);
	}

}
