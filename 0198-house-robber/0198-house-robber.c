int rob(int* nums, int numsSize){
    int withCurr = nums[numsSize-1], woutCurr = 0;
    for(int i=numsSize-2; i>=0; i--){
        int w = nums[i] + woutCurr;
        int wout = withCurr > woutCurr ? withCurr : woutCurr;
        
        withCurr = w;
        woutCurr = wout;
    }
    
    return withCurr > woutCurr ? withCurr : woutCurr;
}