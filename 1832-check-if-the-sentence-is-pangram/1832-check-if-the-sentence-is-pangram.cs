public class Solution {
    public bool CheckIfPangram(string sentence) {
        Dictionary<char, int> hmap = new Dictionary<char, int>();
        string check = "abcdefghijklmnopqrstuvwxyz";
        int sLength = sentence.Length;
        
        for(int i=0;i<sLength;i++){
            if (!hmap.ContainsKey(sentence[i])){
                hmap.Add(sentence[i], 1);
            }
            else hmap[sentence[i]] = hmap[sentence[i]] + 1;
        }
        
        for(int i = 0; i < check.Length; i ++){
            if(!hmap.ContainsKey(check[i])){
                return false;
            }
        }
        
        return true;
    }
}