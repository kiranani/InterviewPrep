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
    public int widthOfBinaryTree(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Deque<LevelIndexNode> q = new ArrayDeque<>();
        int maxWidth = 0;
        q.addLast(new LevelIndexNode(1, 0, root));
        while (q.size() > 0) {
            if (q.peekFirst().level == q.peekLast().level) {
                int width = q.peekLast().index - q.peekFirst().index + 1;
                maxWidth = Math.max(maxWidth, width);
            }
            LevelIndexNode temp = q.removeFirst();
            if (temp.node.left != null) {
                q.addLast(new LevelIndexNode(temp.level + 1, 2 * temp.index + 1, temp.node.left));
            }
            if (temp.node.right != null) {
                q.addLast(new LevelIndexNode(temp.level + 1, 2 * temp.index + 2, temp.node.right));
            }
        }
        return maxWidth;
    }
}

public class LevelIndexNode {
    public int level, index;
    public TreeNode node;
    public LevelIndexNode(int level, int index, TreeNode node) {
        this.level = level;
        this.index = index;
        this.node = node;
    }
}
