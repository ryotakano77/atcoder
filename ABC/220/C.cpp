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
    int N, X;
    vi A;
    cin >> N;
    int tmp_in;
    REP(i, N) {
        cin >> tmp_in;
        A.push_back(tmp_in);
    }
    //cin >> A[i];
    cin >> X;
    X++;
    //int A_sum = accumulate(A.begin(), A.end(), 0);
    vi A_sum_partial;
    int tmp = 0;
    REP(i, N) {
        tmp += A[i];
        A_sum_partial.push_back(tmp);
    }
    int A_sum = A_sum_partial[N-1];
    int div = X / A_sum;
    div *= N;
    int mod = X % A_sum;
    int delta = Lower_bound(A_sum_partial, mod) + 1;
    //cout << delta << endl;
    if (mod != 0) div += delta;
    cout << div << endl;
}