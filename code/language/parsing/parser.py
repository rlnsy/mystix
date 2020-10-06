from typing import List

from code.language.shared.ast import Program, Body


def parse(tokens: List[str]) -> Program:
    """
    PARSER
    """
    return Program(Body([]))  # stub
