// https://leetcode.com/problems/reverse-words-in-a-string-iii

class Solution {
public:
    string reverseWords(string s) {
        string result = "";
        string part = "";
        for (int i = 0; i < s.size(); i++) {
            char c = s[i];
            if (c != ' '){
                part = c + part;
            }
            if (c == ' ') {
                result = result + part + c;
                part = "";
            }
        }
        return result + part;
    }
};