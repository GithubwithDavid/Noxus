#include<iostream>

int find_max(int arr[], int n){
    int max_val = arr[0];
    for(int i = 1; i < n; i++){
        if (arr[i] > max_val){
            max_val = arr[i];
        }
    } 
    return max_val;
}
int main(){
    int arr[] = {50, 40, 30, 20, 10};
    int n = sizeof(arr) / sizeof(arr[0]);
    int max_val = find_max(arr, n);
    std::cout << "The Max Value is " << max_val;
    return 0;
}