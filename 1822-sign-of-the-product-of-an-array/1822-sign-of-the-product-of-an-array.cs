public class Solution {
    public int ArraySign(int[] nums) {
        int length = nums.Length;
        long minus = 0;
        
        for(int i=0; i < length; i++){
            if(nums[i] == 0){
                return 0;
            }
            
            else if(nums[i] < 0){
                minus ++;
            }
            
        }
        
        return minus % 2 == 0 ? 1 : -1;
        
    }
}