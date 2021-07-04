// https://leetcode.com/problems/longest-continuous-increasing-subsequence

class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        if (nums.size() == 1) return 1;
        int count = 1, max_count = 0;
        
        for (int i = 1; i<nums.size(); i++){
            if (nums[i-1] < nums[i]){
                count++;
            }
            else{
                count = 1;
            }
            max_count = max(count, max_count);
            
        }
        return max_count;
        
    }
};