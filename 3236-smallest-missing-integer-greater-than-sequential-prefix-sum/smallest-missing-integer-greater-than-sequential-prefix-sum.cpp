class Solution {
public:
    int missingInteger(vector<int>& nums) {
        int val=nums[0];
        for(int i=1;i<nums.size()&&nums[i]==nums[i-1]+1;i++)
        val+=nums[i];
        unordered_set<int> sto(nums.begin(), nums.end());
        while(sto.count(val))
        val++;
        return val;
        
    }
};