package solutions;

import java.util.HashMap;
import java.util.Scanner;

public class WeekendOrWeekday {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		HashMap<String, Boolean> weekday = new HashMap<>();
		weekday.put("Monday", true);
		weekday.put("Tuesday", true);
		weekday.put("Wednesday", true);
		weekday.put("Thursday", true);
		weekday.put("Friday", true);
		weekday.put("Saturday", false);
		weekday.put("Sunday", false);
		Scanner in = new Scanner(System.in);
		String day = in.next();
		if (weekday.containsKey(day)) {
			if (weekday.get(day))
				System.out.println("Weekday");
			else
				System.out.println("Weekend");
		}
		else
			System.out.println("Invalid");
	}

}
