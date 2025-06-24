import java.util.Stack;
class Solution {
    public List<Integer> findKDistantIndices(int[] nums, int key, int k) {
        if (nums.length==1){
            if (nums[0]==key)
                return Arrays.asList(0);
            return new ArrayList<Integer>();
        }
        Stack<Integer> stack1 = new Stack<>();
        Stack<Integer> stack2 = new Stack<>();
        ArrayList<Integer> list = new ArrayList<>();
        for (int i=nums.length-1; i>=0; i--){
            if (nums[i]==key){
                stack1.push(i);
                stack2.push(i);
            }
        }
        for(int i=0;i<nums.length;i++){
            if (stack1.isEmpty() && stack2.isEmpty())
                break;
            while (!stack1.isEmpty() && i-((int) stack1.peek()) > k )
                stack1.pop();
            //System.out.println(i + " s1 " + stack1.peek());
            if (!stack1.isEmpty() && ((int)stack1.peek()) <= i ){
                list.add(i);
                continue;
            }
            while (!stack2.isEmpty() && ((int) stack2.peek()) < i )
                stack2.pop();
            //System.out.println(i + " s2 " + stack2.peek());
            if (!stack2.isEmpty() && ((int)stack2.peek())-i <= k ){
                list.add(i);
                continue;
            }
        }
        return list;
    }
}
