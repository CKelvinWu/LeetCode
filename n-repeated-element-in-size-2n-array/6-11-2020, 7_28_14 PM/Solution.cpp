// https://leetcode.com/problems/n-repeated-element-in-size-2n-array

class Solution {
public:
    int repeatedNTimes(vector<int>& A) {
        unordered_set<int> seen;
        for (int a : A) {
            if (seen.count(a)) return a;
            seen.insert(a);
        }
        return -1;
    }
};