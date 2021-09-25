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



int func(int n, vi dp) {
    string s = to_string(n);
    int digit = s.size();
    int ret = 0;
    int tmp = 1;
    if (digit == 1) return 1;
    else if (s[0] != '1') {
        REP(i, digit + 1) ret += dp[i];
        return ret;
    }
    else if (s[1] == '0') {
        REP(i, digit) ret += dp[i];
        REP(i, digit - 1) tmp *= 10;
        ret += n - tmp + 1;
        return ret;
    }
    /*else if (s[1] == '1') {
        REP(i, digit) ret += dp[1];
        REP
    }
    */
    else {
        REP(i, digit) ret += dp[i];
        REP(i, digit-1) tmp *= 10;
        ret += n - tmp + 1;
        ret += func(stoll(s.substr(1)), dp);
        REP(i, digit-1) ret -= dp[i];
        return ret;
        //return ret + dp[digit-1];
        //return ret + func(stoll(s.substr(1)), dp);
    }
}

signed main() {
    int N;
    cin >> N;
    //桁数
    //string s = to_string(N);
    //int digit = s.size();

    vi dp(17, 0);
    // 1桁では1の1つ
    dp[1] = 1;
    // 2桁は11
    dp[2] = 11;
    // 3桁以上は計算
    int tmp;
    for (int i = 3; i < 17; i++) {
        dp[i] += i;
        for (int j = i - 1; j >= 1; j--) {
            tmp = 1;
            tmp *=  j * 9;
            REP(k, i-j-1) tmp *= 10;
            dp[i] += tmp;
        }
    }
    cout << func(N, dp) << endl;

    
}

