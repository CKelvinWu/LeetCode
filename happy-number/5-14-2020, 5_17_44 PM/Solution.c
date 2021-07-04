// https://leetcode.com/problems/happy-number



bool isHappy(int n){
    
    
    int ans = 0;
    bool isSingle = false;
    
    //  sum of the squares of its digits
    while (n != 0){
        isSingle = true;
        int res = n % 10;
        ans += res * res;    
        n /= 10;
    }
    if (ans == 1 || ans == 7){
        return true;
    }
    else if (ans < 10){
        return false;
    } 
    else{
        return isHappy(ans);
    }
}