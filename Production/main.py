from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.row_pins = (
    board.GP6,
    board.GP7,
    board.GP0,
)
keyboard.col_pins = (
    board.GP26,
    board.GP27,
    board.GP28,
    board.GP29,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# keyboard.modules = [layers, holdtap, encoder_handler]
keyboard.modules.append(Layers())
keyboard.modules.append(EncoderHandler())
keyboard.extensions.append(MediaKeys())

keyboard.keymap = [
    [KC.ESC, KC.BRID, KC.BRIU, KC.MPLY],
    [KC.INSERT, KC.UP, KC.DELETE, KC.MUTE],
    [KC.LEFT, KC.DOWN, KC.RIGHT, KC.ESC],
    # last entry is placeholder, there is no wire there
]

encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (
        board.GP3,
        board.GP4,
        None,
    ),
    (
        board.GP2,
        board.GP1,
        None,
    ),
)

encoder_handler.map = [
    (
        (KC.VOLD, KC.VOLU),
        (KC.LCTRL(KC.EQUAL), KC.LCTRL(KC.MINUS)),
    )
]

if __name__ == "__main__":
    keyboard.go()
