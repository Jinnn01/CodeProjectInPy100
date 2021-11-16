# Generate a random password - hard version
- Whole password is random
- Example: 4 letter, 2 symbol, 2 number = g^2jk8&P
## How to do that?
- ### My idea:
    1. get each random symbols : random number, random symbol, random letter
    2. put all the generated random signals into one list. Generate a random list
    3. use `random.choice()` function , randomly get elements from the random list(X)
    above may generate problem, the element can be repeated. 
    - wrong exmaple: %v%v1L%7
- ### My idea version2:
  After get the random element list, using `sample()` function
  `sample(list,num)` num = the wanted size of the list
- ### Solution:
    `shuffle()` function, return a new random list 