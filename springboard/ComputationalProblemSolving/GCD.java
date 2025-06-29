package solutions;

import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class GCD {

	private static int getGCD(int a, int b) {
		if (a<b) {
			int tmp = a;
			a = b;
			b = tmp;
		}
		if (b==0)
			return -1;
		if (b==1)
			return 1;
		if (a%b==0)
			return b;
		else
			return getGCD(b, a%b);
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		String input = in.next();
		List<Integer> nums = Arrays.stream(input.split(",")).map(Integer::parseInt).collect(Collectors.toList());
		int gcd = getGCD(nums.get(0), nums.get(1));
		System.out.println(gcd);
	}

}
