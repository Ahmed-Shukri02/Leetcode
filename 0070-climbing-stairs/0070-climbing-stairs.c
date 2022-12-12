int climbStairs(int n){
    if(n <= 2){
        return n;
    }
    int prev1 = 1, prev2 = 2;
    int ans = 0;
    for(int i=0; i<n-2; i++){
        ans = prev1 + prev2;
        prev1 = prev2;
        prev2 = ans;
    }
    return prev2;
}