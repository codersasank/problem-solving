class Solution {
    public boolean isPowerOfTwo(int n) {
        int cnt = 0;
        while (n > 0){
            int bit = n & 1;
            if (bit==1) cnt++;
            n = n>>1;
        }
        return cnt==1;
    }
}
