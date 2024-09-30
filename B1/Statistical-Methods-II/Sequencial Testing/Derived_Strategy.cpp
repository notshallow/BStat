#include <bits/stdc++.h>
using namespace std;

int profit(const vector<int>& l) {
    int p = 15 - l[2]; 
    if (20 - l[2] > 15) return p;
    
    p += (5 - l[3] + l[2]);
    if (20 - l[3] > 8) return p;

    p += (5 - l[4] + l[3]);
    return p;
}

int main() {
    vector<vector<int>> L;
    vector<int> P;

    for (int a = 1; a <= 16; ++a) {
        for (int b = a + 1; b <= 17; ++b) {
            for (int c = b + 1; c <= 18; ++c) {
                for (int d = c + 1; d <= 19; ++d) {
                    for (int e = d + 1; e <= 20; ++e) {
                        L.push_back({a, b, c, d, e});
                    }
                }
            }
        }
    }

    int totalProfit = 0;
    for (const auto& i : L) {
        P.push_back(profit(i));
        totalProfit += P.back(); 
    }
    
    cout << static_cast<double>(totalProfit) / P.size() << endl;
}