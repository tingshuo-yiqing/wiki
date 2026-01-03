// hdu模板
#include<bits/stdc++.h>
using namespace std;

using i64 = long long;
using u32 = unsigned;
using u64 = unsigned long long;

int main() {
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    i64 a, b;
    cin >> a >> b;
    
    if (a == 0 || b == 0) {
        cout << 0 << '\n';
        return 0;
    }

    i64 inf = 1000000000000000000LL;

    // i64 ans = a / __gcd(a, b) * b;  // 不能直接算出来

    if (b / __gcd(a, b) > inf / a)
        cout << "Large" << '\n';
    else
        cout << a / __gcd(a, b) * b << '\n';

    return 0;
}