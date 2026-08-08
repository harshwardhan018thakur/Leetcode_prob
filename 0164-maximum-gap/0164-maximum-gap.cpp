class Solution {
public:
    int maximumGap(vector<int>& nums) {
        int n = nums.size();
        //--- if you are required to find max gap bet all element
        // int mini = nums[0];
        // int ans = -1;
        // for(int i = 1;i<n;i++){
        //     //if any element is less than mini 
        //     if(nums[i] < mini){
        //         mini = nums[i];
        //     }
        //     else{
        //         ans = max(ans,nums[i]-mini);
        //     }
        // }
        // return ans;
        if (nums.size() < 2)
            return 0;

        sort(nums.begin(), nums.end());

        int ans = 0;

        for (int i = 1; i < nums.size(); i++) {
            ans = max(ans, nums[i] - nums[i - 1]);
        }

        return ans;
    }
};