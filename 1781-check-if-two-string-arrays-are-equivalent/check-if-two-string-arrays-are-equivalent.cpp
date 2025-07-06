class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string result,result2;
           for (const string& word : word1) {
        result += word;  // Concatenate using += operator
    }
         for (const string& word : word2) {
        result2 += word;  // Concatenate using += operator
    }
    if (result==result2){
        return true;
    }
    return false;
    }
};