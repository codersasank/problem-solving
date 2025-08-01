class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        int i,j;
        ret.add(new ArrayList<Integer>());
        ret.get(0).add(1);
        for(i=1; i<numRows; i++){
            ret.add(new ArrayList<Integer>());
            for(j=0; j<i+1; j++){
                int num = 0;
                if ( (j-1)>=0 ) num += ret.get(i-1).get(j-1);
                if ( j<i ) num += ret.get(i-1).get(j);
                ret.get(i).add(num);
            }
        }
        return ret;
    }
}
