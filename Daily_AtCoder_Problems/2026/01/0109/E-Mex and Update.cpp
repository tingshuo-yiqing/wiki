// hdu模板
#include<bits/stdc++.h>
using namespace std;

using i64 = long long;
using u32 = unsigned;
using u64 = unsigned long long;

class Mex {
private:
    map<int, int> freq;
    set<int> missing_number;
    vector<int> A;
public:
    Mex(vector<int> const& A) : A(A) {
        for (int i = 0; i <= A.size(); ++i)
            missing_number.insert(i);
        
        for (int x : A) {
            ++freq[x];
            missing_number.erase(x);
        }
    }

    int mex() {
        return *missing_number.begin();
    }

    //todo 更新idx处的值
    void update(int idx, int new_value) {
        if (--freq[A[idx]] == 0)
            missing_number.insert(A[idx]);
        A[idx] = new_value;
        ++freq[new_value];
        missing_number.erase(new_value);
    }
};

int main() {
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n, q;
    cin >> n >> q;

    vector<int> nums(n);
    for (int i = 0; i < n; ++i) cin >> nums[i];

    Mex M(nums);

    for (int _ = 0; _ < q; ++_) {
        int i, x;
        cin >> i >> x;

        M.update(i - 1, x);
        cout << M.mex() << '\n';
    }
    return 0;
}