int length;
int** mem;
char* s;

int dfs(int i, char prev){
    if(i >= length){
        return 0;
    }
    int bit = s[i] - '0';
    int prevBit = prev - '0';

    int flip = INT_MAX;
    int cont = INT_MAX;

    if(mem[i][prevBit] == -1){
        if(prevBit == 0){
            // choose to continue or flip
            cont = dfs(i + 1, s[i]);
            flip = 1 + dfs(i + 1, bit == 1 ? '0' : '1');
        }
        else if(bit == 0){
            // prev is 1 and this is 0, force flip
            flip = 1 + dfs(i + 1, '1');
        }
        else{
            // prev is 1 and this is 1, force continue
            cont = dfs(i + 1, s[i]);
        }
        mem[i][prevBit] = flip > cont ? cont : flip;
    }
    return mem[i][prevBit];

}

int minFlipsMonoIncr(char * string){
    s = string;
    length = strlen(s);
    mem = (int**)malloc(8 * length); // 8 bytes per pointer
    for(int i = 0; i < length; i++){
        int* p = (int*)malloc(sizeof(int) * 2); // 0 and 1 bit
        p[0] = -1; p[1] = -1;
        mem[i] = p;
    }

    int ans = dfs(0, '0');

    for(int i = 0; i < length; i++){
        free(mem[i]);
    }
    free(mem);

    return ans;
}

