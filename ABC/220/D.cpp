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
    // plus[i][j] := jをiにするために足すもの
    vvi plus = {
        {0, 9, 8, 7, 6, 5, 4, 3, 2, 1},
        {1, 0, 9, 8, 7, 6, 5, 4, 3, 2},
        {2, 1, 0, 9, 8, 7, 6, 5, 4, 3},
        {3, 2, 1, 0, 9, 8, 7, 6, 5, 4},
        {4, 3, 2, 1, 0, 9, 8, 7, 6, 5},
        {5, 4, 3, 2, 1, 0, 9, 8, 7, 6},
        {6, 5, 4, 3, 2, 1, 0, 9, 8, 7},
        {7, 6, 5, 4, 3, 2, 1, 0, 9, 8},
        {8, 7, 6, 5, 4, 3, 2, 1, 0, 9},
        {9, 8, 7, 6, 5, 4, 3, 2, 1, 0}
    };
    // mul[i][j] := jをiにするためにかけるもの
    vector<vector<vector<int>>> mul(10, vector<int>(10));
    int mod;
    REP(i, 10) {
        REP(j, 10) {

        }
    }
    REP(i, 10) {
        REP(j, 10) {
            mod = (i * j) % 10;
            mul[mod][j].push_back(i);
        }
    }
    /*
    REP(i, 10) {
        REP(j, 10) {
            for (auto e: mul[i][j]) {
                cout << "i: " << i << "j " << j << " " << e << endl;
            }
        }
    }
    */
}