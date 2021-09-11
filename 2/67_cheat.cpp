#include <bits/stdc++.h>
using namespace std;

long long stringN_to_10(int base, string s) {
    long long base10=0, x=1, m = s.size();
    for (int i = 0; i < m; i++) {
        base10 += 1LL * (s[m-i-1] - '0') * x;
        x *= base;
    }
    return base10;
}

long long base10_to_N(int base, long long original) {
    string baseN = "";
    while (original > 0) {
        baseN = to_string(original % base) + baseN;
        original /= base;
    }
    return stoll(baseN);
}

string base10_to_N_now(int base, long long original) {
    string baseN = "";
    string new_num;
    while (original > 0) {
        new_num = to_string(original % base);
        if (new_num == "8") {
            new_num = "5";
        }
        baseN = new_num + baseN;
        original /= base;
    }
    return baseN;
}

int main() {
    string N;
    int K;
    cin >> N >> K;

    if (N == "0") {
        cout << 0 << endl;
    }

    else {
        long long base10 = 0;
        for (int i = 0; i < K; i++) {
            base10 = stringN_to_10(8, N);
            N = base10_to_N_now(9, base10);
        }
        cout << N << endl;
    }
}