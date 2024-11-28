#pragma GCC optimize("O3")
#include <bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	freopen("str.inp", "r", stdin);
	freopen("str.out", "w", stdout);
	string s; cin >> s;
	vector<int> cnt(91, 0);
	for (int i = 0; i < s.size(); i++)
		cnt[s[i]]++;
	cout << min({cnt['C'], cnt['O'], cnt['A'], cnt['N'] / 2}) << "\n";
}