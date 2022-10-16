public class Solution {
    public bool IsHappy(int n) {
        HashSet<int> hmap = new HashSet<int>();
        int num = n;
        while(true){
            int[] intArr = num.ToString().Select(digit => int.Parse(digit.ToString())).ToArray();
            int sum = 0;
            for(int i=0; i < intArr.Length; i ++){
                sum += (int)Math.Pow(intArr[i], 2);
            }
            
            if (sum == 1){ return true; }
            else if (hmap.Contains(sum)) { return false; }
            else{
                hmap.Add(sum);
                num = sum;
                continue;
            }
        }
        
    }
}