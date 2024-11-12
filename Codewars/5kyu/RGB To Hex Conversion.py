"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
Examples (input --> output):

255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
"""

# Solution:

def clamp_and_convert(color):
    clamped_value = max(0, min(255, color))
    hex_value = hex(clamped_value).lstrip('0x').upper().zfill(2)

    return hex_value


def rgb(r, g, b):
    r_hex = clamp_and_convert(r)
    g_hex = clamp_and_convert(g)
    b_hex = clamp_and_convert(b)

    rgb_hex = r_hex + g_hex + b_hex

    return rgb_hex
