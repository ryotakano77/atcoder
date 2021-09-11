#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
    long long N;
    string S;
    cin >> N >> S;
    vector<int> data;
    char c_now = S[0];
    char c_next;
    int serial = 1;
    for (int i = 1; i < S.size(); i++) {
        c_next = S[i];
        if (c_now == c_next) {
            serial ++;
        }
        else {
            data.push_back(serial);
            serial = 1;
            c_now = c_next;
        }
    }
    data.push_back(serial);

    long long minus = 0;
    for (ll e : data) {
        minus += e * (e + 1) / 2;
    }
    long long all = N * (N + 1) / 2;
    cout << all - minus << endl;
}