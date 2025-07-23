class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        if (source==destination) return true;
        boolean[][] path = new boolean[n][n];
        int i,j,k;
        for (i=0; i<edges.length; i++){
            path[edges[i][0]][edges[i][1]] = true;
            path[edges[i][1]][edges[i][0]] = true;
        }
        for (i=0; i<n; i++){
            for(j=i+1; j<n; j++){
                if (path[i][j]) continue;
                for(k=0; k<n; k++){
                    if (path[i][k] && path[k][j]){
                        path[i][j] = true;
                        path[j][i] = true;
                        break;
                    }
                }
            }
        }
        return path[source][destination];
    }
}
