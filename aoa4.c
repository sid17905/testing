#include <stdio.h>
#include <string.h>
// Function to simulate a match between two players
void match(char *winner, char *player1, char *player2) {
 printf("Match: %s vs %s\n", player1, player2);
 printf("Winner: %s\n", winner);
}
void tennisTournament(char players[][50], int left, int right, char *winner) {
 if (left == right) {
 strcpy(winner, players[left]);
 return;
 }
 int mid = left + (right - left) / 2;
 char winner1[50], winner2[50];
 tennisTournament(players, left, mid, winner1);
 tennisTournament(players, mid + 1, right, winner2);
 strcpy(winner, winner1);
 match(winner, winner1, winner2);
}
int main() {
 int n;
 printf("Enter the number of players: ");
 scanf("%d", &n);
 char players[n][50];
 printf("Enter the names of %d players:\n", n);
 for (int i = 0; i < n; i++) {
 scanf("%s", players[i]);
 }
 char tournamentWinner[50];
 tennisTournament(players, 0, n - 1, tournamentWinner);
 printf("\nTournament Winner: %s\n", tournamentWinner);
 return 0;
}
