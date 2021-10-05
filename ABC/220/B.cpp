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

long long stringN_to_10(int base, string s) {
    long long base10=0, x=1, m = s.size();
    for (int i = 0; i < m; i++) {
        base10 += 1LL * (s[m-i-1] - '0') * x;
        x *= base;
    }
    return base10;
}

long long base10_to_N(int base, long long original) {
    string baseN = "";
    while (original > 0) {
        baseN = to_string(original % base) + baseN;
        original /= base;
    }
    return stoll(baseN);
}

signed main() {
    int K;
    string A, B;
    int A_k, B_k;
    cin >> K >> A >> B;
    A_k = stringN_to_10(K, A);
    B_k = stringN_to_10(K, B);
    cout << A_k * B_k << endl;
}