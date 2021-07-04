// https://leetcode.com/problems/first-bad-version

// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n) {
    
    if (isBadVersion(1) == true) return 1;
    
    int lf, mid, rg;
    lf = 1;
    rg = n;
    
    
    while(lf < rg){
        mid = lf + (rg - lf) / 2;
        if (isBadVersion(mid) == true){
            rg = mid;
        }
        else{
            lf = mid + 1;
        }        
    }
    return lf;
    
}

