public class Solution {
    public IList<IList<int>> FindWinners(int[][] matches) {
        HashSet<int> hset = new HashSet<int>();
        Dictionary<int, int> hmap = new Dictionary<int, int>();
        
        for(int i=0; i < matches.Length; i++){
            hset.Add(matches[i][0]);
            hset.Add(matches[i][1]);
            
            if(hmap.ContainsKey(matches[i][1])){
                hmap[matches[i][1]] = hmap[matches[i][1]] + 1;
            }
            else{
                hmap[matches[i][1]] = 1;
            }
        }
        
        List<int> win, one;
        win = new List<int>();
        one = new List<int>();
        foreach(int player in hset){
            if (!hmap.ContainsKey(player)){
                win.Add(player);
            }
            else if (hmap[player] == 1){
                one.Add(player);
            }
        }
        
        win.Sort();
        one.Sort();
        
        return new List<IList<int>>(){win, one};
    }
    
}
