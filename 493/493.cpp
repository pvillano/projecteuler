#include <stdio>

struct state {
    unsigned short* numBalls;
    unsigned short tot;
    }

double expected(state previous){
	for(int i = 0; i < 7; i++){
		if(previous.state[i] > 7){
			return 0;
