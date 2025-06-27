package solutions;

import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class CoinChange {
	public static int numCoins(int x, int y, int z) {
		int remaining = z, coins=0;
		if (z<=y) return z;
		if (remaining/5 > x)
			coins += x;
		else
			coins += remaining/5;
		remaining -= coins*5;
		if (remaining > y)
			return -1;
		else
			return coins+remaining;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		String line = in.nextLine();
		List<Integer> inputs = Arrays.stream(line.split(",")).map(Integer::parseInt).collect(Collectors.toList());
		int x = inputs.get(0);
		int y = inputs.get(1);
		int z = inputs.get(2);
		int coins = numCoins(x,y,z);
		System.out.println(coins);
		in.close();
	}

}
