class Solution {
public:
    //  stones= a
    bool stoneGameIX(vector<int>& a) {
        array<int,3> c{};
        for(int x:a) c[x%3]++;
        if(c[0]%2==0) return c[1]&&c[2];
        return abs(c[1]-c[2])>2;
        // auto f=[&](int x ,int y){
        //     if(!c[x]) return false;
        //     c[x]--;
        //     int z=min(c[x],c[y]);
        //     return c[x]!=c[y]&&((c[0]&1)||z);
        // };

        // if(c[0]&1) return min(c[1],c[2])>0 && abs(c[1]-c[2])>2;
        // return c[1]>0 && c[2]>0;
        // return f(1,2)|| f(2,1);
    }
};