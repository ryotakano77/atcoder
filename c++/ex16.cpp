#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main(void) {
    vector<int> data(5);
    for (int i = 0; i < 5; i++) {
        cin >> data[i];
    }

    string ans = "NO";
    for (int i = 0; i < 4; i++) {
        if (data[i] == data[i+1]) {
            ans = "YES";
        }
    }
    cout << ans << endl;
    return (0);
}