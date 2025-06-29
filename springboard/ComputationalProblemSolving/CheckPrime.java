package solutions;

import java.util.Scanner;

public class CheckPrime {
	private static boolean checkPrime(int n) {
		if (n==1)
			return false;
		for (int i=2; i<=(int)Math.sqrt(n); i++) {
			if (n%i==0)
				return false;
		}
		return true;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		boolean isPrime =  checkPrime(n);
		System.out.println(isPrime);
	}
}
