// https://leetcode.com/problems/move-zeroes



void moveZeroes(int* nums, int numsSize){
    int j = 0;
    for(int i = 0; i < numsSize; i++){
        if(nums[i] != 0){
            nums[j] = nums[i];
            j++;
        }
    }
    for(int i = j; i < numsSize; i++){
        nums[i] = 0;
    }
    return nums;

}