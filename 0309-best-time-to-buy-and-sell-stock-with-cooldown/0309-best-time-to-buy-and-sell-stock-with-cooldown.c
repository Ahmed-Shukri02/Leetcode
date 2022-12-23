
int** mem;
int None;
int length;
int* p;

int maxProfit(int* prices, int pricesSize){
    None = pricesSize; // index for holding "None"
    length = pricesSize;
    p = prices;
    
    // INITIALIZE DP TABLE MEMORY
    mem = (int**)malloc(length * sizeof(int) * 2); // * 2 since pointer takes up 8 bytes (compared to 4 for int)
    for(int i = 0; i < length; i++){
        int* p = (int*)malloc((length + 1) * sizeof(int)); // (size + 1) since we want to include None in holdings
        for(int j = 0; j <= length; j++){
            p[j] = -2147483648; // INT_MIN
        }
        mem[i] = p;
    }
    
    
    int ans = dfs(0, None);
    
    // FREE DP TABLE
    for(int i = 0; i < length; i ++){
        free(mem[i]);
    }
    free(mem);
    
    
    return ans;
    
}


int dfs(int i, int hold_i){
    if(i >= length){
        return 0;
    }
    
    if(mem[i][hold_i] == -2147483648){
        int buy = 0, sell = 0, hold = dfs(i + 1, hold_i);
        if(hold_i == None){ // not holding anything
            buy = dfs(i + 1, i);
        }
        else{
            sell = p[i] - p[hold_i] + dfs(i + 2, None);
        }
        
        // find max between 0 and buying, selling or holding
        int m = 0;
        m = m > buy ? m : buy;
        m = m > sell ? m : sell;
        m = m > hold ? m : hold;
        
        mem[i][hold_i] = m;
    }
    
    return mem[i][hold_i];
}