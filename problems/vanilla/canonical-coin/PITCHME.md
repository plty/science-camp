## Canonical Coin Systems

+++

@snap[north-west title]
## canonical
@snapend

### Problem statement
Given coin system, lw harus determine apakah system coin itu bisa di-greedy.
Coin yang solusi greedy nya sama dengan 
solusi optimalnya disebut juga canonical coin system


+++

@snap[north-west title]
## canonical
@snapend

Contoh coin canonical itu sistem mata uang Indonesia, 
`$\{1, 2, 10, 20, 50, 100\}$`


Contoh coin yang ga canonical misal di sistem `$\{1, 5, 8\}$`
counterexample-nya itu `$10$` dikarenakan 
`$8 + 1 + 1$` lebih buruk dari `$5 + 5$` 

+++?code=problems/vanilla/canonical-coin/canonical.cpp

@[5](Kita maintain berapa banyak arrow at a given height)
@[8-9](Kalo misalnya gada arrow yang bisa mletusin, kita bikin arrow)
@[10-11](Kalo ada arrow standby, kita suruh mletusin)
@[13](Yang tingginya di `height - 1` obviously naik `1`)
@[14](Yay!)

