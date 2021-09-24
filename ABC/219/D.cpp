#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define int long long
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define pb push_back
#define ALL(obj) (obj).begin(), (obj).end()
#define vi vector<int>
#define vvi vector<vector<int>>
#define Lower_bound(vec, n) distance((vec).begin(), lower_bound((vec).begin(), (vec).end(), (n)))
#define Upper_bound(vec, n) distance((vec).begin(), upper_bound((vec).begin(), (vec).end(), (n)))
//template <class T = int> in()(T x; cin >> x; return (x);)
//template <class T> print(T& x) (cout << x << endl;)
//using template <class T> vec = vector<T>;
#define dual_sort(obj, n) sort((obj).begin(),(obj).end(),[](const vector<int> &alpha,const vector<int> &beta){return alpha[n] < beta[n];})
const int INF = 1LL << 60;
const int MOD = (int)1e9 + 7;
const double EPS = 1e-9;

signed main() {
    int N, X, Y;
    cin >> N >> X >> Y;
    int A, B, S;
    vvi ABS = {};
    REP(i, N) {
        cin >> A >> B;
        A = min(X, A);
        B = min(Y, B);
        S = - A - B;
        ABS.push_back({S, A, B});
    }
    dual_sort(ABS, 0);
    int ans = 0;
    vector<int> best;
    vvi ABS_next;
    vi n_abs;
    while (true) {
        best = ABS[0];
        X = max(0LL, X - best[1]);
        Y = max(0LL, Y - best[2]);
        ans ++;
        if (X == 0LL && Y == 0LL) break;
        if (ans == N) break;
        ABS_next = {};
        REP(i, N-ans) {
            n_abs = ABS[i+1];
            A = n_abs[1];
            B = n_abs[2];
            A = min(X, A);
            B = min(Y, B);
            S = - A - B;
            ABS_next.push_back({S, A, B});
        }
        ABS = ABS_next;
        dual_sort(ABS, 0);
    }
    if (X == 0 and Y == 0) cout << ans << endl;
    else cout << -1 << endl;
}