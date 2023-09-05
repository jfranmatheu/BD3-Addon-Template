import math
from typing import Tuple

from mathutils import Vector


class Vector2:
    x: float = 0.0
    y: float = 0.0

    @classmethod
    def zero(cls):
        return cls(0.0, 0.0)

    def reset(self):
        self.x = 0.0
        self.y = 0.0

    def __set__(self, instance, values: Tuple[float, float] or Tuple[int, int]):
        if not isinstance(values, (Tuple[float, float], Tuple[int, int])):
            raise TypeError('Only objects of type Tuple[float, float] and Tuple[int, int] can be assigned')
        self.x, self.y = values  # This can be self.val = MyCustomClass(val) as well.

    def copy(self) -> 'Vector2':
        return Vector2(self.x, self.y)

    def to_tuple(self) -> Tuple[float, float]:
        return (self.x, self.y)

    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __iadd__(self, other: 'Vector2'):
        self.x += other.x
        self.y += other.y

    def __isub__(self, other: 'Vector2'):
        self.x -= other.x
        self.y -= other.y

    def __imul__(self, other: 'Vector2'):
        self.x *= other.x
        self.y *= other.y

    def __idiv__(self, other: 'Vector2'):
        self.x /= other.x
        self.y /= other.y

    def __add__(self, other: 'Vector2'):
        return Vector2(self.x+other.x, self.y+other.y)

    def __sub__(self, other: 'Vector2'):
        return Vector2(self.x-other.x, self.y-other.y)

    def __mul__(self, other: 'Vector2'):
        return Vector2(self.x*other.x, self.y*other.y)

    def __div__(self, other: 'Vector2'):
        return Vector2(self.x/other.x, self.y/other.y)


    def distance(self, other: 'Vector2') -> float:
        return math.dist([self.x, self.y], [other.x, other.y])


    def __str__(self) -> str:
        return "Vector2(float): [X:%f, Y:%f]" % (self.x, self.y)


class Vector2i:
    x: int = 0
    y: int = 0

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def reset(self):
        self.x = 0
        self.y = 0

    def __set__(self, instance, values: Tuple[int, int] or 'Vector2i'):
        if isinstance(values, Vector2i):
            values = values.x, values.y
        elif not isinstance(values, (Tuple[int, int])):
            raise TypeError('Only objects of type Tuple[int, int] can be assigned')
        self.x, self.y = values  # This can be self.val = MyCustomClass(val) as well.

    def is_zero(self) -> bool:
        return int(self.x) == 0 and int(self.y) == 0

    def copy(self) -> 'Vector2i':
        return Vector2i(self.x, self.y)

    def to_tuple(self) -> Tuple[int, int]:
        return self.x, self.y
    
    def to_vector(self) -> Vector:
        return Vector((self.x, self.y))

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __iadd__(self, other: 'Vector2i'):
        self.x += other.x
        self.y += other.y

    def __isub__(self, other: 'Vector2i'):
        self.x -= other.x
        self.y -= other.y

    def __imul__(self, other: 'Vector2i'):
        self.x *= other.x
        self.y *= other.y

    def __idiv__(self, other: 'Vector2i'):
        self.x /= other.x
        self.y /= other.y

    def __add__(self, other: 'Vector2i') -> 'Vector2i':
        return Vector2i(self.x+other.x, self.y+other.y)

    def __sub__(self, other: 'Vector2i') -> 'Vector2i':
        return Vector2i(self.x-other.x, self.y-other.y)

    def __mul__(self, other: 'Vector2i') -> 'Vector2i':
        return Vector2i(self.x*other.x, self.y*other.y)

    def __truediv__(self, other: 'Vector2i') -> 'Vector2i':
        return Vector2i(self.x/other.x, self.y/other.y)

    ## def clamp(self, min_value: int, max_value: int) -> None:
    ##     self.x = clamp(self.x, min_value, max_value)
    ##     self.y = clamp(self.y, min_value, max_value)

    def distance(self, other: 'Vector2i') -> float:
        return math.dist([self.x, self.y], [other.x, other.y])


    def __str__(self) -> str:
        return "Vector2(int): [X:%i, Y:%i]" % (self.x, self.y)
