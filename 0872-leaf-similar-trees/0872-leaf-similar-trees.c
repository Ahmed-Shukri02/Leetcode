/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int *arrP;

bool leafSimilar(struct TreeNode* root1, struct TreeNode* root2){
    int *lvs1 = (int*)malloc(200*sizeof(int));
    int *lvs2 = (int*)malloc(200*sizeof(int));
    
    arrP = lvs1;
    for(int i=0; i<200; i++){
        arrP[i] = 0;
    }
    arrP = lvs1;
    dfs(root1, &arrP);
    
    arrP = lvs2;
    for(int i=0; i<200; i++){
        arrP[i] = 0;
    }
    arrP = lvs2;
    dfs(root2, &arrP);
    
    for(int i=0; i<200; i++){
        if (lvs1[i] != lvs2[i]){
            return false;
        }
    }
    
    return true;
    
}

void dfs(struct TreeNode* nodeP, int** arr){
    if(nodeP->left == NULL && nodeP->right == NULL){
        **arr = nodeP->val;
        ++*arr;
        return;
    }
    
    if(nodeP->left != NULL){
        dfs(nodeP->left, arr);
    }
    if(nodeP->right != NULL){
        dfs(nodeP->right, arr);
    }
}