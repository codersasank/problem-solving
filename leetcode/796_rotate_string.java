class Solution {
    public boolean rotateString(String s, String goal) {
        if (s.length() != goal.length())
            return false;
        String new_s = s + s;
        return new_s.indexOf(goal)!=-1;
    }
}
