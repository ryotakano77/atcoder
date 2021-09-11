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