#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main() {
    int Q;
    cin >> Q;
    vector<int> t(Q), x(Q);
    for (int i = 0; i < Q; i++) {
        cin >> t[i] >> x[i];
    }
    deque<int> d;
    for (int i = 0; i < Q; i++) {
        if (t[i] == 1) {
            d.push_front(x[i]);
        }
        else if (t[i] == 2)
        {
            d.push_back(x[i]);
        }
        else if (t[i] == 3) {
            cout << d[x[i] - 1] << endl;
        }
        
    }
}