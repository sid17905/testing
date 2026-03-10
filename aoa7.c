#include <stdio.h>
#include <limits.h>
#include <stdbool.h>
#define V 100 
int minDistance(int dist[], bool sptSet[], int vertices) {
 int min = INT_MAX, minIndex;
 for (int v = 0; v < vertices; v++) {
 if (!sptSet[v] && dist[v] < min) {
 min = dist[v];
 minIndex = v;
 }
 }
 return minIndex;
}
void printSolution(int dist[], int vertices) {
 printf("Vertex \t Distance from Source\n");
 for (int i = 0; i < vertices; i++) {
 printf("%d \t %d\n", i, dist[i]);
 }
}
void dijkstra(int graph[V][V], int source, int vertices) {
 int dist[vertices]; 
 bool sptSet[vertices]; 
 for (int i = 0; i < vertices; i++) {
 dist[i] = INT_MAX;
 sptSet[i] = false;
 }
 dist[source] = 0;
 for (int count = 0; count < vertices - 1; count++) {
 int u = minDistance(dist, sptSet, vertices);
 sptSet[u] = true;
 for (int v = 0; v < vertices; v++) {
 if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v]) {
 dist[v] = dist[u] + graph[u][v];
 }
 }
 }
 printSolution(dist, vertices);
}
int main() {
 int vertices, source;
 printf("Enter the number of vertices: ");
 scanf("%d", &vertices);
 int graph[V][V];
 printf("Enter the adjacency matrix (use 0 for no edge):\n");
 for (int i = 0; i < vertices; i++) {
 for (int j = 0; j < vertices; j++) {
 scanf("%d", &graph[i][j]);
 }
 }

 printf("Enter the source vertex: ");
 scanf("%d", &source);

 printf("Shortest paths from source vertex %d:\n", source);
 dijkstra(graph, source, vertices);

 return 0;
}