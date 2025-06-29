package solutions;

import java.util.Scanner;

public class UppercaseOrLowerCase {
	private static String upperOrLower(char ch) {
		if (ch >= 'a' && ch<='z')
			return "Lowercase";
		else if (ch>= 'A' && ch<='Z')
			return "Uppercase";
		else
			return "Not alphabet";
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		char ch = in.next().charAt(0);
		System.out.println(upperOrLower(ch));
	}

}
