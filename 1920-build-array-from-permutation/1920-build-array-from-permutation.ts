function buildArray(nums: number[]): number[] {
    let ans = [];
    
    for(let i: number = 0;i < nums.length; i++){
        ans[i] = nums[nums[i]];
    }
    return ans;
};