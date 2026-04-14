
from dataclasses import dataclass, field


@dataclass
class Engine:
    volume: int
    pistons: int = field(default=6, repr=True)
"""
e1 = Engine(50)
e2 = Engine(50,6)

print(e1)
print(e2==e1)
"""