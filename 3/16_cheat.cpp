#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define myint int
#define int long long

signed main() {
    ll ans = 10000;
    int N, A, B, C;
    int remain;
    cin >> N >> A >> B >> C;
    for (int i = 0; i < 10000; i++) {
        for (int j = 0; j < 10000 - i; j++) {
            remain = N - (A * i) - (B * j);
            if (remain % C != 0) continue;
            if (remain < 0) continue;
            ans = min(ans, i+j+(remain/C));
        }
    }
    cout << ans << endl;
    return 0;
}