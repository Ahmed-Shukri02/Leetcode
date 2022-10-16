public class Solution {
    public bool AreAlmostEqual(string s1, string s2) {
        int counter = 0;
        
        Dictionary<char, int> hmap1 = new Dictionary<char, int>();
        Dictionary<char, int> hmap2 = new Dictionary<char, int>();
        
        int length1 = s1.Length;
        int length2 = s2.Length;
        if(length1 != length2) {return false;}
        
        for(int i = 0; i < length1; i++){
            if (s1[i] != s2[i] && counter >= 2) { return false; }
            else if (s1[i] != s2[i]) { counter++; }
            
            if(!hmap1.ContainsKey(s1[i])) {hmap1.Add(s1[i], 1);}
            else hmap1[s1[i]] = hmap1[s1[i]] + 1;
            
            if(!hmap2.ContainsKey(s2[i])) {hmap2.Add(s2[i], 1);}
            else hmap2[s2[i]] = hmap2[s2[i]] + 1;
        }
        
        foreach (char key in hmap1.Keys){
            if (!hmap2.ContainsKey(key) || hmap1[key] != hmap2[key]){
                return false;
            }
        }
        
        return true;
    }
}