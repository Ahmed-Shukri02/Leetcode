/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */


void dfs(struct TreeNode* node, int* arr, int* returnSize){
    arr[(*returnSize)++] = node->val; // increment counter after writing to final
    if(node->left != NULL){
        dfs(node->left, arr, returnSize);
    }
    if(node->right != NULL){
        dfs(node->right, arr, returnSize);
    }
}   

int* preorderTraversal(struct TreeNode* root, int* returnSize){
    int* final = (int*)malloc(100 * sizeof(int));
    *returnSize = 0;
    if(root == NULL){
        return final;
    }
    dfs(root, final, returnSize);
    for(int i = 0; i < *returnSize; i ++){
        printf("%d, ", final[i]);
    }
    return final;
}   