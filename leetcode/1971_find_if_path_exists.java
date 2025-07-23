class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        if (source==destination) return true;
        ArrayList<Integer>[] graph = new ArrayList[n];
        for(int i=0; i<n; i++){
            graph[i] = new ArrayList<>();
        }
        for (int i=0; i<edges.length; i++){
            graph[edges[i][0]].add(edges[i][1]);
            graph[edges[i][1]].add(edges[i][0]);
        }
        HashMap<Integer, Boolean> visited = new HashMap<>();
        Stack<Integer> stack = new Stack<>();
        stack.push(source);
        while(stack.size()!=0){
            int top = stack.peek();
            if (visited.containsKey(top)){
                stack.pop();
                continue;
            }
            for(Integer node: graph[top]){
                if (node==destination)
                    return true;
                if (!visited.containsKey(node))
                    stack.push(node);     
            }       
            visited.put(top, true);
        }
        return false;
    }
}
