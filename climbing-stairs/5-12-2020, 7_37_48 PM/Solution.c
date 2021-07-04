// https://leetcode.com/problems/climbing-stairs


int climbStairs(int n){

    if(!n || n == 1) return 1;
    
    int n1, n2, res;
    n1 = n2 = 1;
    for(int i = 2; i <= n; i++){
        res = n1 + n2;
        n1 = n2;
        n2 = res;
    }
    return res;
    
}