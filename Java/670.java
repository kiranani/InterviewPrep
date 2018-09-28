class Solution {
    public int maximumSwap(int num) {
        int[] nums = Integer.toString(num).chars().toArray();
        int n = nums.length;
        if (n < 2) {
            return num;
        }
        int[] maxes = new int[n];
        maxes[n - 1] = nums[n - 1];
        boolean exists = false;
        for (int j = n - 2; j > -1; j--) {
            if (maxes[j + 1] > nums[j]) {
                maxes[j] = maxes[j + 1];
                exists = true;
            } else {
                maxes[j] = nums[j];
            }
        }
        if (!exists) {
            return num;
        }
        int i = 0;
        while (i < n - 1) {
            if (maxes[i] != nums[i]) {
                int j = i + 1;
                while (j < n - 1) {
                    if (maxes[j] != maxes[j + 1]) {
                        break;
                    }
                    j++;
                }
                int t = nums[i];
                nums[i] = nums[j];
                nums[j] = t;
                break;
            }
            i++;
        }
        int temp = 0;
        for (i = 0; i < n; i++) {
            temp *= 10;
            temp += Character.getNumericValue(nums[i]);
        }
        return temp;
    }    
}
