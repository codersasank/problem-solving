class Solution {
    public String makeFancyString(String s) {
        StringBuilder ret = new StringBuilder();
        for(int i=0; i<s.length(); i++){
            char ch = s.charAt(i);
            int j = i;
            while(j<s.length() && s.charAt(j)==ch)
                j++;
            if (j==s.length()){
                if(i==s.length()-1)
                    ret.append(ch);
                else{
                    ret.append(ch);
                    ret.append(ch);
                }
                break;
            }
            else if (j==i+1)
                ret.append(ch);
            else{
                ret.append(ch);
                ret.append(ch);
            }
            i = j-1;
        }
        return ret.toString();
    }
}
