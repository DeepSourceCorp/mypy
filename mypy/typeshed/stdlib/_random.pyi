# Actually Tuple[(int,) * 625]
_State = tuple[int, ...]

class Random:
    def __init__(self, seed: object = ...) -> None: ...
    def seed(self, __n: object = ...) -> None: ...
    def getstate(self) -> _State: ...
    def setstate(self, __state: _State) -> None: ...
    def random(self) -> float: ...
    def getrandbits(self, __k: int) -> int: ...
