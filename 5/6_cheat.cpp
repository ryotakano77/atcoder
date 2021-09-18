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
const int INF = 100100100;
const int MOD = (int)1e9 + 7;
const double EPS = 1e-9;
const string ALPHABET = "abcdefghijklmnopqrstuvwxyz";

signed main() {
    int N, K;
    string S;
    cin >> N >> K >> S;

    int char_idx;
    vvi table(N, vector<int>(26, INF));
    for (int i = N - 1; i >= 0; i--) {
        char_idx = S[i] - 'a';
        table[i][char_idx] = i;
        if (i > 0) {
            REP(j, 26) table[i-1][j] = table[i][j];
        }
    }

    string ans;
    int idx_max;
    int idx_now = 0;
    int closest_idx;
    REP(i, K) {
        // 残りK-i文字あるので，右にK-i文字あるのが最大
        // ex) N = 5, K = 3, i = 1のとき
        // 残り２文字だから採用できるのは４文字目まで即ちindex3まで
        // idx_max = N - (K - i) = N - K + i
        idx_max = N - K + i;
        REP(j, 26) {
            closest_idx = table[idx_now][j];
            if (closest_idx <= idx_max) {
                ans += ALPHABET[j];
                idx_now = closest_idx + 1;
                break;
            }
        }
    }
    cout << ans << endl;
}