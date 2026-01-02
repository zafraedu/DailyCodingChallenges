def space_jam(s: str) -> str:
    s = s.replace(' ', '')
    return '  '.join(s).upper()


# Tests
print(space_jam("freeCodeCamp"))
print(space_jam(' free Code Camp '))
print(space_jam("Hello World?!"))
print(space_jam("C@t$ & D0g$"))
print(space_jam("allyourbase"))
