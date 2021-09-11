#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int N, S;
    cin >> N >> S;
    vector<int> apple(N), pinapple(N);
    for (int i=0; i < N; i++) {
        cin >> apple[i];
    }
    for (int i=0; i < N; i++) {
        cin >> pinapple[i];
    }

    int ans = 0;
    for (int a=0; a < N; a++) {
        for (int p = 0; p < N; p++) {
            if (apple[a] + pinapple[p] == S) {
                ans++;
            }
        }
    }
    cout << ans << endl;
}