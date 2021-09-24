#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define int long long
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define pb push_back
#define ALL(obj) (obj).begin(), (obj).end()
#define vi vector<int>
#define vvi vector<vector<int> >
#define Lower_bound(vec, n) distance((vec).begin(), lower_bound((vec).begin(), (vec).end(), (n)))
#define Upper_bound(vec, n) distance((vec).begin(), upper_bound((vec).begin(), (vec).end(), (n)))
//template <class T = int> in()(T x; cin >> x; return (x);)
//template <class T> print(T& x) (cout << x << endl;)
//using template <class T> vec = vector<T>;
const int INF = 1LL << 60;
const int MOD = (int)1e9 + 7;
const double EPS = 1e-9;

signed main() {
    vi ans;
    int N, M;
    int d, v;
    vvi problems(100);
    int ans_i = 0;
    while (true) {
        cin >> N >> M;
        if (N == 0 and M == 0) break;
        REP(i, 100) problems[i] = {};
        ans_i = 0;
        REP(i, N) {
            cin >> d >> v;
            d--;
            problems[d].push_back(v);
        }
        REP(i, M) {
            ans_i += *max_element(ALL(problems[i]));
        }
        ans.push_back(ans_i);
    }
    for (int e : ans) cout << e << endl;
}