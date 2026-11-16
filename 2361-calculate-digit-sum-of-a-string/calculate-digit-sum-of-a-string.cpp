class Solution {
public:
    string digitSum(string s, int k) {
        while(s.size()>k){
            string temp="";
            int sum=0, cnt=0;
            for(char c:s){
                sum+=c-'0';
                if(++cnt==k){
                    temp+=to_string(sum);
                    sum=cnt=0;
                }
            }
            if(cnt) temp+=to_string(sum);
            s=temp;
        }
        return s;
        
    }
};