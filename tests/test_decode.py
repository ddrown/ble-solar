import decode

# -------- run1 ----------------------------------
def test_run1_group1():
    group1 = ['01 03 26 00 64 00 8a 00 02 00 00 1c 19 00 00 00 00 00 00 01', '96 00 8c 00 35 00 00 00 05 00 00 00 24 00 00 05 65 00 00 00', '34 1d 3c']
    decoded = decode.group1decode(group1)
    assert decoded["battery_v"] == 13.8
    assert decoded["battery_a"] == 0.02
    assert decoded["temp_controller"] == 28
    assert decoded["temp_battery"] == 25
    assert decoded["solar_v"] == 40.6
    assert decoded["max_charge_w"] == 140
    assert decoded["dcload_v"] == 0
    assert decoded["dcload_a"] == 0
    assert decoded["dcload_w"] == 0
    assert decoded["solar_w"] == 0
    assert decoded["charge_today_wh"] == 53
    assert decoded["charge_total_wh"] == 1381
    assert decoded["dcload_today_wh"] == 0
    assert decoded["dcload_total_wh"] == 52
    assert decoded["mppt_mode"] == 0
    assert decoded["float_mode"] == 1
    assert decoded["maxv_mode"] == 1
    assert decoded["dcload_mode"] == 0

def test_run1_group2():
    group2 = ['01 03 22 00 01 00 0c 00 04 00 8a 00 8a 00 8a 00 7e 00 7e 00', '78 00 6f 00 00 00 00 00 0a 00 05 00 0f 00 00 00 00 88 eb']
    decoded = decode.group2decode(group2)
    assert decoded["system_v"] == 12
    assert decoded["boost_v_1"] == 13.8
    assert decoded["boost_v_2"] == 13.8
    assert decoded["boost_v_3"] == 13.8
    assert decoded["over_recovery_v_1"] == 12.6
    assert decoded["over_recovery_v_2"] == 12.6
    assert decoded["over_discharge_v"] == 11.1
    assert decoded["light_delay_s"] == 10
    assert decoded["light_control_v"] == 5

def test_run1_group3():
    group3 = ['01 03 0a 00 35 00 00 00 8c 00 8b 00 84 2e 71']
    decoded = decode.group3decode(group3)
    assert decoded["total_charge_wh"] == 53
    assert decoded["max_charge_w_3"] == 140
    assert decoded["highest_v"] == 13.9
    assert decoded["lowest_v"] == 13.2

def test_run1_group4():
    group4 = ['01 03 02 00 00 b8 44']
    decoded = decode.group4decode(group4)
    assert decoded["errors"] == 0

# -------- run2 ----------------------------------
def test_run2_group1():
    group1 = ['01 03 26 00 64 00 88 00 00 00 00 1a 19 00 00 00 00 00 00 00', '00 00 8c 00 4a 00 00 00 00 00 00 00 25 00 00 05 7a 00 00 00', '34 25 10']
    decoded = decode.group1decode(group1)
    assert decoded["battery_v"] == 13.6 # todo: screenshot shows 13.7
    assert decoded["battery_a"] == 0
    assert decoded["temp_controller"] == 26
    assert decoded["temp_battery"] == 25
    assert decoded["solar_v"] == 0
    assert decoded["max_charge_w"] == 140
    assert decoded["dcload_v"] == 0
    assert decoded["dcload_a"] == 0
    assert decoded["dcload_w"] == 0
    assert decoded["solar_w"] == 0
    assert decoded["charge_today_wh"] == 74
    assert decoded["charge_total_wh"] == 1402
    assert decoded["dcload_today_wh"] == 0
    assert decoded["dcload_total_wh"] == 52
    assert decoded["mppt_mode"] == 0
    assert decoded["float_mode"] == 0
    assert decoded["maxv_mode"] == 0
    assert decoded["dcload_mode"] == 0

