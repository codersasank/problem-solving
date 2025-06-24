class Solution {
    public int firstUniqChar(String s) {
        int present=0,check=0;
        for (int i=0; i<s.length(); i++){
            char ch = s.charAt(i);
            int pos = ch - 'a';
            if ( (present & (1<<pos)) ==0){
                present |= (1 << pos);
            }
            else if ( (check & (1<<pos)) ==0){
                check |= (1 << pos);
            }
        }
        //System.out.println(Integer.toBinaryString(check));
        for (int i=0; i<s.length(); i++){
            char ch = s.charAt(i);
            int pos = ch - 'a';
            if ( ((1<<pos) & check) == 0)
                return i;
        }
        return -1;
    }
}
