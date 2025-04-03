class Solution {
public:
    int longestConsecutive(vector<int>& a) {
         int n= a.size();
    int lastsmallest =INT_MIN;
    int cnt=0;
    int largest =0;

    sort(a.begin(),a.end());
    for(int i=0;i<n;i++){
        if(a[i]-1 ==lastsmallest){
            cnt++;
            lastsmallest =a[i];
        }
        else if(a[i]!=lastsmallest){
            cnt=1;
            lastsmallest=a[i];
        }
        largest=max(cnt,largest);
    }
    return largest;
    }
};