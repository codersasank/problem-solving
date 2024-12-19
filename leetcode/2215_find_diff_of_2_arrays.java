class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        HashMap<Integer, Boolean> dict1 = new HashMap<Integer, Boolean>();
        HashMap<Integer, Boolean> dict2 = new HashMap<Integer, Boolean>();
        int i, n1 = nums1.length, n2=nums2.length;
        for(i=0; i<n1; i++) dict1.put(nums1[i], true);
        for(i=0; i<n2; i++) dict2.put(nums2[i], true);
        List<Integer> lst1 = new ArrayList<Integer>();
        List<Integer> lst2 = new ArrayList<Integer>();
        for(i=0; i<n1; i++)
        {
            if (!dict2.containsKey(nums1[i]))
            {
                lst1.add(nums1[i]);
                dict2.put(nums1[i], true);
            }
        }
        for(i=0; i<n2; i++)
        {
            if (!dict1.containsKey(nums2[i]))
            {
                lst2.add(nums2[i]);
                dict1.put(nums2[i], true);
            }
        }
        List<List<Integer>> result = new ArrayList<>();
        result.add(lst1);
        result.add(lst2);
        return result;
    }
}