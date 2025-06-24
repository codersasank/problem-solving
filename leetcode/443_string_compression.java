class Solution {
    public int compress(char[] chars) {
        int front = 0, last = 0;
        if (chars.length==1)
            return 1;
        while (last<chars.length){
            int cnt = 0;
            char ch = chars[last];
            while (last<chars.length && chars[last]==ch){
                last++;
                cnt++;
            }
            chars[front++] = ch;
            if (cnt > 1){
                char[] number = String.valueOf(cnt).toCharArray();
                for (char digit: number)
                    chars[front++] = digit;
            }
            if (last == chars.length-1 && chars[last]==ch)
                break;
        }
        return front;
    }
}
