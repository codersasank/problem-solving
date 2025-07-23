class Solution {
    // Function to return an ArrayList with exact result and formatted result
    static ArrayList<Float> divisionWithPrecision(float a, float b) {
        // code here
        ArrayList<Float> ret = new ArrayList<>();
        ret.add(a/b);
        ret.add( Float.parseFloat(String.format("%.3f", a/b)) );
        return ret;
    }
}
