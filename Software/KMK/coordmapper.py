from kmk.handlers.sequences import simple_key_sequence
from kmk.keys import KC

# *2 for split keyboards, which will typically manage twice the number of keys
# of one side. Having this N too large will have no impact (maybe slower boot..)
N = len(keyboard.col_pins) * len(keyboard.row_pins) * 2

keyboard.coord_mapping = list(range(N))

layer = []

for i in range(N):
    c, r = divmod(i, 100)
    d, u = divmod(r, 10)
    layer.append(
        simple_key_sequence(
            (
                getattr(KC, 'N' + str(c)),
                getattr(KC, 'N' + str(d)),
                getattr(KC, 'N' + str(u)),
                KC.SPC,
            )
        )
    )
print(layer)

if __name__ == '__main__':
    keyboard.go()
