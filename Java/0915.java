class Solution {
    public int partitionDisjoint(int[] A) {
        int n = A.length;
        int[] mins = new int[n];
        int[] maxes = new int[n];
        maxes[0] = A[0];
        mins[n - 1] = A[n - 1];
        for (int i = 1; i < n; i++) {
            maxes[i] = maxes[i - 1] > A[i] ? maxes[i - 1] : A[i];
            mins[n - i - 1] = mins[n - i] > A[n - i - 1] ? A[n - i - 1] : mins[n - i];
        }
        int i = 0;
        while (i < n - 1) {
            if (maxes[i] <= mins[i + 1]) {
                break;
            }
            i++;
        }
        return i + 1;
    }
}
