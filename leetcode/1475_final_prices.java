class Solution {
    public int[] finalPrices(int[] prices) {
        int n = prices.length, i, j;
        int[] answer = new int[n];
        for (i=0; i<n-1; i++)
        {
            j = i+1;
            while (j<n && prices[j]>prices[i]) j++;
            if (j==n) answer[i] = prices[i];
            else answer[i] = prices[i] - prices[j];
        }
        answer[n-1] = prices[n-1];
        return answer;
    }
}