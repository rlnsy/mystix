import unittest

from code.language.shared import ast


class ASTTests(unittest.TestCase):

    def test_program_construction(self):
        try:
            b: ast.Body = ast.Body([ast.Command(), ast.Command()])
            p: ast.Program = ast.Program(b)
        except TypeError:
            self.fail("Failed to build")
