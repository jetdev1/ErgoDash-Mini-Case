import board
from storage import getmount

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide, SplitType


class KMKKeyboard(_KMKKeyboard):
    # Identify which side this is
    side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT

    if side == SplitSide.LEFT:
        row_pins = (board.GP10, board.GP11, board.GP12, board.GP13)
        col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8)
        # Define wiring
        dpin = board.GP18
        dpin2 = board.GP19  
    else:
        row_pins = (board.GP27, board.GP26, board.GP22, board.GP21)
        col_pins = (board.GP8, board.GP7, board.GP6, board.GP5, board.GP4, board.GP3, board.GP2)
        dpin = board.GP26
        dpin2 = board.GP27

    diode_orientation = DiodeOrientation.COL2ROW
    # *2 for split keyboards, which will typically manage twice the number of keys
    # of one side. Having this N too large will have no impact (maybe slower boot..)
    N = len(col_pins) * len(row_pins) * 2
    coord_mapping = list(range(N))

    split = Split(
        split_side=side,
        split_target_left=True,
        split_flip=True,
        split_type=SplitType.UART,
        uart_interval=20,
        data_pin=dpin,
        data_pin2=dpin2,
        use_pio=True
    )
    modules = [split]

