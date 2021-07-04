// https://leetcode.com/problems/complement-of-base-10-integer

class Solution {
public:
    int bitwiseComplement(int N) {
        int c = 1;
        while (c < N) c = (c << 1) + 1;
        
        return c ^ N;
    }
};