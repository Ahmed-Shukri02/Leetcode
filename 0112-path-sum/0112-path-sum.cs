/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    private List<int> ans = new List<int>();
    
    public bool HasPathSum(TreeNode root, int targetSum) {
        if(root == null) { return false; }
        
        this.dfs(root, 0);
        
        foreach(int sum in ans){
            if(sum == targetSum) { return true; }
        }
        return false;
    }
    private void dfs(TreeNode node, int sum){
        sum += node.val;
        
        if(node.left == null && node.right == null){ // leaf node
            ans.Add(sum);
            return;
        }
        
        if(node.left != null){ this.dfs(node.left, sum); }
        if(node.right != null){ this.dfs(node.right, sum); }
        
        sum -= node.val;
        return;
    }
}