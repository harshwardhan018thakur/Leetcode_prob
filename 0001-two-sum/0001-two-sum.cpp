class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // int n = nums.size();
        // int i = 0,j = n-1;
        // //sort(nums.begin(),nums.end());
        // while(i < j){
        //     int sum = nums[i]+nums[j];
        //     if(sum == target) return{i,j};
        //     else if(sum > target) j--;
        //     else i++;
        // }
        // return {};

          unordered_map<int, int> mp;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            if (mp.find(complement) != mp.end()) {
                return {mp[complement], i};
            }

            mp[nums[i]] = i;
        }

        return {};
    }
};