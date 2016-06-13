#define N 80
#include "82.h"
int A[N][N];
int prev[N]
int S1[N];
int *temp;
int i,j, changed;
for (j = 0; j < N; j++){
	for(i = 0; i < N; i++){
		A[i][j] = At[j][i];
	}
}
for(i = 0; i < N; i++}{
	prev[i] = 0;
}
for (j = 0; j < N; j++){
	for(i = 0; i < N; i++){
		S1[i] = A[j][i] + prev[i];
	}
	changed = 1;
	while(changed){
		changed = 0;
		for(i = 0; i < N - 1; i++){
			if(S1[i] + A[j][i] < S1[i+1]){
				S1[i+1] = S1[i] + A[j][i];
				changed = 1;
			}
			
			/*
			an optimisation from
				if(S1[i+1] + A[j][i+1] < S1[i]){
					S1[i] = S1[i+1] + A[j][i+1];
				}
			that reduces the number of times this loop runs by up to N
			by allowing better values to propogate upwards within a run of the for loop
			*/
			if(S1[N-1-i] + A[j][N-1-i] < S1[N-2-i]){
				S1[N-2-i] = S1[N-1-i] + A[j][N-1-i];
				changed = 1;
			}
		}
	}
	temp = S1;
	S1 = prev;
	prev = temp;
}
	