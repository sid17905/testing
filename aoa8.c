#include <stdio.h>
#include <limits.h>
#define V 10 
int tsp(int graph[V][V], int mask, int pos, int n, int dp[V][1 << V]) {
 if (mask == (1 << n) - 1) {
 return graph[pos][0]; 
 }
 if (dp[pos][mask] != -1) {
 return dp[pos][mask];
 }
 int minCost = INT_MAX;
 for (int city = 0; city < n; city++) {
 if ((mask & (1 << city)) == 0) {
 int newCost = graph[pos][city] + tsp(graph, mask | (1 << city), city, n, dp);
 if (newCost < minCost) {
 minCost = newCost;
 }
 }
 }
 return dp[pos][mask] = minCost;
}
int main() {
 int n;
 int graph[V][V], dp[V][1 << V];
 printf("Enter the number of cities: ");
 scanf("%d", &n);
 printf("Enter the distance matrix (use 0 for same city):\n");
 for (int i = 0; i < n; i++) {
 for (int j = 0; j < n; j++) {
 scanf("%d", &graph[i][j]);
 }
 }
 for (int i = 0; i < V; i++) {
 for (int j = 0; j < (1 << V); j++) {
 dp[i][j] = -1;
 }
 }
 int minCost = tsp(graph, 1, 0, n, dp);
 printf("Minimum cost of Travelling Salesman Problem: %d\n", minCost);
 return 0;
}