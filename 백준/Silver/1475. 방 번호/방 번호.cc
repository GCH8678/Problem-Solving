#include <bits/stdc++.h>
using namespace std;

int main(void){
    int n;
    cin >> n;
    int d[9] = {};
    while(n>0){
        if (n%10 == 9){
            d[6]++;
        }else{
            d[n%10]++;
        }
        n/=10;
    }
    d[6]=d[6]/2+d[6]%2;
    int m=0;
    for(int i: d){
        if(m<i){
            m = i;
        }
    }
    cout<<m;

}
