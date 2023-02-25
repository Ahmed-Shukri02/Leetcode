int maxProfit(int* prices, int pricesSize){
    int* dp = (int*)malloc(sizeof(int) * pricesSize);
    for(int i=0; i < pricesSize; i++){
        dp[i] = 0;
    }
    int m = prices[pricesSize - 1];
    for(int i=pricesSize - 2; i >= 0; i-- ){
        dp[i] = dp[i + 1] >= m - prices[i] ? dp[i + 1] : m - prices[i];
        m = prices[i] >= m ? prices[i] : m;
    };

    int final = dp[0];
    free(dp);
    return final;
}