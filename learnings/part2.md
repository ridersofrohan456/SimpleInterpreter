# Learning
## Part 2

Differences from part 1:
* get_next_token was refactored, and the logic to increment pos pointer was put into method **move_forward**
* skip_whitespace() was added to ignore whitespace chars
* integer() was added to handle multi-digit integer inputs
* expr() method was modified to handle MINUS

Additional concepts:
* A **lexeme** is a char sequence that form a token
    * Example:
        INTEGER: 345, 9, 4, 11
        PLUS: +
        MINUS: -
* **Parsing** is the process of recognizing a phrase (essentially finding meaning/structure) in a stream of tokens
* The part of the interpreter/compiler doing the parsing is called **parser*8

Additional work:
* Handle multiplication of two integers
* Handle division of two integers
* Modify code to interpret expressions containing an arbitrary number of additions and subtractions
