#include<bits/stdc++.h>
using namespace std;

// n : 수여 크기
// lst : 수열 크기
// x : 합이 x 같을 때

int main(void){
    int n; // 수열의 크기
    cin >> n;

    vector<int> v;

    for (int i=0;i<n;i++){
        int a;
        cin >> a;
        v.push_back(a);
    }
    int x;
    cin >> x;

    sort(v.begin(),v.end());


    int l= 0;
    int r= v.size()-1;
    int count = 0;
    while(l<r){
        if ((v[l]+v[r])==x){
            count++;
            l++;
            r--;
        }else if((v[l]+v[r])>x){
            r--;
        }else{
            l++;
        }
    }
    cout <<count;

    // 조건을 만족하는 쌍의 갯수



}