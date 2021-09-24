#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define int long long
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define pb push_back
#define ALL(obj) (obj).begin(), (obj).end()
//template <class T = int> in()(T x; cin >> x; return (x);)
//template <class T> print(T& x) (cout << x << endl;)
//using template <class T> vec = vector<T>;
const int INF = 100100100;
const int MOD = (int)1e9 + 7;
const double EPS = 1e-9;

signed main() {
    int N, M, T;
    cin >> N >> M >> T;
    vector<int> vec;
    int temp;
    int ans = 0;

    vec.push_back((ll)0);
    REP(i, N) {
        cin >> temp;
        vec.push_back(temp);
    }
    vec.push_back(T);

    int time_pre, time_post;
    REP(i, N+1) {
        time_pre = vec[i];
        time_post = vec[i+1];
        ans += max((ll)0, time_post - time_pre - M);
    }
    cout << ans << endl;
}