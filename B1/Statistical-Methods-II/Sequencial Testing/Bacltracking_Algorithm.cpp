#include <bits/stdc++.h>
using namespace std;


map<vector<int>, double> memMap;
double gain(int x, int y, int C, int V, int N) {
    vector<int> key {x,y,C,N};
    if (memMap.find(key) != memMap.end())
        return memMap[key];

    if (x >= C || y > N - C)
        return memMap[key] = 0;

    double p = static_cast<double>(C - x) / (N - x - y);
    double g = p * (V - 1 + gain(x + 1, y, C, V, N)) 
                + (1 - p) * (gain(x, y + 1, C, V, N) - 1);
    return memMap[key] = max(g, 0.0);
}

int main(){
    cout << gain(0,0,5,5,20);
}

int main() {
    int k=1;
    for (int c = 1; c <= 1000; ++c) {
        int n = k;
        double G = 4 * n;
        while (G > 0) {
            ++n;
            G = gain(0, 0, c, 5, n);
        }
        k = n;
        cout << "[" << c << "," << n - 1 << "]" << endl;
    }
}