bool canJump(int* nums, int numsSize){
    int *mem = (int*)malloc(sizeof(int)*numsSize);
    for(int i=0; i < numsSize; i++){
        mem[i] = 0;
    }
    mem[numsSize - 1] = 1;

    for(int i = numsSize - 2; i >= 0 ; i--){
        int limit = numsSize - 1 > i + nums[i] ? i + nums[i] : numsSize - 1; // limit is basically max one can jump clamped to the final elem
        for(int j = i + 1; j <= limit; j++){
            if(mem[j] == 1){ mem[i] = 1; break;}
        }
    }

    bool ans = mem[0] == 1;
    free(mem);
    return ans;
}