class Solution{
	private int n;
	private List<Integer> ret;
    Solution() {
    	ret = new ArrayList<Integer>();
    }
    public void print_pat(int cur, boolean decrement)
    {
        ret.add(cur);
        if (decrement)
        {
            if (cur>0)
                print_pat(cur-5, true);
            else if (cur==this.n)
                return;
            else
                print_pat(cur+5, false);
        }
        else
        {
            if (cur<this.n)
                print_pat(cur+5, false);
            else
                return;
        }
    }
    public List<Integer> pattern(int N){
        this.n = N;
        print_pat(N, true);
        return this.ret;
    }
}