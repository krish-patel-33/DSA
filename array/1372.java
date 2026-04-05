/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int maxStep = 0;

    public int longestZigZag(TreeNode root) {
        if (root == null) return 0;
        
        // Start DFS traversal from root in both directions
        dfs(root, true, 0);
        dfs(root, false, 0);
        
        return maxStep;
    }

    private void dfs(TreeNode node, boolean goLeft, int step) {
        if (node == null) return;
        
        // Update the maximum zigzag length found so far
        maxStep = Math.max(maxStep, step);
        
        if (goLeft) {
            // We are going left. So the next step will expect to go right.
            dfs(node.left, false, step + 1);
            // If we decide to go right instead, we break the zigzag and start a new one.
            dfs(node.right, true, 1);
        } else {
            // We are going right. So the next step will expect to go left.
            dfs(node.right, true, step + 1);
            // If we decide to go left instead, we break the zigzag and start a new one.
            dfs(node.left, false, 1);
        }
    }
}
