#include<bits/stdc++.h>
using namespace std;

int main() {
    int n; scanf("%d", &n);
    vector<int> coins(n);
    for (int i = 0; i < n; i++)
        scanf("%d", c[i]);

    int max_value = *max_element(c.begin(), c.end());

    int opt[max_value * 2];
    memset(opt, 63, sizeof opt); 
    opt[0] = 0;

    for (int coin: coins)
        for (int i = 0; i < max_value * 2; i++)
            opt[i] = min(opt[i], opt[i - coin] + 1]);

    // Ini males, infe yet correct
    int cid = 0;
    for (int i = 0; i < max_value * 2; i++) {
        if (i == coin[cid])
            cid++;
        greedy[i] = greedy[i - coin] + 1;
    }
}
