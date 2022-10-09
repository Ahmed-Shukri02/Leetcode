public class Solution {
    public int CountOdds(int low, int high) {
        
        int j = 0;
        for (int i = low; i <= high; i++){
            if(i % 2 != 0){
                j ++;
            }
        }
        
        return j;
    }
}