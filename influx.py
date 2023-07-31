#!venv/bin/python

from influxdb import InfluxDBClient
from datetime import datetime, timezone

client = InfluxDBClient(host='localhost', port=8086)

client.switch_database("solar-charger")
client.write_points([{
    "measurement": "charger",
    "time": datetime.now(tz=timezone.utc).replace(microsecond=0).isoformat(),
    "fields": {
        'unknown_1_1': 100,
        'battery_v': 13.4,
        'battery_a': 0.0,
        'unknown_1_2': 0,
        'temp_controller': 26,
        'temp_battery': 25,
        'unknown_1_3': 0,
        'unknown_1_4': 0,
        'unknown_1_5': 0,
        'solar_v': 0.0,
        'max_charge_w': 277,
        'unknown_1_23': 820,
        'unknown_1_25': 0,
        'unknown_1_27': 0,
        'unknown_1_29': 0,
        'unknown_1_31': 38,
        'unknown_1_33': 0,
        'unknown_1_35': 2222,
        'unknown_1_37': 0,
        'unknown_1_39': 52,
        'unknown_2_1': 1,
        'system_v': 12,
        'unknown_2_2': 4,
        'boost_v_1': 14.0,
        'boost_v_2': 14.0,
        'boost_v_3': 14.0,
        'over_recovery_v_1': 12.6,
        'over_recovery_v_2': 12.6,
        'unknown_2_3': 120,
        'over_discharge_v': 11.1,
        'unknown_2_4': 0,
        'unknown_2_5': 0,
        'light_delay_s': 10,
        'light_control_v': 5,
        'unknown_2_31': 15,
        'unknown_2_33': 0,
        'unknown_2_35': 0,
        'total_charge_wh': 820,
        'unknown_3_2': 0,
        'max_charge_w_3': 277,
        'highest_v': 13.4,
        'lowest_v': 13.4,
        'errors': 0
    }
}])

