function twoSum(nums: number[], target: number): number[] {
    const hmap: Map<number, number | undefined> = new Map();
    for(let i:number = 0; i < nums.length; i++){
        let remainder: number = target - nums[i];
        if (hmap.get(remainder) != undefined){
            return [i, hmap.get(remainder)];
        }
        hmap.set(nums[i], i);
    }
};