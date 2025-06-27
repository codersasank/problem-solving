package solutions;

public class SwapTwoNumbers {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a = 21 , b = 34;
		a = a ^ b;
		b = a ^ b;
		a = a ^ b;
		System.out.println(a + " " + b);
	}

}
