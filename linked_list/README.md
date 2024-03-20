## Linked List Cycle
- https://leetcode.com/problems/linked-list-cycle/description/
- easy

slowとfastの2つのポインタを使用する。

最初：slowはhead、fastはheadの1つ先を指して、slowは1つずつ、fastは2つずつ進む。

もしslowとfastが同じものを指せば循環がある。逆に、循環がない場合はfast or fast.nextがnullとなる

## Linked List Cycle Ⅱ
- medium
最初：slowとfastは同じ位置

サイクルが始まる位置Aまでの距離x、Aからslowとfastが出会う位置Bまでの距離をy、BからAまでの距離をzとすると、

2(x+y) = x + 2y + xで、x=zとなる

よって、出会ったらheadとslowを1つずつ動かして中点を取ればよい