def test_run2_group2():
    group2 = ['01 03 22 00 01 00 0c 00 04 00 8a 00 8a 00 8a 00 7e 00 7e 00', '78 00 6f 00 00 00 00 00 0a 00 05 00 0f 00 00 00 00 88 eb']
    decoded = decode.group2decode(group2)
    assert decoded["system_v"] == 12
    assert decoded["boost_v_1"] == 13.8
    assert decoded["boost_v_2"] == 13.8
    assert decoded["boost_v_3"] == 13.8
    assert decoded["over_recovery_v_1"] == 12.6
    assert decoded["over_recovery_v_2"] == 12.6
    assert decoded["over_discharge_v"] == 11.1
    assert decoded["light_delay_s"] == 10
    assert decoded["light_control_v"] == 5

def test_run2_group3():
    group3 = ['01 03 0a 00 4a 00 00 00 8c 00 8a 00 88 5b 86']
    decoded = decode.group3decode(group3)
    assert decoded["total_charge_wh"] == 74
    assert decoded["max_charge_w_3"] == 140
    assert decoded["highest_v"] == 13.8
    assert decoded["lowest_v"] == 13.6

def test_run2_group4():
    group4 = ['01 03 02 00 00 b8 44']
    decoded = decode.group4decode(group4)
    assert decoded["errors"] == 0

# -------- run3 ----------------------------------
def test_run3_group1():
    group1 = ['01 03 26 00 64 00 8b 06 df 00 f4 25 19 00 00 00 00 00 00 02', 'ad 01 15 01 41 00 00 00 05 00 00 00 25 00 00 06 bb 00 00 00', '34 47 44']
    decoded = decode.group1decode(group1)
    assert decoded["battery_v"] == 13.9
    assert decoded["battery_a"] == 17.59 # was 17.8 at screenshot, but data capture was minutes later
    assert decoded["temp_controller"] == 37
    assert decoded["temp_battery"] == 25
    assert decoded["solar_v"] == 68.5
    assert decoded["max_charge_w"] == 277
    assert decoded["dcload_v"] == 0
    assert decoded["dcload_a"] == 0
    assert decoded["dcload_w"] == 0
    assert decoded["solar_w"] == 244
    assert decoded["charge_today_wh"] == 321
    assert decoded["charge_total_wh"] == 1723
    assert decoded["dcload_today_wh"] == 0
    assert decoded["dcload_total_wh"] == 52
    assert decoded["mppt_mode"] == 0
    assert decoded["float_mode"] == 1
    assert decoded["maxv_mode"] == 1
    assert decoded["dcload_mode"] == 0

def test_run3_group2():
    group2 = ['01 03 22 00 01 00 0c 00 04 00 8c 00 8c 00 8c 00 7e 00 7e 00', '78 00 6f 00 00 00 00 00 0a 00 05 00 0f 00 00 00 00 dc 38']
    decoded = decode.group2decode(group2)
    assert decoded["system_v"] == 12
    assert decoded["boost_v_1"] == 14.0
    assert decoded["boost_v_2"] == 14.0
    assert decoded["boost_v_3"] == 14.0
    assert decoded["over_recovery_v_1"] == 12.6
    assert decoded["over_recovery_v_2"] == 12.6
    assert decoded["over_discharge_v"] == 11.1
    assert decoded["light_delay_s"] == 10
    assert decoded["light_control_v"] == 5

def test_run3_group3():
    group3 = ['01 03 0a 01 79 00 00 01 15 00 8c 00 83 f6 b9']
    decoded = decode.group3decode(group3)
    assert decoded["total_charge_wh"] == 377
    assert decoded["max_charge_w_3"] == 277
    assert decoded["highest_v"] == 14.0
    assert decoded["lowest_v"] == 13.1

def test_run3_group4():
    group4 = ['01 03 02 00 00 b8 44']
    decoded = decode.group4decode(group4)
    assert decoded["errors"] == 0

# -------- run4 ----------------------------------
def test_run4_group1():
    group1 = ['01 03 26 00 64 00 86 00 00 00 00 1b 19 00 00 00 00 00 00 00', '00 01 15 03 34 00 00 00 00 00 00 00 26 00 00 08 ae 00 00 00', '34 38 d3']
    decoded = decode.group1decode(group1)
    assert decoded["battery_v"] == 13.4
    assert decoded["battery_a"] == 0
    assert decoded["temp_controller"] == 27
    assert decoded["temp_battery"] == 25
    assert decoded["solar_v"] == 0
    assert decoded["max_charge_w"] == 277
    assert decoded["dcload_v"] == 0
    assert decoded["dcload_a"] == 0
    assert decoded["dcload_w"] == 0
    assert decoded["charge_today_wh"] == 820
    assert decoded["charge_total_wh"] == 2222
    assert decoded["dcload_today_wh"] == 0
    assert decoded["dcload_total_wh"] == 52
    assert decoded["mppt_mode"] == 0
    assert decoded["float_mode"] == 0
    assert decoded["maxv_mode"] == 0
    assert decoded["dcload_mode"] == 0

