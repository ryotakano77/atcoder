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
using Graph = vector<vector<int>>;
const int INF = 1LL << 60;
const int MOD = (int)1e9 + 7;
const double EPS = 1e-9;

vector<bool> seen;
vector<int> first_order; // 行きがけ順
vector<int> last_order; // 帰りがけ順
vector<int> first_node; // 行きがけ順にソートしたノード
vector<int> last_node; // 帰りがけ順にソートしたノード
vector<int> groupe; // 連結成分

void dfs(const Graph &G, int v, int& first_ptr, int& last_ptr) {
    groupe.push_back(v);
    // 行きがけ順をインクリメントしながらメモ
    first_node[first_ptr] = v;
    first_order[v] = first_ptr++;
    seen[v] = true;
    for (auto next_v: G[v]) {
        if (seen[next_v]) continue;
        dfs(G, next_v, first_ptr, last_ptr);
    }
    // 帰りがけ順をインクリメントしながらメモ
    last_node[last_ptr] = v;
    last_order[v] = last_ptr++;
}

signed main() {
    int N, M;
    cin >> N >> M;
    Graph graph_forward(N), graph_backward(N);
    int A, B;
    REP(i, M) {
        cin >> A >> B;
        A--;
        B--;
        graph_forward[A].push_back(B);
        graph_backward[B].push_back(A);
    }

    seen.assign(N, false); // 全頂点を「未訪問」に初期化
    first_order.resize(N);
    last_order.resize(N);
    first_node.resize(N);
    last_node.resize(N);
    int first_ptr = 0, last_ptr = 0;

    // 順行グラフでdfs
    REP(i, N) {
        if (seen[i]) continue;
        dfs(graph_forward, i, first_ptr, last_ptr);
    }

    vvi groupes;
    seen.assign(N, false);
    first_ptr = 0;
    last_ptr = 0;
    //逆行グラフでdfs
    vector<int> n = last_node;
    for (int i = N-1; i >= 0; i--) {
        if (seen[n[i]]) continue;
        groupe = {};
        dfs(graph_backward, n[i], first_ptr, last_ptr);
        groupes.push_back(groupe);
    }

    // 数える
    int ans = 0;
    int num_groupe;
    for (auto g: groupes) {
        num_groupe = g.size();
        ans += (num_groupe * (num_groupe - 1)) / 2;
    }
    cout << ans << endl;
}