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

signed main() {
    int N, Q, tmp;
    vector<int> classes;
    cin >> N;

    REP(i, N) {
        cin >> tmp;
        classes.push_back(tmp);
    }
    cin >> Q;

    sort(ALL(classes));

    int student, idx, ans;
    REP(i, Q) {
        cin >> student;
        idx = Lower_bound(classes, student);
        //idx = distance((classes).begin(), lower_bound((classes).begin(), (classes).end(), (N)));
        
        if (idx == 0) ans = classes[0] - student;
        else if (idx == N) ans = student - classes[N-1];
        else ans = min(student - classes[idx-1], classes[idx] - student);
        cout << ans << endl;
    }
}