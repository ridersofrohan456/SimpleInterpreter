# Token types
# Following tutorial: https://ruslanspivak.com/lsbasi-part1/
# EOF (end of file) token is used to indicate that there is no more input left for lexical analysis
from builtins import *

INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
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
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Error parsing input')

    def move_forward(self):
        """Advances the 'pos' pointer and sets the current_char variable"""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_over_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.move_forward()

    def integer(self):
        """Return a (multi-digit) int consumed from input"""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.move_forward()
        return int(result)

    def get_next_token(self):
        """Lexical analyzer (aka tokenizer)

        Breaks up input string (sentence) apart into tokens.
        One token at a time

        :return: token
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_over_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '+':
                self.move_forward()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.move_forward()
                return Token(MINUS, '-')

            self.error()

        return Token(EOF, None)

    def consume(self, token_type):
        # compare current token type with the passed token type and if they match
        # then consume the current token and assign next token to self.current_token
        # otherwise raise err exception
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """ Parser / Interpreter

        expr -> INTEGER PLUS INTEGER
        expr -> INTEGER MINUS INTEGER

        """
        # set current token to first token from input
        self.current_token = self.get_next_token()

        # Expect current token to be an integer
        left = self.current_token
        self.consume(INTEGER)

        # Expect current token to be a '+' OR '-'
        operation = self.current_token
        if operation.type == PLUS:
            self.consume(PLUS)
        else:
            self.consume(MINUS)

        # Expect current token to be an integer
        right = self.current_token
        self.consume(INTEGER)

        if operation.type == PLUS:
            result = left.value + right.value
        else:
            result = left.value - right.value
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


if __name__ == '__main__':
    main()
