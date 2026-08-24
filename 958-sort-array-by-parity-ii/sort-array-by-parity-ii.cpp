class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& nums) {
        int i=0, j=1;
        while(i<nums.size()){
            if(nums[i]%2){
                while(nums[j]%2) j+=2;
                swap(nums[i],nums[j]);
                j+=2;
            }i+=2;
        }
        return nums;
    }
};