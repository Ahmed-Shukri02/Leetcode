public class Solution {
    public bool CanMakeArithmeticProgression(int[] arr) {
        Array.Sort(arr);
        int first = arr[0] - arr[1];
        for(int i = 0; i < arr.Length - 1; i++){
            if (arr[i] - arr[i+1] != first) {return false;} 
        }
        
        return true;
    }
}