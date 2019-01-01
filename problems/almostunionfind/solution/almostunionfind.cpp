// @author plty

#include<bits/stdc++.h>
using namespace std;
#define N 100500
#define TWON 201000
typedef long long ll;

ll p[TWON], group_size[TWON], group_sum[TWON];

int find_set(int x) {
    return p[x] = p[x] == x ? x : find_set(p[x]);
}

void join(int x, int y) {
    int a = find_set(x), b = find_set(y);
    if (a == b) return;
    p[b] = a;

    group_size[a] += group_size[b];
    group_sum[a] += group_sum[b];
}

void move(int x, int y) {
    int a = find_set(x), b = find_set(y);
    p[x] = b;

    group_size[a]--;
    group_size[b]++;

    group_sum[a] -= x;
    group_sum[b] += x;
}

int main() {
    int n, k; 
    while (~scanf("%d%d", &n, &k)) {
        for (int i = 0; i < n + 1; i++) {
            p[i] = N + i;
            p[N + i] = N + i;
            group_size[N + i] = 1;
            group_sum[N + i] = i;
        }

        while (k--) {
            int cmd; scanf("%d", &cmd);
            if (cmd == 1) {
                int p, q; scanf("%d%d", &p, &q);
                join(p, q);
            }

            if (cmd == 2) {
                int p, q; scanf("%d%d", &p, &q);
                move(p, q);
            }

            if (cmd == 3) {
                int p; scanf("%d", &p);
                p = find_set(p);
                printf("%lld %lld\n", group_size[p], group_sum[p]);
            }
        }
    }
}
