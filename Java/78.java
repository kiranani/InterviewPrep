class Solution {
    public List<List<Integer>> recurse(int[] nums, int index) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        if (index == nums.length) {
            ans.add(new ArrayList());
            return ans;
        }
        List<List<Integer>> subs = recurse(nums, index + 1);
        ans.addAll(subs);
        for (List<Integer> l: subs) {
            List<Integer> nl = new ArrayList<Integer>(l);
            nl.add(nums[index]);
            ans.add(nl);
        }
        return ans;
    }
    public List<List<Integer>> subsets(int[] nums) {
        return recurse(nums, 0);
    }
}
