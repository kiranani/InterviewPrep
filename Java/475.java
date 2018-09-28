class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        Arrays.sort(houses);
        Arrays.sort(heaters);
        int j = 0, max = 0, ans = 0;
        for (int i = 0; i < houses.length; i++) {
            while (j < heaters.length - 1) {
                if (Math.abs(houses[i] - heaters[j]) < Math.abs(houses[i] - heaters[j + 1])) {
                    break;
                }
                j++;
            }
            ans = Math.max(ans, Math.abs(houses[i] - heaters[j]));
        }
        return ans;
    }
}
