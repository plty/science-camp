## Almost Union Find

+++
@snap[north-west title]
## almostunionfind
@snapend

## Kenapa Susah?
### @css[fragment](Karena node bisa punya anak)

+++
@snap[north-west title]
## almostunionfind
@snapend

### Gimana cara forcenya ?
@img[fragment](problems/almostunionfind/img/diagram.png)

+++?code=problems/almostunionfind/solution/almostunionfind.cpp&lang=cpp

@[38-43](Initialization)
@[11-13](Regular implementation of `find_set`)
@[15-22](Modify `join` to mitigate `group_sum`)
@[24-33](Create `move` function)
@[45-62](bada bing, bada boom)

