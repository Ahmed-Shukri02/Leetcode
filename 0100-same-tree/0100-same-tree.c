/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int pSize, qSize;
const int null = -100000; // - 10^5
bool isSameTree(struct TreeNode* p, struct TreeNode* q){
    // O(max(p, q)) time, O(p + q) space
    if(p == NULL && q == NULL){
        return true;
    }
    
    pSize = 0;
    qSize = 0;
    int* pArr = (int*)malloc(sizeof(int) * 500);
    int* qArr = (int*)malloc(sizeof(int) * 500);

    preorder(p, pArr, &pSize);
    preorder(q, qArr, &qSize);

    if(pSize != qSize){
        free(pArr);
        free(qArr);
        return false;
    }

    for(int i = 0; i < pSize; i++){
        if (pArr[i] != qArr[i]){
            free(pArr);
            free(qArr);
            return false;
        }
    }

    free(pArr);
    free(qArr);
    return true;
}


void preorder(struct TreeNode* node, int* arr, int* curr){
    if(node == NULL){
        return;
    }
    arr[(*curr)++] = node->val;
    if(node->left != NULL){
        preorder(node->left, arr, curr);
    } else{ arr[(*curr)++] = null; }
    if(node->right != NULL){
        preorder(node->right, arr, curr);
    } else{ arr[(*curr)++] = null; }
}