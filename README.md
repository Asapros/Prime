# Prime
The most compact prime number finder I can write.

Its total length is 77 bytes!

The one interesting thing that is happening there, is that python is not highlighting `for` keyword because its connected to `0` from last expression.
I didn't expect that, but it works anyway!

# How it works

- First, the `n` variable is initalized at the value of 2.
- Then, there's an infinite loop (python converts value after `while` to `bool`, so i used `1`, which is an int representation of `True`)
  - `n` is multiplied by 2, first it was bitwise shifting by 2 positions, but it was adding `1` more character.
  - Then value of `m` is set to `n-1`. I don't have a clue what's this method called, many prime numbers are just one lower than powers of `2`.
  - `for` loop, iterables from `2` to `m`, and saves in a list `True` if modulo of `m` and the number is zero.
  - Now, we want to check if there are any `True`s in the list. That would say that it's not the prime number.
  - So, `any` checks it. First I used `~` symbol, but it wasn't working for some reason...
  - If there aren't any `True`s in the list, it means that the number is prime. It's just printed.
