#include<iostream>
using namespace std;
int main(){
    int n, sum;
    cout << "Enter No. of Elements: ";
    cin >> n;
    int* arr = new int[n];
    for(int i = 0; i < n; i++){
        cout << "Enter Number " << i+1 << ": "; 
        cin >> arr[i];
    }
    sum = 0;
    for(int i = 0; i < n; i++){
        sum = sum + arr[i];
    }
    cout << "Sum: " << sum << "\n";
    cout << "Average: " << sum / n;
    delete[] arr;
    return 0;
}
