#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int check[1000001];
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	
	int n;
	cin >> n;
	vector<int>ans = vector<int>(n,-1);
	vector<int>ary = vector<int>(n);
	for (int i = 0; i < n; i++) {
		cin >> ary[i];
		check[ary[i]]++;
	}
	stack<int> st;
	for (int i = 0; i < n; i++) {
		if (!st.empty()) {
			while (check[ary[i]] > check[ary[st.top()]]) {
				ans[st.top()] = ary[i];
				st.pop();
				if (st.empty())
					break;
			}
			st.push(i);
		}
		else
			st.push(i);
	}
	for (int k : ans)
		cout << k << ' ';
	cout << '\n';

}
