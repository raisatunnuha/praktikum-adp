#include<bits/stdc++.h>
using namespace std;
int main(){
    array <float,21> nilai_x;
    cout << "|  x  |     f(x)     |"<<endl;
    for (int i=-10; i<=10; i++){
        if (i<0) {
            nilai_x[i+10] = 1.0/i;
        }
        else if (i==0) {
                nilai_x[i+10]=10;
        }
        else {
            nilai_x[i+10]=i*i+2*i;
        }
        printf("|%4d | %12g |\n", i, nilai_x[i+10]);
    }
    return 0;
}
