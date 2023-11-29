class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int length = s.length();
        int hash_t[128] = {0};
        int max = 0;
        for (int left=0, right=0; right<length; right++){
            left = (hash_t[s[right]] >= left)?hash_t[s[right]]:left;
            max = (max >= right - left + 1)?max:right - left + 1;
            hash_t[s[right]] = right + 1;
        }
        return max;
    }
};
