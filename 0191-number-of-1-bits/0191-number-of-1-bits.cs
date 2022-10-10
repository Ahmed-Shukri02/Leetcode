public class Solution {
    public int HammingWeight(uint n) {
        
        string bstring = Convert.ToString(n, 2);
        int counter = 0;
        for(int i=0; i < bstring.Length; i++){
            if(bstring[i] == char.Parse("1")){
                counter++;
            }
        }
        
        return counter;
    }
}