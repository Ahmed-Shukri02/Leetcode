int maxSubarraySumCircular(int* nums, int numsSize){
    int curr_max, max_val, curr_min, min_val, sum;
    curr_max = max_val = -40000;
    curr_min = min_val = 40000;
    sum = 0;
    for(int i = 0; i < numsSize; i++){
        curr_max = nums[i] > nums[i] + curr_max ? nums[i] : nums[i] + curr_max;
        curr_min = nums[i] > nums[i] + curr_min ? nums[i] + curr_min : nums[i];
        max_val = max_val > curr_max ? max_val : curr_max;
        min_val = min_val < curr_min ? min_val : curr_min;
        sum += nums[i];
    }
    if(sum == min_val){
        return max_val;
    }
    return max_val > sum - min_val ? max_val : sum - min_val;
}