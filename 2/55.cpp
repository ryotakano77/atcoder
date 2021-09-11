#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, Q;
    long long P;
    cin >> N >> P >> Q;
    vector<long long> data(N);
    for (int i = 0; i < N; i++) {
        cin >> data[i];
    }

    long long mul;
    int ans=0;

    for (int i = 0; i < N-4; i++) {
        for (int j = i+1; j<N-3; j++) {
            for (int k = j+1; k<N-2; k++) {
                for (int l = k+1; l<N-1; l++) {
                    for (int m=l+1; m<N; m++) {
                        mul = data[i] * data[j] % P * data[k] % P * data[l]% P * data[m] % P;
                        if (mul == Q) {
                            ans ++;
                        }
                    }
                }
            }
        }
    }
    cout << ans << endl;
}