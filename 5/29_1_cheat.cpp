#include <bits/stdc++.h>
using namespace std;
#define ll long long
//#define int long long
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
using Graph = vector<vector<int>>;
//const int INF = 1LL << 60;
const int MOD = (int)1e9 + 7;
const double EPS = 1e-9;

signed main() {
    int W, N;
    cin >> W >> N;
    vi field(W, 0);
    vi ans;
    int L, R;
    int height;
    REP(i, N) {
        cin >> L >> R;
        L--;
        R--;
        height = 0;
        height = *max_element(field.begin()+L, field.begin()+R+1);
        for (int j = L; j <= R; j++) field[j] = height + 1;
        ans.push_back(height + 1);
    }
    for (auto &e: ans) cout << e << endl;
}