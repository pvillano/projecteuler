#include <stdio.h>
#include "82.h"

int main(int argc, const char *argv[]) {
    int A[N][N];
    int arr1[N];
    int arr2[N];
    int *prev = arr1;
    int *S1 = arr2;
    int *temp;
    int y, x, changed;

    for (y = 0; y < N; y++) {
        for (x = 0; x < N; x++) {
            A[x][y] = At[y][x];
        }
    }
    for (y = 0; y < N; y++) {
        prev[y] = 0;
    }
    for (x = 0; x < N; x++) {
        for (y = 0; y < N; y++) {
            S1[y] = A[x][y] + prev[y];
        }
        changed = 1;
        while (changed) {
            changed = 0;
            for (y = 0; y < N - 1; y++) {
                if (S1[y] + A[x][y + 1] < S1[y + 1]) {
                    S1[y + 1] = S1[y] + A[x][y + 1];
                    changed = 1;
                }
            }
        }
        changed = 1;
        while (changed) {
            changed = 0;
            for (y = N - 1; y > 0; y--){
                if(S1[y] + A[x][y - 1] < S1[y - 1]) {
                    S1[y - 1] = S1[y] + A[x][y - 1];
                    changed = 1;
                }
            }

        }
        temp = S1;
        S1 = prev;
        prev = temp;
        printf("x=%d\n", x);
    }

    int smallest = prev[0];
    for (y = 1; y < N; ++y) {
        smallest = (prev[y] < smallest ? prev[y] : smallest);
    }
    printf("%d", smallest);
}