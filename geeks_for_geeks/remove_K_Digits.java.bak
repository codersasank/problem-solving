class Solution {
    public String removeKdigits(String S, int K) {
        int n = S.length(), popped = 0, idx = 1, i=0;
        int[] digits = new int[S.length()];
        for(i=0; i<S.length(); i++)
            digits[i] = S.charAt(i)-'0';
        if (K==n-1) return Integer.toString(Arrays.stream(digits).min().getAsInt());
        if (K==n) return "0";
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(S.charAt(0)-'0');
        while (idx < n)
        {
            while (!stack.isEmpty() && popped<K && (stack.peek()  > S.charAt(idx)-'0' ) )
            {
                stack.pop(); popped += 1;
            }
            stack.push(S.charAt(idx)-'0'); idx += 1;
        }
        int size = stack.size();
        for(i=idx; i<n; i++)
            stack.push(S.charAt(i)-'0');
        StringBuilder ret = new StringBuilder();
        while (!stack.isEmpty())
            ret.append(stack.pop());
        String retStr = ret.reverse().toString().substring(0,n-K);
        for (i=0; i<n-K; i++)
            if (retStr.charAt(i)!='0') break;
        if (i==n-K) return "0";
        return retStr.substring(i,n-K);
    }
}