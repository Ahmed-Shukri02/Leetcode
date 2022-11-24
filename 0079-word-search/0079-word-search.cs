public class Solution {
    private int ROWS, COLS, wlength;
    private char[][] board1;
    private string word1;
    private HashSet<(int, int)> path;
    
    private bool oob(int i, int j){
        return (i < 0 || i >= ROWS) || (j < 0 || j >= COLS);
    }
    
    public bool Exist(char[][] board, string word) {
        ROWS = board.Length;
        COLS = board[0].Length;
        wlength = word.Length;
        board1 = board;
        word1 = word;
        path = new HashSet<(int, int)>();
        
        for(int i=0; i <ROWS; i++){
            for(int j=0; j<COLS;j++){
                if(this.dfs(i, j, 0)) { return true; }
            }
        }
        
        return false;
    }
    
    
    private bool dfs(int i, int j, int p){
        if (p >= wlength){ return true; }
        else if (this.oob(i, j) || board1[i][j] != word1[p] || path.Contains((i, j))) { return false; }
        path.Add((i, j));
        
        bool sol = false;
        (int, int)[] dirs = {(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)};
        foreach((int, int) dir in dirs){
            if (this.dfs(dir.Item1, dir.Item2, p + 1)){
                sol = true;
                break;
            }
        }
        
        path.Remove((i, j));
        return sol;
    }
}