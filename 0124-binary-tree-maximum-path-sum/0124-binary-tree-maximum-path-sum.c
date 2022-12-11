/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxSum;

int dfs(struct TreeNode* node){
    if(node->left == NULL && node->right == NULL){
        maxSum = maxSum > node->val? maxSum: node->val;
        return node->val > 0? node->val : 0;
    }
    int left = 0, right = 0;
    if(node->left){
        left = dfs(node->left);
        left = left > 0? left: 0;
    }
    if(node->right){
        right = dfs(node->right);
        right = right > 0? right: 0;
    }
    maxSum = maxSum > node->val + left + right ? maxSum : node->val + left + right;
    return left > right? left + node->val: right + node->val;
}

int maxPathSum(struct TreeNode* root){
    maxSum = -INFINITY;
    dfs(root);
    return maxSum;
}


