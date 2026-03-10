#include <stdio.h>
#include <stdlib.h>
// Structure to represent an edge
struct Edge {
 int src, dest, weight;
};
// Structure to represent a graph
struct Graph {
 int V, E;
 struct Edge* edges;
};
// Structure to represent a subset for Union-Find
struct Subset {
 int parent, rank;
};
struct Graph* createGraph(int V, int E) {
 struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
 graph->V = V;
 graph->E = E;
 graph->edges = (struct Edge*)malloc(E * sizeof(struct Edge));
 return graph;
}
int find(struct Subset subsets[], int i) {
 if (subsets[i].parent != i)
 subsets[i].parent = find(subsets, subsets[i].parent);
 return subsets[i].parent;
}
void unionSets(struct Subset subsets[], int x, int y) {
 int rootX = find(subsets, x);
 int rootY = find(subsets, y);
 if (subsets[rootX].rank < subsets[rootY].rank)
 subsets[rootX].parent = rootY;
 else if (subsets[rootX].rank > subsets[rootY].rank)
 subsets[rootY].parent = rootX;
 else {
 subsets[rootY].parent = rootX;
 subsets[rootX].rank++;
 }
}
int compareEdges(const void* a, const void* b) {
 return ((struct Edge*)a)->weight - ((struct Edge*)b)->weight;
}
void kruskalMST(struct Graph* graph) {
 int V = graph->V;
 struct Edge result[V];
 int e = 0, i = 0;
 qsort(graph->edges, graph->E, sizeof(graph->edges[0]), compareEdges);
 struct Subset* subsets = (struct Subset*)malloc(V * sizeof(struct Subset));
 for (int v = 0; v < V; v++) {
 subsets[v].parent = v;
 subsets[v].rank = 0;
 }
while (e < V - 1 && i < graph->E) {
 struct Edge nextEdge = graph->edges[i++];
 int x = find(subsets, nextEdge.src);
 int y = find(subsets, nextEdge.dest);
 if (x != y) {
 result[e++] = nextEdge;
 unionSets(subsets, x, y);
 }
 }
 printf("Minimum Spanning Tree (Kruskal's Algorithm):\n");
 for (i = 0; i < e; i++) {
 printf("%d -- %d == %d\n", result[i].src, result[i].dest, result[i].weight);
 }
 free(subsets);
}
int main() {
 int V, E;
 printf("Enter number of vertices and edges: ");
 scanf("%d %d", &V, &E);
 struct Graph* graph = createGraph(V, E);
 printf("Enter the edges (source, destination, weight):\n");
 for (int i = 0; i < E; i++) {
 scanf("%d %d %d", &graph->edges[i].src, &graph->edges[i].dest, &graph->edges[i].weight);
 }
 kruskalMST(graph);
 free(graph->edges);
 free(graph);
 return 0;
}
