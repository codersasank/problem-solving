class Solution {
    public int countHillValley(int[] nums) {
        int i=1, j, cnt=0;
        while(i<nums.length-1){
            if (nums[i-1]==nums[i]){
                i++;
                continue;
            }
            j = i;
            while ((nums[j]==nums[i]) && (i<nums.length-1)) i++;
            if ((i==nums.length-1) && (nums[i]==nums[j])) break;
            if (((nums[j]-nums[j-1]) ^ (nums[j]-nums[i])) >= 0) cnt++;
        }
        return cnt;
    }
}
