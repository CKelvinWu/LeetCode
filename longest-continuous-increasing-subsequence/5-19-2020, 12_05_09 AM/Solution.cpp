// https://leetcode.com/problems/longest-continuous-increasing-subsequence

class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        
        int count = 0, max_count = 0;        
        for (int i = 0; i < nums.size(); i++){
            if (i == 0 || nums[i-1] < nums[i]){                
                max_count = max(max_count, ++count);
            }
            else{
                count = 1;
            }                   
        }
        return max_count;
        

    }
};