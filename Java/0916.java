class Solution {
    public List<String> wordSubsets(String[] A, String[] B) {
        Map<Character, Integer> hash = new HashMap<>();
        for (int i = 0; i < B.length; i++) {
            WordHash h = new WordHash(B[i]);
            for (Character c: h.hash.keySet()) {
                hash.put(c, Math.max(hash.getOrDefault(c, 0), h.hash.get(c)));
            }
        }
        List<String> ll = new ArrayList<>();
        for (int i = 0; i < A.length; i++) {
            WordHash h = new WordHash(A[i]);
            boolean uni = true;
            for (Character c: hash.keySet()) {
                if (hash.get(c) > h.hash.getOrDefault(c, 0)) {
                    uni = false;
                }
                if (!uni) {
                    break;
                }
            }
            if (uni) {
                ll.add(A[i]);
            }
        }
        return ll;
    }
}

class WordHash {
    public Map<Character, Integer> hash = new HashMap<>();
    public WordHash(String word) {
        for (int i = 0; i < word.length(); i++) {
            this.hash.put(word.charAt(i), this.hash.getOrDefault(word.charAt(i), 0) + 1);
        }
    }
}
