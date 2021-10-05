#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define int long long
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define pb push_back
#define ALL(obj) (obj).begin(), (obj).end()
//template <class T = int> in()( T x; cin >> x; return (x);)
//template <class T> print(T& x) (cout << x << endl;)
//using template <class T> vec = vector<T>;
const int INF = 100100100;
const int MOD = (int)1e9 + 7;
const double EPS = 1e-9;

signed main() {
    int N, M, P;
    int intmp;
    while (true) {
        cin >> N >> M >> P;
        if (N == 0) break;

        //vector<int> cards(0);
        int all = 0;
        int hit = 0;

        REP(i, N) {
            cin >> intmp;
            all += intmp * 100;
            if (i+1 == M) hit = intmp;
        }

        float tmp = all * (100 - P) / 100.0;

        int ans;
        if (hit != 0) ans = tmp / hit;
        else ans = 0;

        cout << ans << endl;
    }
}