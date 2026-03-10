#include <stdio.h>
#include <stdbool.h>
#define N 10 
int board[N][N];
int n; 
void printSolution() {
 for (int i = 0; i < n; i++) {
 for (int j = 0; j < n; j++) {
 printf("%c ", board[i][j] ? 'Q' : '.');
 }
 printf("\n");
 }
 printf("\n");
}
bool isSafe(int row, int col) {
 for (int i = 0; i < col; i++) { // Check left row
 if (board[row][i]) return false;
 }
 for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) { // Check upper diagonal
 if (board[i][j]) return false;
 }
 for (int i = row, j = col; i < n && j >= 0; i++, j--) { // Check lower diagonal
 if (board[i][j]) return false;
 }
 return true;
}
bool solveNQueens(int col) {
 if (col >= n) { // All queens placed successfully
 printSolution();
 return true;
 }

 bool res = false;
 for (int i = 0; i < n; i++) {
 if (isSafe(i, col)) {
 board[i][col] = 1;
 res = solveNQueens(col + 1) || res;
 board[i][col] = 0; // Backtrack
 }
 }
 return res;
}
int main() {
 printf("Enter the number of queens: ");
 scanf("%d", &n);
 if (n < 1 || n > N) {
 printf("Invalid input! Please enter a number between 1 and %d.\n", N);
 return 1;
 }
 for (int i = 0; i < n; i++) {
 for (int j = 0; j < n; j++) {
 board[i][j] = 0;
 }
 }
 if (!solveNQueens(0)) {
 printf("No solution exists for %d queens.\n", n);
 }
 return 0;
}