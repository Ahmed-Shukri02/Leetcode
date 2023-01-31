public class Solution {
    private int length;
    private Dictionary<(int, int), int> mem;
    public int BestTeamScore(int[] scores, int[] ages) {
        length = scores.Length;
        if(length == 1){ return scores[0]; }
        List<(int, int)> arr = new List<(int, int)>();
        for(int i = 0; i < scores.Length; i++){
            arr.Add((ages[i], scores[i]));
        }
        arr.Sort((x, y) => {
            int result = x.Item1.CompareTo(y.Item1);
            return result == 0 ? x.Item2.CompareTo(y.Item2) : result;
        });
        mem = new Dictionary<(int, int), int>();
        return this.dfs(0, int.MinValue, arr);
    }

    int dfs(int i, int min_num, List<(int, int)> arr){
        if(i >= length){ return 0; }
        (int, int) key = (i, min_num);
        if (mem.ContainsKey(key)){
            return mem[key];
        }
        else if (i > 0 && arr[i].Item2 < min_num){
            return this.dfs(i + 1, min_num, arr);
        }

        int inc = arr[i].Item2 + this.dfs(i + 1, Math.Max(min_num, arr[i].Item2), arr);
        int ex = this.dfs(i + 1, min_num, arr);
        mem[key] = Math.Max(inc, ex);

        return mem[key];
    }
}