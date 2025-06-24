class Solution {
    public String[] divideString(String s, int k, char fill) {
        int num = (int) Math.ceil(s.length()*1.0/k);
        String[] arr = new String[num];
        int i;
        for(i=0; i<num-1; i++)
            arr[i] = s.substring(i*k , (i+1)*k);
        arr[num-1] = s.substring((num-1)*k, s.length()) + new String(new char[k- (s.length()-(num-1)*k) ]).replace('\0', fill);
        return arr;
    }
}
