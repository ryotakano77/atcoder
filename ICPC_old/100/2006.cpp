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
    unordered_map<char, string> um;
    um['1'] = ".,!? ";
    um['2'] = "abc";
    um['3'] = "def";
    um['4'] = "ghi";
    um['5'] = "jkl";
    um['6'] = "mno";
    um['7'] = "pqrs";
    um['8'] = "tuv";
    um['9'] = "wxyz";

    string num;
    int N;
    cin >> N;
    REP(i, N) {
        cin >> num;
        int len = num.size();
        char c = num[0];
        int c_count = 0;
        int num_count = 1;
        string ans = "";
        

        while (true) {
            if (num_count == len) {
                //if (c != ' ') ans += um[c][c_count % (um[c].size())];
                break;
            }
            char c_next = num[num_count];
            if (c_next == '0') {
                if (c != '0') ans += um[c][c_count % (um[c].size())];
                c = '0';
                c_count = 0;
            }
            else if (c == '0') {
                c = num[num_count];
                c_count = 0;
            }
            else {
                c_count++;
            }
            num_count++;
        }
        cout << ans << endl;
    }
}
