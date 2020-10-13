from typing import List
import re


class tokenizer:

    def __init__(self, content: str):
        self.current_token = 0
        self.content = content
        self.fixed_literals = [';', '+', '-', '/', '^', '*', 'log', 'sin', 'cos', 'exp', 'xy"', 'line xy', 'true', 'false', 'number', 'category',
                               'binary', '"live"', '"static"', 'remote', 'plot', 'called', 'on new data from', 'map', 'to', '<START>', '<END>', '"="', '=']
        self.tokens: List[str] = []

    def tokenize(self) -> List[str]:
        """
        TOKENIZER
        """
        RESERVED_WORD = "_"

        # regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        tokenized_program = self.content.replace("\n", ";")
        print("tokenized program: ", tokenized_program)
        for p in self.fixed_literals:
            tokenized_program = tokenized_program.replace(
                p, RESERVED_WORD + p + RESERVED_WORD)
            print("Stepping: ", tokenized_program)
        tokenized_program = tokenized_program.replace(
            RESERVED_WORD+RESERVED_WORD, RESERVED_WORD)
        print(tokenized_program)
        if len(tokenized_program) > 0 and tokenized_program.startswith(RESERVED_WORD):
            tokenized_program = tokenized_program[len(RESERVED_WORD):]
        res = tokenized_program.split(RESERVED_WORD)
        print("Splitted: ", res)

        # TODO: optimize
        new_res = []
        for i in res:
            if i.strip():
                new_res.append(i.strip())
        print("Trimmed: ", new_res)
        self.tokens = list(new_res)
        return list(new_res)

    def check_next(self):
        if len(tokens) == 0:
            raise Exception('Error: No tokens loaded, use tokenize()')
        if self.current_token < len(self.tokens):
            return self.tokens[self.current_token]
        else:
            return "NO MORE TOKENS"

    def get_next(self):
        if len(tokens) == 0:
            raise Exception('Error: No tokens loaded, use tokenize()')
        if self.current_token < len(self.tokens):
            token = self.tokens[current_token]
            self.current_token += 1
        else:
            token = "NULLTOKEN"
        return token

    def check_token(self, regexp):
        s = self.check_next()
        print(f"Comparing {s} to {regexp}")
        return re.match(regexp, s)

    def get_and_check_next(self, regexp):
        s = self.get_next()
        if (re.match(regexp, s) == None):
            raise Exception(
                f"Unexpected token! Expected something matching {regexp}, got {s}")
        print(f"Matched {s} to {regexp}")
        return s

    def more_tokens(self):
        return self.current_token < self.tokens.length
