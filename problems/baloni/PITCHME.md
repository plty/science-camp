## Baloni

+++
@snap[north-west title]
## baloni
@snapend

## Gasusah kan
### @css[fragment](Tapi mungkin kebetulan)
### @css[fragment](lw cupu.)

+++?code=problems/baloni/solution/baloni.py

@[5](Kita maintain berapa banyak arrow at a given height)
@[8-9](Kalo misalnya gada arrow yang bisa mletusin, kita bikin arrow)
@[10-11](Kalo ada arrow standby, kita suruh mletusin)
@[13](Yang tingginya di `height - 1` obviously naik `1`)
@[14](Yay!)
