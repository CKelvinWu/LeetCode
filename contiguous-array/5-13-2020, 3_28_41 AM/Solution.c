// https://leetcode.com/problems/contiguous-array

// adjust diff index
int diffindex(int i){
    return i + 1;
}


int findMaxLength(int* nums, int numsSize){
   
    int maxLength = 0;
    
    int diff[diffindex(numsSize + 1)];    
    diff[diffindex(-1)] = 0;
    for(int i = 0; i < numsSize; i++){
        if(nums[i] == 0){
            diff[diffindex(i)] = diff[diffindex(i-1)] + 1;
        }
        else{
            diff[diffindex(i)] = diff[diffindex(i-1)] - 1;
        }
    }
    
    
    // range -numsSize ~ numsSize
    int findMaxJSize = 2 * numsSize + 1;
    int findMaxJ[findMaxJSize];
    for (int j = 0; j < findMaxJSize; j++){
        findMaxJ[j] = -1;
    }
    for (int j = 0; j < numsSize; j++){
        findMaxJ[diff[diffindex(j)]+ numsSize] = j;
    }
    
//  start i ~ j
    for (int i = 0; i < numsSize; i++){
        int target = diff[diffindex(i-1)];
        int length = findMaxJ[target+numsSize] - i + 1;
        if (length > maxLength){
            maxLength = length;
        }
    }
    return maxLength;
}