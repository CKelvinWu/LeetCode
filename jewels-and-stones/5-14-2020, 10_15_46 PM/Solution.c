// https://leetcode.com/problems/jewels-and-stones



int numJewelsInStones(char * J, char * S){

    int JSize = strlen(J);
    int SSize = strlen(S);
    int count = 0;
    for (int i = 0; i < SSize; i++){
        for (int j = 0; j < JSize; j++){
            if (S[i] == J[j]){
                count++;
            }            
            
        }
    }
    return count;
    
}