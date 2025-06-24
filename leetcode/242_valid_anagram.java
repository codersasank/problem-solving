class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length()!=t.length())
            return false;
        int[] count = new int[26];
        for(int i=0; i<s.length(); i++){
            int pos = s.charAt(i) - 'a';
            count[pos] += 1;
        }
        for(int i=0; i<t.length(); i++){
            int pos = t.charAt(i) - 'a';
            count[pos] -= 1;
            if (count[pos] < 0)
                return false;
        }
        return true;
    }
}
