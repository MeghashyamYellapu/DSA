class Solution {
public:
    int scoreOfString(string s) {
        int sum=0,ans=0;
        for (int i=1;i<s.size();i++){
            sum=s[i-1]-s[i];
            if (0>sum){
                sum= sum*-1;
            }
            ans+=sum;
        }
        return ans;
    }
};