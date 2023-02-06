/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shuffle(int* nums, int numsSize, int n, int* returnSize){
    int* final = (int*)malloc(sizeof(int) * numsSize);
    int i = 0;
    int m = 0;
    while(m < n){
        final[i++] = nums[m];
        final[i++] = nums[m + n];
        m ++;
    }
    *returnSize = numsSize;
    return final;
}