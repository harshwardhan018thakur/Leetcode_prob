class Solution {
public:
    int findMin(vector<int>& nums) {
        int ans = nums[0];
        int n = nums.size();
        for(int i = 1;i<n;i++){
            if(nums[i] < ans){
                ans = nums[i];
            }
        }
        return ans;
    }
};