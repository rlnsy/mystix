from typing import cast


class Value:

    def equals(self, v) -> bool:
        return False


class IntegerValue(Value):

    def __init__(self, val: int):
        self.value = val

    def equals(self, v: Value) -> bool:
        if type(v) is IntegerValue:
            return self.value == cast(IntegerValue, v).value
        else:
            return False
