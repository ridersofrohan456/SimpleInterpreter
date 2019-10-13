# Token types
# Following tutorial: https://ruslanspivak.com/lsbasi-part1/
# EOF (end of file) token is used to indicate that there is no more input left for lexical analysis
from builtins import *

INTEGER = 'INTEGER'
PLUS = 'PLUS'
EOF = 'EOF'


class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, or EOF
        self.type = type
        # token value: 0,1,2,3,4,5,6,7,8,9,'+', or None
        self.value = value

    def __str__(self):
        """ String representation of the class instance

            Examples:
                Token(INTEGER, 3)
                Token(PLUS, '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    # why call str w/in repr, and call repr above?
    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3+5"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """Lexical analyzer (aka tokenizer)

        Breaks up input string (sentence) apart into tokens.
        One token at a time

        :return: token
        """
        text = self.text

        # if self.pos is past the end of sentence, return EOF
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # get the char at the self.pos position and decide what token to create based on the given character
        current_char = text[self.pos]

        # If character is a digit, convert to integer token and increment pos
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        # If character is a digit, convert to 'PLUS' token and increment pos
        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token
        self.error()

    def consume(self, token_type):
        # compare current token type with the passed token type and if they match
        # then consume the current token and assign next token to self.current_token
        # otherwise raise err exception
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """expr -> INTEGER PLUS INTEGER """
        # set current token to first token from input
        self.current_token = self.get_next_token()

        # Expect current token to be a single digit integer
        left = self.current_token
        self.consume(INTEGER)

        # Expect current token to be a '+' token
        operation = self.current_token
        self.consume(PLUS)

        # Expect current token to be a single digit integer
        right = self.current_token
        self.consume(INTEGER)


        result = left.value + right.value
        return result


def main():
    while True:
        try:
            text = input('input calc> ')
        except EOFError:
            break

        if not text:
            continue

        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__== '__main__':
    main()
