public class Solution {
    public double Average(int[] salary) {
        Array.Sort(salary);
        int sum = 0;
        int length = salary.Length;
        for(int i = 1; i < length - 1; i ++){
            sum += salary[i];
        }
        
        return (double)sum/(length - 2);
    }
}