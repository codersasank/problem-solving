class Solution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        int cnt = 0;
        for(int fruit:fruits){
            boolean found = false;
            for(int i=0; i<baskets.length; i++){
                if (baskets[i]>= fruit){
                    baskets[i] = 0;
                    found = true;
                    break;
                }
            }
            if (!found) cnt++;
        }
        return cnt;
    }
}
