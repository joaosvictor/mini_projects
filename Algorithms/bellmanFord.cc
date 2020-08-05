// Yes a exception here, I'm puting here a cc algorithm, why ?? I don't know.

#include <iostream>
using namespace std;

int main() {
	// the implementation: >>>
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
