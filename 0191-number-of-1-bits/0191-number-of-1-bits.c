int hammingWeight(uint32_t n) {
    int final = 0;
    for(int i=0; i<32; i++){
        if(n>>i & 1 == 1){
            final++;
        }
    }
    return final;
}