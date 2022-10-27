public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> hmap = new Dictionary<int, int>();
        for(int i=0; i < nums.Length; i++){
            if(hmap.ContainsKey(nums[i])){
                return new int[] {i, hmap[nums[i]]};
            }
            else if (hmap.ContainsKey(target - nums[i])){ hmap[target - nums[i]] = i; }
            else hmap.Add(target - nums[i], i);
        }
        
        return null;
    }
}