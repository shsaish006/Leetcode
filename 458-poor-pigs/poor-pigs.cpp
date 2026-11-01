class Solution {
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        assert(buckets>=1 && minutesToDie>0 && minutesToTest>=0);
        int base=minutesToTest/ minutesToDie+1;
        int cnt=0;
        long long val=1;
        while(val<buckets){
            val*=base;
            cnt++;
        }
        return cnt;
        
    }
};