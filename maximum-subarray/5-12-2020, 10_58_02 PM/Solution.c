// https://leetcode.com/problems/maximum-subarray

int max(int n1, int n2){
    if(n1 >= n2){
        return n1;
    }
    else{
        return n2;
    }
}

int maxSubArray(int* nums, int numsSize){
    if(numsSize == 1) return nums[0];
    int localmax, globalmax;
    localmax = globalmax = nums[0];
    for(int i = 1; i < numsSize; i++){
        localmax = max(localmax + nums[i], nums[i]);
        globalmax = max(localmax, globalmax);
    }
    return globalmax;
}

