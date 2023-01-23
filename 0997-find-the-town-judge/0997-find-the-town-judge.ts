function findJudge(n: number, trust: number[][]): number {
    let trusting: Map<number, number> = new Map();
    let trusted: Map<number, number> = new Map();

    trust.forEach(([s, d]: number[]):void => {
        let trusting_arr: number = trusting.get(s) ? trusting.get(s) + 1: 1
        let trusted_arr: number = trusted.get(d) ? trusted.get(d) + 1 : 1

        trusting.set(s, trusting_arr)
        trusted.set(d, trusted_arr)
    })

    for(let i:number = 1; i <= n; i++){
        if(!trusting.get(i) && (trusted.get(i) | 0) == n - 1){
            return i
        }
    }
    return -1
};