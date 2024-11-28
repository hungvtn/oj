#include <bits/stdc++.h> 
using namespace std;

int main() {
    freopen("bal.inp", "r", stdin);
    freopen("bal.out", "w", stdout);

    int n, x[100001], y[100001];
    cin >> n;
    map<int, int> cnt;
    for (int i = 1; i <= n; i++) {
        cin >> x[i] >> y[i];
        cnt[x[i]]++;
    }
    for (int i = 1; i <= n; i++) {
        int a = (n - 1) + cnt[y[i]];
        int b = (n - 1) - cnt[y[i]];
        cout << a << " " << b << "\n";
    }
    return 0;
}
