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

struct Edge {
    ll to;
    ll cost;
};
using Graph = vector<vector<Edge>>;
using P = pair<long, int>;
/* dijkstra(G, s, dis)
    入力：グラフG，開始点s，距離を格納するdis，最短経路の前の点を記録するprev
    計算量：O(|E|log|V|)
    副作用：dis，prevが書き換えられる
*/
void dijkstra(const Graph &G, int s, vector<ll> &dis, vector<int> &prev) {
    int N = G.size();
    dis.resize(N, INF);
    prev.resize(N, -1);
    priority_queue<P, vector<P>, greater<P>> pq;
    dis[s] = 0;
    pq.emplace(dis[s], s);
    while (!pq.empty()) {
        P p = pq.top();
        pq.pop();
        int v = p.second;
        if (dis[v] < p.first) continue;
        for (auto &e : G[v]) {
            if (dis[e.to] > dis[v] + e.cost) {
                dis[e.to] = dis[v] + e.cost;
                prev[e.to] = v;
                pq.emplace(dis[e.to], e.to);
            }
        }
    }
}

vector<int> get_path(const vector<int> &prev, int t) {
    vector<int> path;
    for (int cur = t; cur != -1; cur = prev[cur]) {
        path.push_back(cur);
    }
    reverse(ALL(path));
    return path;
}

signed main() {
    int N, M;
    cin >> N >> M;
    int a, b, c;
    Edge e;
    Graph g(N);
    REP(i, M) {
        cin >> a >> b >> c;
        a--;
        b--;
        e = {a, c};
        g[b].push_back(e);
        e = {b, c};
        g[a].push_back(e);
    }
    
    vi dist, prev;
    dijkstra(g, 0, dist, prev);
    vi dist0 = dist;
    //cout << "1 to n" << endl;
    //REP(i, N) cout << dist0[i] << endl;
    REP(i, N) dist[i] = INF;
    dijkstra(g, N-1, dist, prev);
    vi distn = dist;
    //cout << "n to 1" << endl;
    //REP(i, N) cout << distn[i] << endl;
    //cout << "ans" << endl;
    REP(i, N) {
        cout << dist0[i] + distn[i] << endl;
    }
    
}