#pragma GCC optimize("O3")
#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main()
{
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    freopen("rgc.inp", "r", stdin);
    freopen("rgc.out", "w", stdout);
    int n; cin >> n;
    for (int i = (int)sqrt(n); i > 0; i--)
        if (n % (i * i) == 0) {
            cout << i << " " << n / (i * i) << "\n";
            return 0;
        }
}