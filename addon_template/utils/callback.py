from typing import Set


class CallbackSet:
    def __init__(self):
        self.callback_func: Set[callable] = set()

    def __iadd__(self, function: callable) -> None:
        self.add(function)

    def __isub__(self, function: callable) -> bool:
        return self.remove(function)

    def add(self, function: callable) -> None:
        self.callback_func.add(function)

    def remove(self, function: callable) -> bool:
        if function in self.callback_func:
            self.callback_func.remove(function)
            return True
        return False

    def __call__(self, *args, **kwargs) -> None:
        for call in self.callback_func:
            call(*args, **kwargs)
