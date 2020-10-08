from typing import List

from ..Node import Node
from .Func import Func


class MathFuncs(Node):
    def __init__(self, function_list: List[Func]):
        self.mth_func_lst: List[Func] = function_list
