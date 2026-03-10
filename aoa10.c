#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define N 4 // 15-Puzzle is a 4x4 grid
int puzzle[N][N];state
void printPuzzle() {
 for (int i = 0; i < N; i++) {
 for (int j = 0; j < N; j++) {
 if (puzzle[i][j] == 0)
 printf(" ");
 else
 printf("%2d ", puzzle[i][j]);
 }
 printf("\n");
 }
 printf("\n");
}
void findEmptyTile(int *x, int *y) {
 for (int i = 0; i < N; i++) {
 for (int j = 0; j < N; j++) {
 if (puzzle[i][j] == 0) {
 *x = i;
 *y = j;
 return;
 }
 }
 }
}
void swap(int *a, int *b) {
 int temp = *a;
 *a = *b;
 *b = temp;
}
bool moveTile(char move) {
 int x, y;
 findEmptyTile(&x, &y);
 switch (move) {
 case 'w': // Up
 if (x > 0) {
 swap(&puzzle[x][y], &puzzle[x - 1][y]);
 return true;
 }
 break;
 case 's': // Down
 if (x < N - 1) {
 swap(&puzzle[x][y], &puzzle[x + 1][y]);
 return true;
 }
 break;
 case 'a': // Le
if (y > 0) {
 swap(&puzzle[x][y], &puzzle[x][y - 1]);
 return true;
 }
 break;
 case 'd': // Right
 if (y < N - 1) {
 swap(&puzzle[x][y], &puzzle[x][y + 1]);
 return true;
 }
 break;
 }
 return false;
}
bool isSolved() {
 int expected = 1;
 for (int i = 0; i < N; i++) {
 for (int j = 0; j < N; j++) {
 if (i == N - 1 && j == N - 1) {
 return puzzle[i][j] == 0; // Last tile must be empty
 }
 if (puzzle[i][j] != expected++) {
 return false;
 }
 }
 }
 return true;
}
int main() {
 printf("Enter the 15-puzzle configuration (4x4 grid, use 0 for empty tile):\n");
 for (int i = 0; i < N; i++) {
 for (int j = 0; j < N; j++) {
 scanf("%d", &puzzle[i][j]);
 }
 }
 printf("Initial Puzzle State:\n");
 printPuzzle();
 char move;
 while (!isSolved()) {
 printf("Enter move (w=Up, s=Down, a=Left, d=Right): ");
 scanf(" %c", &move);
 if (moveTile(move)) {
 printPuzzle();
 } else {
 printf("Invalid move! Try again.\n");
 }
 }
 printf("Congratulations! You solved the puzzle!\n");
 return 0;
}