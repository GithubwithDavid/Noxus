#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to multiply a vector (representing a large number) with an integer
vector<int> multiply(vector<int>& num, int multiplier) {
    vector<int> result;
    int carry = 0;
    
    // Multiply each digit
    for (int i = 0; i < num.size(); i++) {
        int product = num[i] * multiplier + carry;
        result.push_back(product % 10);
        carry = product / 10;
    }
    
    // Add remaining carry
    while (carry) {
        result.push_back(carry % 10);
        carry /= 10;
    }
    
    return result;
}

// Function to calculate factorial using vector representation
vector<int> factorial(int n) {
    if (n == 0 || n == 1) {
        return {1};
    }
    
    vector<int> result = {1};
    for (int i = 2; i <= n; i++) {
        result = multiply(result, i);
    }
    
    return result;
}

// Function to print the result
void printFactorial(const vector<int>& result) {
    for (int i = result.size() - 1; i >= 0; i--) {
        cout << result[i];
    }
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    
    if (n < 0) {
        cout << "Error: Cannot calculate factorial of negative number!" << endl;
    } else {
        cout << "The factorial of " << n << " is: ";
        vector<int> fact = factorial(n);
        printFactorial(fact);
        cout << endl;
        cout << "Number of digits: " << fact.size() << endl;
    }
    
    char choice;
    cout << "Do you want to continue (y/n): ";
    cin >> choice;
    if (choice == 'y' || choice == 'Y') {
        main();
    } else {
        cout << "Thanks for using our program";
    }
}