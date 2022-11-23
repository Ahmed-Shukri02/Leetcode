public class Solution {
    public bool IsValidSudoku(char[][] board) {
        Dictionary<(int, int), HashSet<int>> quad = new Dictionary<(int, int), HashSet<int>>();
        List<HashSet<int>> row, col;
        
        row = new List<HashSet<int>>();
        col = new List<HashSet<int>>();
        
        for(int i = 0; i < 9; i++){
            row.Add(new HashSet<int>());
            col.Add(new HashSet<int>());
            
            for(int j = 0; j < 9; j ++){
                quad.Add((i, j), new HashSet<int>());
            }
        }
        
        for(int i=0; i < 9; i++){
            for(int j=0; j< 9; j++){
                char num = board[i][j];
                if(num == '.') { continue; }
                (int, int) q = ((int) Math.Floor((double)(i / 3)), (int) Math.Floor((double)(j / 3)));
                if(quad[q].Contains(num) || row[i].Contains(num) || col[j].Contains(num)){
                    return false;
                }
                quad[q].Add(num);
                row[i].Add(num);
                col[j].Add(num);
            }
        }
        
        return true;
        
    }
}