int cmp(const void* a, const void* b){
    return(*(int*)a - *(int*)b);
}

int maxIceCream(int* costs, int costsSize, int coins){
    // sort arr
    qsort(costs, costsSize, sizeof(int), cmp);
    int f = 0, i = 0;
    while(i < costsSize && costs[i] <= coins){
        coins = coins - costs[i];
        i++; f++;
    }
    return f;
}