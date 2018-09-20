class Solution {
    public int subarrayBitwiseORs(int[] A) {
        Set<Integer> s = new HashSet<Integer>();
        Set<Integer> s1 = new HashSet<Integer>();
        for (int i = 0; i < A.length; i++) {
            Set<Integer> s2 = new HashSet<Integer>();
            s2.add(A[i]);
            s.add(A[i]);
            for (Integer x: s1) {
                int y = x | A[i];
                s2.add(y);
                s.add(y);
            }
            s1 = s2;
        }
        return s.size();
    }
}
