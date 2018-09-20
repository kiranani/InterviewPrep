class Solution {
    public int coinChange(int[] coins, int amount) {
        Arrays.sort(coins);
        int[] amounts = new int[amount + 1];
        //System.out.println(coins[0]);
        int ans = recurse(coins, amount, amounts);
        return ans;
    }
    
    public int recurse(int[] coins, int amount, int[] amounts) {
        if (amount < 0) {
            return -1;
        } else if (amount == 0 || amounts[amount] != 0) {
            return amounts[amount];
        } else {
            int minCount = amount + 1;
            for (Integer coin: coins) {
                int count = recurse(coins, amount - coin, amounts);
                if (count != -1 && count < minCount) {
                    minCount = count;
                }
            }
            if (minCount != amount + 1) {
                amounts[amount] = 1 + minCount;
            } else {
                amounts[amount] = -1;
            }
            return amounts[amount];
        }
    }
}
