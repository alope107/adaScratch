def number_to_hex_string(num):
    prefix = '0x'
    hex_string = hex(num)
    if hex_string.startswith(prefix):
        hex_string = hex_string[len(prefix):]
    if len(hex_string) < 2:
        hex_string = '0' + hex_string
    return hex_string.upper()

print(number_to_hex_string(12))