class Solution {
    public int diagonalSum(int[][] mat) {
        int n = mat.length;
        int sum = 0;
        
        for (int i = 0; i < n; i++) {
            sum += mat[i][i]; // Primary diagonal
            sum += mat[i][n - 1 - i]; // Secondary diagonal
        }
        
        // If the dimension is odd, the middle element is added twice, 
        // so we need to subtract it once
        if (n % 2 != 0) {
            sum -= mat[n / 2][n / 2];
        }
        
        return sum;
    }
}
