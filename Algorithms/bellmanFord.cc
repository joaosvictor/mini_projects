// bellman ford algorithm
// https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm

#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= n; i++) distance[i] = INF;
    distance[x] = 0;
    for (int i = 1; i <= n-1; i++){
       	for (auto e:edges){
       		int a, b, w,
       		tie(a,b,w) = e;
       		distance[b] = min(distance[b], distance[a]+w); 
		
    		}
       	}
};
