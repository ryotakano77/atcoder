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
#define Erase(vec) (vec).erase(unique((vec).begin(), (vec).end()), (vec).end())
//template <class T = int> in()(T x; cin >> x; return (x);)
//template <class T> print(T& x) (cout << x << endl;)
//using template <class T> vec = vector<T>;
using Graph = vector<vector<int>>;
const int INF = 1LL << 60;
const int MOD = (int)1e9 + 7;
const double EPS = 1e-9;

signed main() {
    int W, N;
    cin >> W >> N;
    vi L(N), R(N);
    REP(i, N) {
        cin >> L[i] >> R[i];
        L[i]--;
    }
    vi compression;
    REP(i, N)  {
        compression.push_back(L[i]);
        compression.push_back(R[i]);
    }
    sort(ALL(compression));
    Erase(compression);
    REP(i, N) {
        L[i] = Lower_bound(compression, L[i]);
        R[i] = Lower_bound(compression, R[i]);
    }
    vi h(compression.size());
    int height;
    REP(i, N) {
        height = *max_element(h.begin()+L[i], h.begin()+R[i]) + 1;
        fill(h.begin()+L[i], h.begin()+R[i], height);
        cout << height << endl;
    }
}