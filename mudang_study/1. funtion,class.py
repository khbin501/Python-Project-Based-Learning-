from dataclasses import dataclass

@dataclass
class BusType:
    name : str
    decrease_level : int

def level_check(level):
    if level <=2:
        return'여유'
    if level == 3:
        return'보통'
    return '혼잡'

def minus_level(bus: BusType,level):
    return level - bus.decrease_level

s_mudang = BusType("s_mudang", 2)
m_mudang = BusType("m_mudang", 4)
b_mudang = BusType("b_mudang", 5)

current_level  = int(input())
print(level_check(current_level))
current_level = minus_level(s_mudang, current_level)
print(current_level)