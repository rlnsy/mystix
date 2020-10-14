from .Func import Func
from ..Var import Var
from .Operand import Operand
from ..Value import Value


class SimpleFunc(Func):

    def __init__(self, impacted_var: Var, op: Operand, v: Value):
        self.impacted_var: Var = impacted_var
        self.op: Operand = op
        self.rhs = v
        pass

    operations = dict({
        "+": "__calcSum",
        "-": "__calcDif",
        "*": "__calcMul",
        "/": "__calcDiv",
        "^": "__calcPwr"
    })

    def __calcSum(self):
        self.impacted_var = self.impacted_var + self.rhs
        pass

    def __calcDif(self):
        self.impacted_var = self.impacted_var - self.rhs
        pass

    def __calcMul(self, parameter_list): 
        self.impacted_var = self.impacted_var * self.rhs
        pass

    def __calcDiv(self, parameter_list):
        self.impacted_var = self.impacted_var / self.rhs
        pass

    def __calcPwr(self, parameter_list):
        self.impacted_var = self.impacted_var ^ self.rhs
        pass

    def calculate(self):
        # add error checking is op is invalid?
        self.operations.get(self.op)()
        pass

    pass