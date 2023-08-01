# thirty-two bits from four 8 bit values
def thirtytwo(values, start_offset):
    return values[start_offset] << 24 | values[start_offset+1] << 16 | values[start_offset+2] << 8 | values[start_offset+3] 

# sixteen bits from two 8 bit values
def sixteen(values, start_offset):
    return values[start_offset] << 8 | values[start_offset+1]

# sixteen bits from two 8 bit values, divided by 10
def sixteen_10(values, start_offset):
    return sixteen(values, start_offset)/10

# sixteen bits from two 8 bit values, divided by 100
def sixteen_100(values, start_offset):
    return sixteen(values, start_offset)/100

# 1 = 010301010013543b
def group1decode(bytes):
    values = base_decode(bytes)
    flags = sixteen(values, 27)
    decoded = {
        "unknown_1_1": sixteen(values, 3),
        "battery_v": sixteen_10(values, 5),
        "battery_a": sixteen_100(values, 7),
        "solar_w": sixteen(values, 9),
        "temp_controller": values[11],
        "temp_battery": values[12],
        "dcload_v": sixteen_10(values, 13),
        "dcload_w": sixteen_10(values, 15),
        "dcload_a": sixteen_10(values, 17),
        "solar_v": sixteen_10(values, 19),
        "max_charge_w": sixteen(values, 21),
        "charge_today_wh": sixteen(values, 23),
        "dcload_today_wh": sixteen(values, 25),
        "mppt_mode": 1 if (flags & 0x2) else 0,
        "float_mode": 1 if (flags & 0x4) else 0, # or is this "max volt"?
        "maxv_mode": 1 if (flags & 0x1) else 0, # or is this "float mode"?
        "dcload_mode": 1 if (flags & 0x8000) else 0,
        "unknown_1_27": flags,
        "unknown_1_29": sixteen(values, 29),
        "unknown_1_31": sixteen(values, 31),
        "charge_total_wh": thirtytwo(values, 33),
        "dcload_total_wh": thirtytwo(values, 37),
    }
    return decoded

# flags
# start = 0
# 2023-07-30 12:52:46 = 2     (solar charge on, mppt?)
# 2023-07-30 14:10:16 = 5     (solar charge float?)
# 2023-07-30 14:17:30 = 32773 (dc load on)
# 2023-07-30 17:14:12 = 32768
# 2023-07-31 08:30:46 = 0     (dc load off)

# 2 = 010302010011e47e15c0
def group2decode(bytes):
    values = base_decode(bytes)
    decoded = {
        "unknown_2_1": sixteen(values, 3),
        "system_v": sixteen(values, 5),
        "unknown_2_2": sixteen(values, 7),
        "boost_v_1": sixteen_10(values, 9),
        "boost_v_2": sixteen_10(values, 11),
        "boost_v_3": sixteen_10(values, 13),
        "over_recovery_v_1": sixteen_10(values, 15),
        "over_recovery_v_2": sixteen_10(values, 17),
        "unknown_2_3": sixteen(values, 19),
        "over_discharge_v": sixteen_10(values, 21),
        "unknown_2_4": sixteen(values, 23),
        "unknown_2_5": sixteen(values, 25),
        "light_delay_s": sixteen(values, 27),
        "light_control_v": sixteen(values, 29),
    }
    for i in range(31, 36, 2):
        decoded[f"unknown_2_{i}"] = sixteen(values, i)
    return decoded

# 3 = 01030400000584f9
def group3decode(bytes):
    values = base_decode(bytes)
    decoded = {
        "total_charge_wh": sixteen(values, 3),
        "unknown_3_2": sixteen(values, 5),
        "max_charge_w_3": sixteen(values, 7),
        "highest_v": sixteen_10(values, 9),
        "lowest_v": sixteen_10(values, 11),
    }
    return decoded

# 4 = 010301210001d5fc
def group4decode(bytes):
    values = base_decode(bytes)
    decoded = {
        "errors": sixteen(values, 3) # this is unverified
    }
    return decoded

def base_decode(values):
    hex = " ".join(values).split(" ")
    bytes = [int(byte, 16) for byte in hex]

    # 2 header (address?) bytes
    if bytes[0] != 1 or bytes[1] != 3:
        print(f"expected header 1,3 got {bytes[0]},{bytes[1]}")
        return []

    # 1 message length byte
    length = bytes[2]
    if length != len(bytes) - 5:
        print(f"expected length {length}, got length {length(bytes)-5}")
        return []
    return bytes
