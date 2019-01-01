// @author plty
#include<bits/stdc++.h>
using namespace std;

map<string, int> cnt;
int main() {
    int n; scanf("%d", &n);
    while (n--) {
        char qry[64]; scanf("%s", qry);
        printf("%d\n", cnt[qry]);
        int len = strlen(qry);
        while (qry[len] = '\0', len--)
            cnt[qry]++;
    }
}
