#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	if( argc != 2) {
		printf("Usage: 48 <number to raise to powers or something>\n");
		exit(0);
	}
	int n = atoi(argv[1]);
	long long psum, sum = 0;
	int i, j;
	for (i = 1; i <= n; i++) {
		psum = 1;
		for (j = 1; j <= i; j++) {
			psum *= i;
			psum %= 10000000000;
		}
		sum += psum;
		sum %= 10000000000;
	}
	printf("Sum from 1^1 to %d^%d: %lld\n", n, n, sum);
	exit(0);
}
