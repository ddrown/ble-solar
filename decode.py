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
    decoded = {
        "unknown_1_1": sixteen(values, 3),
        "battery_v": sixteen_10(values, 5),
        "battery_a": sixteen_100(values, 7),
        "unknown_1_2": sixteen(values, 9),
        "temp_controller": values[11],
        "temp_battery": values[12],
        "unknown_1_3": sixteen(values, 13),
        "unknown_1_4": sixteen(values, 15),
        "unknown_1_5": sixteen(values, 17),
        "solar_v": sixteen_10(values, 19),
        "max_charge_w": sixteen(values, 21)
    }
    for i in range(23, 40, 2):
        decoded[f"unknown_1_{i}"] = sixteen(values, i)
    return decoded

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
