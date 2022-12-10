/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    long final, total;

    long treeTotal(struct TreeNode* node){
        //printf("%d, %p, %p\n", node->val, node->left, node->right);
        if(node->left == NULL && node->right == NULL){
            return node->val;
        }

        //printf("%d", node->val);
        int ans = node->val;
        if(node->left){ans += treeTotal(node->left);}
        if(node->right){ans += treeTotal(node->right);}

        return ans;
    }

    long dfs(struct TreeNode* node){
        if(node->left == NULL && node->right == NULL){
            return node->val;
        }

        long ans = node->val;
        if(node->left){
            int left = dfs(node->left);
            final = final > ((total - left) * left) ? final : ((total - left) * left);
            ans += left;
        }
        if(node->right){
            int right = dfs(node->right);
            final = final > ((total - right) * right) ? final : ((total - right) * right);
            ans += right;
        }

        return ans;
    }

    public: long maxProduct(struct TreeNode* root){
        // find total
        total = treeTotal(root);
        dfs(root);
        return final % (long)(pow(10, 9) + 7);
    }
};