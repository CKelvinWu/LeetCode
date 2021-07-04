// https://leetcode.com/problems/valid-parentheses



bool isValid(char * s){
    int len = strlen(s);
    if (len%2) return false;
    if (len==0) return true;
    
    int limit = len/2, id = 0;
    char* stack[limit];
    
    for(int i = 0; i<len; ++i){
        char curr = s[i];
        if(curr == '(' || curr == '[' || curr == '{'){
            if(id == limit) return false;
            stack[id++] = curr;
        }
        
        // there's no (id-1) while id is 0
        else if(id == 0){
            return false;
        }
        
        // neighbors are pairs      
        else if(curr == ')' && stack[id-1] == '(' || curr == ']' && stack[id-1] == '[' || curr == '}' && stack[id-1] == '{' ){
            id--;
        }
        else{
            return false;
        }
    }
    return id == 0;
    
    
}