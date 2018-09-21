class Solution {
    public int countNumbersWithUniqueDigits(int n) {
        int[] counts = new int[n];
        int total = 1;
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                counts[i] = 9;
            } else if (i < 10) {
                counts[i] = counts[i - 1] * (10 - i);
            } else {
                break;
            }
            //System.out.println(total + ":" + counts[i]);
            total += counts[i];
        }
        return total;
    }
}
