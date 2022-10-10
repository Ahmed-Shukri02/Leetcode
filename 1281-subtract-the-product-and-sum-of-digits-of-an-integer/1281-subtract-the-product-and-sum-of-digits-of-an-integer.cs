public class Solution {
    public int SubtractProductAndSum(int n) {
        string n_s = n.ToString();
        int p = 1;
        int s = 0;
        for(int i = 0; i < n_s.Length; i ++){
            int num = (int)(n_s[i] - '0');
            p *= num;
            s += num;
        }
        
        return p - s;
    }
    
}