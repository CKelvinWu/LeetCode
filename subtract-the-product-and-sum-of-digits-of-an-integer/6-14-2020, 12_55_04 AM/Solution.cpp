// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer

class Solution {
public:
    int subtractProductAndSum(int n) {
        int mult = 1;
        int sum = 0;
        
        while(n >= 1) {
            int res = n % 10;
            mult *= res;
            sum += res;
            n /= 10;
        }
        return mult - sum;
    }
};