public class Solution {
    Dictionary<int, int> mem = new Dictionary<int, int>();
    int r;

    public int NumSquares(int n) {
        r = (int) Math.Floor(Math.Sqrt(n));
        return this.dfs(n);
    }

    private int dfs(int num){
        if(num == 0){ return 0; }
        else if (num < 0){return int.MaxValue;}

        if(mem.ContainsKey(num)) { return mem[num]; }

        int m = int.MaxValue;
        for(int i=1; i <= r; i++){
            m = Math.Min(m, this.dfs(num - (int) Math.Pow(i, 2)));
        }

        mem.Add(num, 1 + m);
        return 1 + m;
    }
}