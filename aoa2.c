#include <stdio.h>
int binarySearch(int arr[], int left, int right, int key) {
 while (left <= right) {
 int mid = left + (right - left) / 2;
 if (arr[mid] == key)
 return mid;
 if (arr[mid] < key)
 left = mid + 1;
 else
 right = mid - 1;
 }
 return -1; 
}
void selectionSort(int arr[], int n) {
 int i, j, min_idx, temp;
 for (i = 0; i < n - 1; i++) {
 min_idx = i;
 // Find the minimum element in the unsorted part
 for (j = i + 1; j < n; j++) {
 if (arr[j] < arr[min_idx]) {
 min_idx = j;
 }
 }
 temp = arr[min_idx];
 arr[min_idx] = arr[i];
 arr[i] = temp;
 }
}
void printArray(int arr[], int n) {
 for (int i = 0; i < n; i++) {
 printf("%d ", arr[i]);
 }
 printf("\n");
}
int main() {
 int n, key, result;
 printf("Enter the number of elements: ");
 scanf("%d", &n);
 int arr[n];
 printf("Enter %d elements: ", n);
 for (int i = 0; i < n; i++) {
 scanf("%d", &arr[i]);
 }
 selectionSort(arr, n);
 printf("Sorted array: \n");
 printArray(arr, n);
 printf("Enter the element to search: ");
 scanf("%d", &key);
result = binarySearch(arr, 0, n - 1, key);
 if (result != -1)
 printf("Element found at index %d\n", result);
 else
 printf("Element not found\n");
 return 0;
}

