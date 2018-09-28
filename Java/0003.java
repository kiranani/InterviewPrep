class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) {
            return 0;
        }
        Map<Character, Integer> cMap = new HashMap<Character, Integer>();
        int max = 0, minI = 0, maxI = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (cMap.containsKey(c)) {
                if (minI < cMap.get(c)) {
                    minI = cMap.get(c);
                }
            }
            max = Math.max(i - minI + 1, max);
            cMap.put(c, i + 1);
        }
        return max;
    }
}
