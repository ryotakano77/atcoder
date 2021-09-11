#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> graph(N, 0);
    int a, b;
    for (int i=0; i < M; i++) {
        cin >> a >> b;
        a--;
        b--;
        if (a > b) {
            graph[a]++;
        }
        else {
            graph[b]++;
        }
    }
    int ans = 0;
    for (int i = 0; i < N; i++) {
        if (graph[i] == 1) {
            ans++;
        }
    }
    cout << ans << endl;
}