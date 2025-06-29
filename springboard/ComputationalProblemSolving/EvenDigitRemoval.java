package solutions;

import java.util.Scanner;

public class EvenDigitRemoval {
	private static int reverseNum(int n) {
		int rev = 0;
		while (n > 0) {
			rev = rev*10 + n%10;
			n /= 10;
		}
		return rev;
	}
	private static int removeEven(int n) {
		int result = 0;
		while(n>0) {
			int digit = (n%10);
			n /= 10;
			if (digit%2==0) continue;
			result = result*10 + digit;
		}
		result = reverseNum(result);
		return result;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		System.out.println(removeEven(n));
	}

}
