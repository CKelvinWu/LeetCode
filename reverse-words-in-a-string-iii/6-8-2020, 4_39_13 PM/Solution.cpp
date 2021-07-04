// https://leetcode.com/problems/reverse-words-in-a-string-iii

class Solution {
public:
    string reverseWords(string s) {
        for (int i = 0; i < s.length(); i++) {
            if (s[i] != ' '){
                int j = i;
                for (; j < s.length() && s[j] != ' '; j++) {};
                reverse(s.begin() + i, s.begin() + j);
                i = j;
            }
            
        }
        return s;
    }
};