public class Solution {
    public int NearestValidPoint(int x, int y, int[][] points) {
        int min = int.MaxValue;
        int final = -1;
        int length = points.Length;
        
        for(int i=0; i < length; i++){
            if(points[i][0] == x || points[i][1] == y) { 
                if(Math.Abs(points[i][0] - x) + Math.Abs(points[i][1] - y) < min){
                    min = Math.Abs(points[i][0] - x) + Math.Abs(points[i][1] - y);
                    final = i;
                }
            }    
        }
        
        return final;
    }
}