class Solution {
public:
    int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
        int ans=0;
        for(int x: arr1){
            bool flag=1;
            for(int y: arr2) if(abs(x-y)<=d) flag=0;
            ans+=flag;
        }
        return ans;
        
    }
};