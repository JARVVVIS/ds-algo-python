// 2.2 using hashing to solve in O(n)

#include<bits/stdc++.h> 
using namespace std; 
// This function prints all distinct elements 
void printDistinct(int arr[],int n) 
{ 
    // Creates an empty hashset 
    unordered_set<int> s; 
    // Traverse the input array 
    for (int i=0; i<n; i++) 
    { 
        // If not present, then put it in 
        // hashtable and print it 
        if (s.find(arr[i])==s.end()) 
        { 
            s.insert(arr[i]); 
            cout << arr[i] << " "; 
        } 
    } 
} 
int main () 
{ 
    int arr[] = {10, 5, 3, 4, 3, 5, 6}; 
    int n=7; 
    printDistinct(arr,n); 
    return 0; 
} 