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
    int N;
    cin >> N;
    vector<string> vec;
    int num_a = 0;
    string s;
    string ans = "";
    REP(i, N) {
        cin >> s;
        if (s == "A") {
            num_a++;
        }
        else {
            if (num_a == 0) {
                ans = "NO";
                break;
            }
            else num_a--;
        }
    }
    if (num_a > 0) ans = "NO";
    if (ans == "NO") cout << ans << endl;
    else cout << "YES" << endl;
}