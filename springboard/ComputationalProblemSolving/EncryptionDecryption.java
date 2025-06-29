package solutions;

import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class EncryptionDecryption {
	private static String encrypt(String data, String key) {
		int digit1 = Character.getNumericValue(key.charAt(0));
		int digit2 = Character.getNumericValue(key.charAt(1));
		int digit3 = Character.getNumericValue(key.charAt(2));
		StringBuilder result = new StringBuilder();
		for(int i=0; i<data.length(); i++) {
			char ch = data.charAt(i);
			if (Character.isUpperCase(ch))
				ch -= digit1;
			else if (Character.isLowerCase(ch))
				ch -= digit2;
			else if (Character.isDigit(ch))
				ch -= digit3;
			result.append(ch);
		}
		return result.toString();
	}
	private static String decrypt(String data, String key) {
		int digit1 = Character.getNumericValue(key.charAt(0));
		int digit2 = Character.getNumericValue(key.charAt(1));
		int digit3 = Character.getNumericValue(key.charAt(2));
		StringBuilder result = new StringBuilder();
		for(int i=0; i<data.length(); i++) {
			char ch = data.charAt(i);
			if (Character.isUpperCase(ch+digit1))
				ch += digit1;
			else if (Character.isLowerCase(ch+digit2))
				ch += digit2;
			else if (Character.isDigit(ch+digit3))
				ch += digit3;
			result.append(ch);
		}
		return result.toString();
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		List<String> input = Arrays.stream(in.nextLine().split(",")).collect(Collectors.toList());
		String data = input.get(0);
		String key = input.get(1);
		String encryptedData = encrypt(data, key);
		String decryptedData = decrypt(encryptedData, key);
		System.out.println(encryptedData);
		System.out.println(decryptedData);
		
	}

}
