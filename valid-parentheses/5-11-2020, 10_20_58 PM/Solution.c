// https://leetcode.com/problems/valid-parentheses



bool isValid(char * s){
    int len = strlen(s);
    if (len%2) return false;
    
    int limit = len/2, id = 0;
    char* stack = malloc(limit);
    
    for(int i = 0; i<len; ++i){
        char curr = s[i];
        // printf("%c",curr);
        if(curr == '(' || curr == '[' || curr == '{'){
            printf("1id = %d\n", id);
            if(id == limit) return false;
            stack[id++] = curr;
        }
        else if(id == 0){
            return false;
        }
//      neighbors are pairs
        else if(curr == ')' && stack[id-1] == '(' || curr == ']' && stack[id-1] == '[' || curr == '}' && stack[id-1] == '{' ){
            // printf("2id = %d\n", id);
            id--;
        }
        else{
            // printf("3id = %d\n", id);
            return false;
        }
    }
    free(stack);
    return id == 0;
    
    
}