// https://leetcode.com/problems/reverse-integer



int reverse(int x){
    long long ans = 0;
    
    while(x != 0){
        int pop = x % 10;
        x /= 10;
        ans = ans*10 + pop;
        
    }
    if (ans > INT_MAX || ans < INT_MIN) return 0;
    
    return ans;
   
}