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
    public List<List<String>> printTree(TreeNode root) {
        Queue<AnnotatedNode> q = new LinkedList<>();
        List<AnnotatedNode> l = new ArrayList<>();
        q.add(new AnnotatedNode(root, 1, 1));
        int pos, c = 0;
        while (q.size() > 0) {
            AnnotatedNode t = q.remove();
            l.add(t);
            c++;
            if (t.node.left != null) {
                pos = 2 * t.pos;
                q.add(new AnnotatedNode(t.node.left, t.level + 1, pos));
            }
            if (t.node.right != null) {
                pos = 2 * t.pos + 1;
                q.add(new AnnotatedNode(t.node.right, t.level + 1, pos));
            }
        }
        int lc = l.get(c - 1).level;
        int n = (1 << lc) - 1;
        List<List<String>> ans = new ArrayList<List<String>>();
        for (AnnotatedNode t: l) {
            if (t.level > ans.size()) {
                List<String> nl = new ArrayList<>();
                for (int i = 0; i < n; i++) {
                    nl.add("");
                }
                ans.add(nl);
            }
            int gap = (1 << (lc - t.level + 1)) - 1;
            int index = gap / 2 + (gap + 1) * (t.pos - (1 << (t.level - 1)));
            ans.get(t.level - 1).set(index, Integer.toString(t.node.val));
        }
        return ans;
    }
}

public class AnnotatedNode {
    public TreeNode node;
    public int level;
    public int pos;
    public AnnotatedNode(TreeNode node, int level, int pos) {
        this.node = node;
        this.level = level;
        this.pos = pos;
    }
}
