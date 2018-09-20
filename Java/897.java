/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<TreeNode> l = new ArrayList<TreeNode>();
    public TreeNode increasingBST(TreeNode root) {
        recurse(root);
        for (int i = 0; i < l.size() - 1; i++) {
            l.get(i).right = l.get(i + 1);
        }
        return l.get(0);
    }
    public void recurse(TreeNode root) {
        if (root == null) {
            return;
        }
        recurse(root.left);
        l.add(root);
        TreeNode r = root.right;
        root.left = null;
        root.right = null;
        recurse(r);
    }
}
