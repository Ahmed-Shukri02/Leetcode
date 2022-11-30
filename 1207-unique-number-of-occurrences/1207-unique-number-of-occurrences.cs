public class Solution {
    public bool UniqueOccurrences(int[] arr) {
        Dictionary<int, int> hmap = new Dictionary<int, int>();
        HashSet<int> hset = new HashSet<int>();
        
        for(int i=0;i < arr.Length;i++){
            if(hmap.ContainsKey(arr[i])){
                hmap[arr[i]] = hmap[arr[i]] + 1;
            }
            else{
                hmap.Add(arr[i], 1);
            }
        }
        
        foreach(var pair in hmap){
            if(hset.Contains(pair.Value)){
                return false;
            }
            hset.Add(pair.Value);
        }
        
        return true;
    }
}