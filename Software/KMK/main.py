import board
from kb import KMKKeyboard

from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys

from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.handlers.sequences import simple_key_sequence

print("Starting")
keyboard = KMKKeyboard()

# Add extensions
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())
keyboard.modules.append(ModTap())

# Enable debugging
keyboard.debug_enabled = True


# Cleaner Keycodes
# Colemak
XXXXX = KC.NO
SYSLAYER = KC.LT(2, KC.TG(2))
NUMLAYER = KC.LT(1, KC.TG(1))
SSPC = KC.LT(1, KC.SPC)
# Home row mods
MODA = KC.MT(KC.A, KC.LCTL)
MODR = KC.MT(KC.R, KC.LALT)
MODS = KC.MT(KC.S, KC.LGUI)
MODT = KC.MT(KC.T, KC.LSFT)
MODN = KC.MT(KC.N, KC.RSFT)
MODE = KC.MT(KC.E, KC.RGUI)
MODI = KC.MT(KC.I, KC.RALT)
MODO = KC.MT(KC.O, KC.RCTL)

# System
COPYPASTE = KC.MT(KC.LCTL(KC.C), KC.LCTL(KC.V))
tabp = KC.MT(KC.LALT(KC.LGUI, KC.LEFT),KC.LCTL)
tabn = KC.MT(KC.LALT(KC.LGUI, KC.RIGHT), KC.LALT)
deskp = KC.MT(KC.LCTL(KC.LEFT), KC.LGUI)
deskn = KC.MT(KC.LCTL(KC.RIGHT), KC.LSFT)
back = KC.LGUI(KC.LCBR)
fwd = KC.LGUI(KC.RCBR)

layer = []

N = len(keyboard.row_pins) * len(keyboard.col_pins) * 2
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
keyboard.keymap = [layer]

# keyboard.keymap = [
#     [   # COLEMAK DH
#          KC.TAB  ,  KC.Q   ,  KC.W   ,  KC.F  , KC.P  ,  KC.B  , KC.BRIU ,      KC.VOLU  ,   KC.J   ,  KC.L   ,  KC.U   ,  KC.Y   , KC.SCOLON , KC.BSPC ,
#          KC.CAPS ,  KC.A   ,  KC.R   ,  KC.S  , KC.T  ,  KC.G  , KC.BRID ,      KC.VOLD  ,   KC.M   ,  KC.N   ,  KC.E   ,  KC.I   ,   KC.O    , KC.ENT  ,
#          KC.TRNS ,  KC.Z   ,  KC.X   ,  KC.C  , KC.D  ,  KC.V  ,  XXXXX  ,       XXXXX   ,   KC.K   ,  KC.H   , KC.COMM , KC.DOT  ,  KC.SLSH  , KC.QUOT ,
#          KC.TRNS , KC.TRNS , KC.TRNS , KC.ESC , XXXXX , KC.SPC , KC.TRNS ,      SYSLAYER , NUMLAYER , KC.TRNS ,  XXXXX  , KC.MRWD ,  KC.MPLY  , KC.MFFD ,
#     ],
# 
#     [  # NUMBERS AND SYMBOLS
#          KC.TRNS , KC.PSLS , KC.N7   , KC.N8 , KC.N9 , KC.PPLS , KC.TRNS ,    KC.TRNS , KC.BSLS , KC.LCBR , KC.RCBR , KC.DLR  , KC.AT   , KC.CIRC ,
#          KC.TRNS , KC.PAST , KC.N4   , KC.N5 , KC.N6 , KC.PMNS , KC.TRNS ,    KC.TRNS , KC.PIPE , KC.LPRN , KC.RPRN , KC.EXLM , KC.HASH , KC.UNDS ,
#          KC.TRNS , KC.TRNS , KC.N1   , KC.N2 , KC.N3 , KC.DOT  , XXXXX   ,    XXXXX   , KC.TRNS , KC.LBRC , KC.RBRC , KC.AMPR , KC.GRV  , KC.PERC ,
#          KC.TRNS , KC.TRNS , KC.TRNS , KC.N0 , XXXXX , KC.TRNS , KC.TRNS ,    KC.TRNS , KC.TRNS , KC.TRNS , XXXXX   , KC.TRNS , KC.TRNS , KC.TRNS ,
#     ],
# 
#     [  # SYSTEM - macOS
#          KC.TRNS , KC.TRNS , KC.TRNS ,  KC.TRNS   ,  KC.TRNS  , KC.TRNS , KC.TRNS ,     KC.TRNS , KC.TRNS ,  KC.TRNS   , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS ,
#          KC.TRNS ,  tabp   ,  tabn   ,  deskp     ,  deskn    , KC.TRNS , KC.TRNS ,     KC.TRNS , KC.LEFT ,  KC.DOWN   , KC.UP   , KC.RGHT , KC.TRNS , KC.TRNS ,
#          KC.TRNS , KC.TRNS , KC.TRNS ,    back    ,  fwd      , KC.TRNS , XXXXX   ,     XXXXX   , KC.TRNS , COPYPASTE  , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS ,
#          KC.TRNS , KC.TRNS , KC.TRNS ,  KC.TRNS   ,  XXXXX    , KC.TRNS , KC.TRNS ,     KC.TRNS , KC.TRNS ,  KC.TRNS   , XXXXX   , KC.TRNS , KC.TRNS , KC.TRNS ,
#     ],
# 
#     [  # Fn
#          KC.TRNS , KC.TRNS , KC.F7   , KC.F8   , KC.F9   , KC.F10  , KC.TRNS ,     KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS ,
#          KC.TRNS , KC.TRNS , KC.F4   , KC.F5   , KC.F6   , KC.F11  , KC.TRNS ,     KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS ,
#          KC.TRNS , KC.TRNS , KC.F1   , KC.F2   , KC.F3   , KC.F12  , XXXXX   ,     XXXXX   , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS ,
#          KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS , XXXXX   , KC.TRNS , KC.TRNS ,     KC.TRNS , KC.TRNS , KC.TRNS , XXXXX   , KC.TRNS , KC.TRNS , KC.TRNS ,
#     ],
# 
#     [  # Tetris
#          KC.TRNS , KC.TRNS , KC.TRNS , KC.W    , KC.TRNS , KC.TRNS , KC.TRNS ,     KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS ,
#          KC.TRNS , KC.TRNS , KC.A    , KC.S    , KC.D    , KC.TRNS , KC.TRNS ,     KC.TRNS , KC.TRNS , KC.J    , KC.TRNS , KC.L    , KC.TRNS , KC.TRNS ,
#          KC.F4   , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS , XXXXX   ,      XXXXX  , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS ,
#          KC.TRNS , KC.TRNS , KC.TRNS , KC.TRNS , XXXXX   , KC.SPC  , KC.TRNS ,     KC.TRNS , KC.TRNS , KC.TRNS ,  XXXXX  , KC.TRNS , KC.TRNS , KC.TRNS ,
#     ]
# ]
#


if __name__ == '__main__':
    import digitalio
    from time import sleep
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT
    led.value = True
    sleep(0.5)
    led.value = False
    
    keyboard.go()

