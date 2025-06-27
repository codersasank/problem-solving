package solutions;

public class CeilOfNumber {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double number = 8.37233;
		number = 8.0;
		int ceil = (int)number;
		ceil = (ceil==number)?ceil:ceil+1;
		System.out.println(ceil);
	}

}
