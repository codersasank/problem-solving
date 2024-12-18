class Solution {
    public int largestAltitude(int[] gain) {
        int highest = 0, cur = 0, n = gain.length, i;
        for(i=0; i<n; i++)
        {
            cur += gain[i];
            if (cur > highest) highest = cur;
        }
        return highest;
    }
}