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
const int INF = 1LL << 60;
const int MOD = (int)1e9 + 7;
const double EPS = 1e-9;
const string alphabets = "abcdefghijklmnopqrstuvwxyz";

signed main() {
    string x;
    int n;
    cin >> x >> n;
    map<char, char> new_alphabet;
    REP(i, 26) new_alphabet[x[i]] = alphabets[i];
    vector<string> strs;
    string tmp;
    REP(i, n) {
        cin >> tmp;
        strs.push_back(tmp);
    }
    map<string, string> names;
    string name;
    vector<string> names_old;
    string name_old;
    REP(i, n) {
        name = strs[i];
        name_old = "";
        REP(j, name.length()) {
            name_old += new_alphabet[name[j]];
        }
        names_old.push_back(name_old);
        names[name_old] = name;
    }
    sort(ALL(names_old));
    REP(i, n) cout << names[names_old[i]] << endl;
}