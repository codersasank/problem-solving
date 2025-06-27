class Solution {
    public static int ceil(double a){
        if (a>=0)
            return ((int)a)==a?(int)a:(int)a+1;
        else
            return (int)a;
    }
    public static int floor(double a){
        if (a<0)
            return ((int)a)==a?(int)a:(int)a-1;
        else
            return (int)a;
    }
    public ArrayList<Integer> divFloorCeil(int a, int b) {
        // code here
        ArrayList<Integer> result = new ArrayList<>();
        result.add(floor((double)a/b));
        result.add(ceil((double)a/b));
        return result;
    }
}
