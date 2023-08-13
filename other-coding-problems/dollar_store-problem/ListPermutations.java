import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;

public class ListPermutations {

	public static double roundPrice(double price) {

		price = price * 100;
		price = Math.round(price);
		price = price / 100;
		return price;
	}

	public static void main(String[] args) {

		HashSet<List<Integer>> permutSet = new HashSet<List<Integer>>();
		HashSet<List<Integer>> combinSet = new HashSet<List<Integer>>();
		int n1, n2, n3, n4, n5, n6, n7;
		int[] itemCosts = { 107, 124, 154, 135 };

		Arrays.sort(itemCosts);
		

		for (n1 = 1; n1 <= 4; n1++) {

			for (n2 = 1; n2 <= 4; n2++) {

				for (n3 = 1; n3 <= 4; n3++) {

					for (n4 = 1; n4 <= 4; n4++) {

						for (n5 = 1; n5 <= 4; n5++) {

							for (n6 = 1; n6 <= 4; n6++) {

								for (n7 = 1; n7 <= 4; n7++) {

									List<Integer> numList = Arrays.asList(n1, n2, n3, n4, n5, n6, n7);
									permutSet.add(numList);
									Collections.sort(numList);
									combinSet.add(numList);

								}
							}

						}
					}
				}
			}
		}

		List<Double> costList = new ArrayList<Double>();
		for (List<Integer> choice : combinSet) {

			double actualCost = 0;
			for (Integer whichItem : choice) {

				actualCost = actualCost + itemCosts[whichItem - 1];
			}
			costList.add(actualCost);

		}
		//System.out.println(costList);

		for (int cnt = itemCosts[0]; cnt <= itemCosts[3]; cnt++) {

			double bundleCost;
			int[] flagCount = new int[itemCosts[3] - itemCosts[0] + 1];
			bundleCost = cnt / 1.0 * 7;
			for (Double costCnt : costList) {
				// 
				// 

				if (roundPrice(bundleCost) >= roundPrice(costCnt)) {
					flagCount[cnt - itemCosts[0]] = flagCount[cnt - itemCosts[0]] + 1;
				}
			}

			System.out.println("For a price of Rs " + cnt + ", there is a profit only in "
					+ flagCount[cnt - itemCosts[0]] + " out of 120 possible choices");
			double percentage;
			percentage = flagCount[cnt - itemCosts[0]] / 120.0 * 100;
			System.out.println(percentage + " % of the time there is no loss in case the price is Rs " + cnt);
			if (flagCount[cnt - itemCosts[0]] / 120.0 * 100 >= 90) {
				System.out.println("No loss if Rs " + (cnt) + " is the price.");
			}
		}

		
		System.out.println("The combinations are : " + combinSet);
		// System.out.println(permutSet.size());
		// System.out.println(combinSet.size());

	}

}
