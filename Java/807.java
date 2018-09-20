class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int[] maxY = new int[grid[0].length];
        int[] maxX = new int[grid.length];
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] > maxY[j]) {
                    maxY[j] = grid[i][j];
                }
                if (grid[i][j] > maxX[i]) {
                    maxX[i] = grid[i][j];
                }
            }
        }
        int total = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                int maxRise = Math.min(maxX[i], maxY[j]);
                int rise = maxRise > grid[i][j] ? maxRise - grid[i][j] : 0;
                total += rise;
            }
        }
        return total;
    }
}
