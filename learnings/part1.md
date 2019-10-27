# Learning
## Part 1

Difference between interpreter and compiler:
* Interpreter: if a translator processes and executes the source program without translating it into machine language first
* Compiler: if a translator translates a source program into machine language

Current restrictions:
* Building a calculator which can only add two single-digit integers
* Can't handle whitespace

What's happening:
* When an expression (let's say 4+5) is entered, the interpreter receives "4+5" as a string
* It then gets broken up into "tokens", which is an object made up of a type and value
    * ex: if you get '4', token type is INTEGER and value is 4
* Breaking up string into tokens is called **lexical analysis**
* The part of the interpreter that does this is called the **lexical analyzer**, or lexer
    * Other names are **scanner** or **tokenizer**

* In the code, the method **get_next_token** is the lexical analyzer. It creates a token depending on the input characters
* Interpreter currently expects a specific stream: INTEGER->PLUS->INTEGER
* The method which finds and interprets that structure is **expr**
    * Verifies that the sequence of tokens corresponds to the expected sequence
    * After it verifies, it gets result by adding the two values
* helper method **consume** verifies that the token type passed matches the current token type
    * If stream of tokens doesn't match INTEGER->PLUS->INTEGER, consume throws an exception
    
Additional work:
* Handle whitespace
* Handle multiple-digit integers  
* Handle subtraction
