class Solution {
public:
    int majorityElement(vector<int>& nums) {
         int el;
         int cnt=0;
         int n= nums.size();
        for(int i=0;i<n;i++){
           if(cnt<=0){
            el=nums[i];
            cnt=1;
           }
           else if(el==nums[i]){
                cnt++;
            }
            else{
                cnt--;
            }
        }
        if(cnt>0) {
            return el;
        }
        return -1;
        
    }
};