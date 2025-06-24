class Solution {
    public void setZeroes(int[][] matrix) {
        boolean foundZero = false;
        int storRow=0, storCol=0;
        for(storRow=0; storRow<matrix.length; storRow++){
            for(storCol=0; storCol<matrix[0].length; storCol++){
                if (matrix[storRow][storCol]==0){
                    foundZero = true;
                    break;
                }
            }
            if (foundZero)
                break;
        }
        if (!foundZero)
            return;
        for(int r=0; r<matrix.length; r++){
            if (matrix[r][storCol]==0)    
                matrix[r][storCol] = -1;
            else
                matrix[r][storCol] = 1;
        }
        for(int c=0; c<matrix[0].length; c++){
            if (matrix[storRow][c]==0)    
                matrix[storRow][c] = -1;
            else
                matrix[storRow][c] = 1;
        }
        matrix[storRow][storCol] = -1;
        for(int r=0; r<matrix.length; r++){
            for(int c=0; c<matrix[0].length; c++){
                if (matrix[r][c]==0){
                    matrix[storRow][c] = -1;
                    matrix[r][storCol] = -1;
                }
            }
        }
        for(int r=0; r<matrix.length; r++){
            for(int c=0; c<matrix[0].length; c++){
                if (r==storRow || c==storCol)
                    continue;
                if (matrix[storRow][c] == -1 || matrix[r][storCol] == -1)
                    matrix[r][c] = 0;
            }
        }
        for(int r=0; r<matrix.length; r++)
            matrix[r][storCol] = 0;
        for(int c=0; c<matrix[0].length; c++)
            matrix[storRow][c] = 0;
    }
}
