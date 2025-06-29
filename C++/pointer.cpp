#include<iostream>
using namespace std;

void multiple(int &n){
    n = n * 5;
}
int main(){
    int n;
    cout << "Enter a number: ";
    cin >> n;
    multiple(n);
    cout << n;
}
