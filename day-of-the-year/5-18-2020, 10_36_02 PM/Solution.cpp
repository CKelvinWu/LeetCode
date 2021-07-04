// https://leetcode.com/problems/day-of-the-year

class Solution {
public:
    
    int dayOfYear(string date) {
        int days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int year = stoi(date.substr(0, 4)), month = stoi(date.substr(5, 2)), day = stoi(date.substr(8, 2));
    
        if (month > 2 && year%4 == 0 && (year%100 != 0 || year%400 == 0)){
            day++;
        }
        int sum = 0;
        for (int i = 1; i < month; i++){            
            sum += days[i-1];
        }
        sum += day;
        
        return sum;
    }
};