def test_run4_group2():
    group2 = ['01 03 22 00 01 00 0c 00 04 00 8c 00 8c 00 8c 00 7e 00 7e 00', '78 00 6f 00 00 00 00 00 0a 00 05 00 0f 00 00 00 00 dc 38']
    decoded = decode.group2decode(group2)
    assert decoded["system_v"] == 12
    assert decoded["boost_v_1"] == 14.0
    assert decoded["boost_v_2"] == 14.0
    assert decoded["boost_v_3"] == 14.0
    assert decoded["over_recovery_v_1"] == 12.6
    assert decoded["over_recovery_v_2"] == 12.6
    assert decoded["over_discharge_v"] == 11.1
    assert decoded["light_delay_s"] == 10
    assert decoded["light_control_v"] == 5

def test_run4_group3():
    group3 = ['01 03 0a 03 34 00 00 01 15 00 86 00 86 de 21']
    decoded = decode.group3decode(group3)
    assert decoded["total_charge_wh"] == 820
    assert decoded["max_charge_w_3"] == 277
    assert decoded["highest_v"] == 13.4
    assert decoded["lowest_v"] == 13.4

def test_run4_group4():
    group4 = ['01 03 02 00 00 b8 44']
    decoded = decode.group4decode(group4)
    assert decoded["errors"] == 0

# -------- run5 ----------------------------------
def test_run5_group1():
    group1 = ['01 03 26 00 64 00 85 00 00 00 00 1a 19 00 85 00 36 00 07 00', '00 00 dd 01 29 00 14 80 00 00 00 00 27 00 00 09 d7 00 00 00', '49 ca 21']
    decoded = decode.group1decode(group1)
    assert decoded["battery_v"] == 13.3
    assert decoded["battery_a"] == 0
    assert decoded["temp_controller"] == 26
    assert decoded["temp_battery"] == 25
    assert decoded["solar_v"] == 0
    assert decoded["max_charge_w"] == 221
    assert decoded["dcload_v"] == 13.3
    assert decoded["dcload_a"] == 0.7
    assert decoded["dcload_w"] == 5.4 # ????
    assert decoded["solar_w"] == 0
    assert decoded["charge_today_wh"] == 297
    assert decoded["charge_total_wh"] == 2519
    assert decoded["dcload_today_wh"] == 20
    assert decoded["dcload_total_wh"] == 73
    assert decoded["mppt_mode"] == 0
    assert decoded["float_mode"] == 0
    assert decoded["maxv_mode"] == 0
    assert decoded["dcload_mode"] == 1

# -------- run6 ----------------------------------
def test_run6_group1():
    group1 = ['01 03 26 00 64 00 85 00 00 00 00 1a 19 00 85 00 12 00 02 00', '00 00 dd 01 29 00 1c 80 00 00 00 00 27 00 00 09 d7 00 00 00', '51 c3 0d']
    decoded = decode.group1decode(group1)
    assert decoded["battery_v"] == 13.3
    assert decoded["battery_a"] == 0
    assert decoded["temp_controller"] == 26
    assert decoded["temp_battery"] == 25
    assert decoded["solar_v"] == 0
    assert decoded["max_charge_w"] == 221
    assert decoded["dcload_v"] == 13.3
    assert decoded["dcload_a"] == 0.2
    assert decoded["dcload_w"] == 1.8 # ????
    assert decoded["solar_w"] == 0
    assert decoded["charge_today_wh"] == 297
    assert decoded["charge_total_wh"] == 2519
    assert decoded["dcload_today_wh"] == 28
    assert decoded["dcload_total_wh"] == 81
    assert decoded["mppt_mode"] == 0
    assert decoded["float_mode"] == 0
    assert decoded["maxv_mode"] == 0
    assert decoded["dcload_mode"] == 1
