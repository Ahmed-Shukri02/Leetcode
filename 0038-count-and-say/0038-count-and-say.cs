public class Solution {
    public string CountAndSay(int n) {
        string ans = "1";
        for(int i = 0; i < n - 1; i ++){
            ans = this.helper(ans);
        }
        
        return ans;
        
    }
    
    
    private string helper(string s){
        string final = "";
        
        int counter = 1;
        for(int i = 1; i < s.Length; i ++){
            if(s[i] == s[i-1]){
                counter++;
            }
            else{
                final +=  counter.ToString() + s[i-1].ToString();
                counter = 1;
            }
        }
        
        final += counter.ToString() + s[s.Length - 1].ToString();
        
        return final;
        
    }
}