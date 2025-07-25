class Solution {
    public int maxSum(int[] nums) {
        int max = Arrays.stream(nums).max().getAsInt();
        if (max < 0)
            return max;
        int sum = 0;
        boolean[] present = new boolean[101];
        for(int num: nums){
            if (num<=0 || present[num]) continue;
            sum += num;
            present[num] = true;
        }
        return sum;
    }
}
