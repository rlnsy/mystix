from typing import List


def tokenize(content: str) -> List[str]:
    """
    TOKENIZER
    """
    RESERVED_WORD = "_"
    fixed_literals = [';', '+', '-', '/', '^', '*', 'log', 'sin', 'cos', 'exp', 'xy"', 'line xy', 'true', 'false', 'number', 'category',
                      'binary', '"live"', '"static"', 'remote', 'plot', 'called', 'on new data from', 'map', 'to', '<START>', '<END>', '"="', '=']
    tokens = 0
    current_token = 0

    tokenized_program = content.replace("\n", ";")
    print("tokenized program: ", tokenized_program)
    for p in fixed_literals:
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
        new_res.append(i.strip())
    print("Trimmed: ", new_res)
    return list(new_res)
