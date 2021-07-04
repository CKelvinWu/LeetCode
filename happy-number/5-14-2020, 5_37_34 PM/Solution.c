// https://leetcode.com/problems/happy-number


int next_n(int n){
    int ans = 0;
    while (n != 0){
        int res = n % 10;
        ans += res * res;    
        n /= 10;
    }
    return ans;
}
bool isHappy(int n){    
    int fast = n;
    int slow = n;
    
    do{
        slow = next_n(slow);
        fast = next_n(next_n(fast));
    } while(fast != slow);
    
    return fast == 1;
}