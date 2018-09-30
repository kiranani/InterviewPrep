class Solution {
    public boolean hasGroupsSizeX(int[] deck) {
        Map<Integer, Integer> hash = new HashMap<>();
        for (int i = 0; i < deck.length; i++) {
            hash.put(deck[i], hash.getOrDefault(deck[i], 0) + 1);
        }
        int gcd = 0;
        for (Integer k: hash.keySet()) {
            if (hash.get(k) < 2) {
                return false;
            }
            gcd = gcd == 0 ? hash.get(k) : gcd(gcd, hash.get(k));
            if (gcd < 2) {
                return false;
            }
        }
        return true;
    }
    
    public int gcd(int a, int b) {
        if (a == 1 || b == 1) {
            return 1;
        }
        if (a == b) {
            return a;
        }
        if (a > b) {
            return gcd(a - b, b);
        }
        return gcd(a, b - a);
    }
}
