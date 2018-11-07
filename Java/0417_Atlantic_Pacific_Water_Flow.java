class Solution {
    public int[][] dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    public int m, n;
    public List<int[]> pacificAtlantic(int[][] matrix) {
        List<int[]> ans = new ArrayList<int[]>();
        m = matrix.length;
        if (m == 0) {
            return ans;
        }
        n = matrix[0].length;
        boolean[][] pacifica = new boolean[m][n], atlantic = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            if (!pacifica[i][0]) {
                pacifica[i][0] = true;
                dfs(pacifica, matrix, i, 0);
            }
            if (!atlantic[i][n - 1]) {
                atlantic[i][n - 1] = true;
                dfs(atlantic, matrix, i, n - 1);
            }
        }
        for (int j = 0; j < n; j++) {
            if (!pacifica[0][j]) {
                pacifica[0][j] = true;
                dfs(pacifica, matrix, 0, j);
            }
            if (!atlantic[m - 1][j]) {
                atlantic[m - 1][j] = true;
                dfs(atlantic, matrix, m - 1, j);
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (atlantic[i][j] && pacifica[i][j]) {
                    int[] coord = {i, j};
                    ans.add(coord);
                }
            }
        }
        return ans;
    }
    public void dfs(boolean[][] dp, int[][] matrix, int i, int j) {
        for (int[] dir: dirs) {
            int ni = i + dir[0], nj = j + dir[1];
            if (-1 < ni && ni < m && -1 < nj && nj < n && !dp[ni][nj] && matrix[i][j] <= matrix[ni][nj]) {
                dp[ni][nj] = true;
                dfs(dp, matrix, ni, nj);
            }
        }
    }
}
