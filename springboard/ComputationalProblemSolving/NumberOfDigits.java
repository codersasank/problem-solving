package solutions;

public class NumberOfDigits {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int num = 13349234;
		int cnt=0;
		while (num > 0) {
			num = num / 10;
			cnt++;
		}
		System.out.println(cnt);
		num = 13349234;
		cnt = 1 + (int) Math.log10(num);
		System.out.println(cnt);
	}

}
