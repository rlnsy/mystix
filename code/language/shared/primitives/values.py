from typing import cast


class Value:

    def equals(self, v) -> bool:
        return False


class NumericalValue(Value):

    def __init__(self):
        self.value = 0

    def equals(self, v: Value) -> bool:
        if isinstance(v, NumericalValue):
            return self.value == cast(NumericalValue, v).value
        else:
            return False


class IntegerValue(NumericalValue):

    def __init__(self, val: int):
        super(NumericalValue, self).__init__()
        self.value = val


class FloatValue(NumericalValue):

    def __init__(self, val: float):
        super(NumericalValue, self).__init__()
        self.value = val
