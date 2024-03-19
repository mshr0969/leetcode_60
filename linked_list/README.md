## Linked List Cycle
- https://leetcode.com/problems/linked-list-cycle/description/
- easy

slowとfastの2つのポインタを使用する。

最初：slowはhead、fastはheadの1つ先を指して、slowは1つずつ、fastは2つずつ進む。

もしslowとfastが同じものを指せば循環がある。逆に、循環がない場合はfast or fast.nextがnullとなる
