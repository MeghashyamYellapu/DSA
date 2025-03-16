class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
       set <int> st;
       vector<int> arr;
       for(int i=0;i<nums.size();i++){
        st.insert(nums[i]);
       }
       int in=0;
      for(auto it:st){
        nums[in]=it;
        in++;
       }
       return in; 
    }
};