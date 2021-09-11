#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

void recursive_comb(int *indexes, int s, int rest, function<void(int *)> f) {
  if (rest == 0) {
    f(indexes);
  } else {
    if (s < 0) return;
    recursive_comb(indexes, s - 1, rest, f);
    indexes[rest - 1] = s;
    recursive_comb(indexes, s - 1, rest - 1, f);
  }
}

// nCkの組み合わせに対して処理を実行する
void foreach_comb(int n, int k, function<void(int *)> f) {
  int indexes[k];
  recursive_comb(indexes, n - 1, k, f);
}

int main() {
    int N, P, Q;
    cin >> N >> P >> Q;
    vector<int> data(N);
    for (int i; i < N; i++) {
        cin >> data[i];
    }
    int ans = 0;
    foreach_comb(N, 5, [&](int *indexes) {
        ans += (data[indexes[0]]*data[indexes[1]]*data[indexes[2]]*data[indexes[3]*data[indexes[4]]]) % P == Q;
    });
    cout << ans << endl;
}