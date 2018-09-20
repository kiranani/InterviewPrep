class KthLargest {
    private Queue<Integer> minHeap = new PriorityQueue<Integer>();
    private int K;
    public KthLargest(int k, int[] nums) {
        K = k;
        int i;
        for (i = 0; i < k && i < nums.length; i++) {
            minHeap.add(nums[i]);
        }
        for (;i < nums.length; i++) {
            this.add(nums[i]);
        }
    }
    
    public int add(int val) {
        if (minHeap.size() < K) {
            minHeap.add(val);
            return minHeap.peek();
        }
        if (minHeap.peek() < val) {
            minHeap.remove();
            minHeap.add(val);
        }
        return minHeap.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
