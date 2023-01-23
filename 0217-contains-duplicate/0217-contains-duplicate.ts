function containsDuplicate(nums: number[]): boolean {
    const hset: Set<number> = new Set();
    for(let i:number = 0; i < nums.length; i++){
        if (hset.has(nums[i])){
            return true;
        }
        hset.add(nums[i]);
    }
    return false;
};