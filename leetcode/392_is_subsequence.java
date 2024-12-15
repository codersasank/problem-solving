class Solution {
    public boolean isSubsequence(String s, String t) {
        int idx_s = 0, idx_t = 0;
        int n_s = s.length(), n_t = t.length();
        while (idx_s < n_s && idx_t < n_t)
        {
            if (s.charAt(idx_s)==t.charAt(idx_t))
            {
                idx_s ++; idx_t ++;
                continue;
            }
            idx_t ++;
        }
        if (idx_s == n_s)
            return true;
        return false;        
    }
}