int ROWS, COLS;
int **mat;

int minFallingPathSum(int** matrix, int matrixSize, int* matrixColSize){
    ROWS = matrixSize;
    COLS = *matrixColSize;
    mat = matrix;
    
    int **mem = (int**)malloc(sizeof(int) * 2 * matrixSize);
    for(int i=0; i < matrixSize; i++){
        int *ptr = (int*)malloc(sizeof(int) * *matrixColSize);
        mem[i] = ptr;
    }
    
    for(int i=0; i<ROWS; i++){
        for(int j=0; j<COLS; j++){
            mem[i][j] = INFINITY;
        }
    }
    
    int final = INFINITY;
    for(int j=0; j < COLS; j++){
        int ans = dfs(0, j, mem);
        final = ans < final ? ans : final;
    }
    
    return final;
}

int dfs(int i, int j, int** mem){
    if(j < 0 || j >= COLS){ return INFINITY; }
    else if (i >= ROWS) { return 0; }
    
    if(mem[i][j] == 2147483647){
        int l, r, c;
        l = dfs(i + 1, j - 1, mem);
        r = dfs(i + 1, j + 1, mem);
        c = dfs(i + 1, j, mem);
        
        // get max from l, r and c
        int m = l;
        m = r < m ? r : m;
        m = c < m ? c : m;
        
        mem[i][j] = mat[i][j] + m;
    }
    
    return mem[i][j];
}