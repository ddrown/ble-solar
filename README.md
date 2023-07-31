This uses [gatttool](https://manpages.debian.org/unstable/bluez/gatttool.1.en.html) (a bluetooth low energy utility) to speak to a solar charge controller made by Helios.

This is a proof of concept and has a lot of rough edges. Everything is experimental and may not be reliable.

I'm testing against the [HQST 40A MPPT controller](https://hqsolarpower.com/40a-mppt-solar-charge-controller-with-parallel-charging-bluetooth/)

I suspect the other rebranded controllers will also work:
* LiTime https://www.litime.com/products/litime-30a-mppt-12v-24v-auto-dc-input-solar-charge-controller-with-bluetooth-adapter
* Helios https://www.helios-ne.com/mppt-charge-controller-40a.com
* BougeRV https://www.bougerv.com/products/40a-mppt-solar-charge-controller

And anything other MPPT solar charge controller using the PVChargePro/ChargePro2.0 app is worth experimenting with

This assumes the computer collecting the data is in a different location than the bluetooth adapter and uses ssh to gather the data. I'm using a USB bluetooth adapter on an openwrt access point in the same room.

Example data is in the tests/ directory, along with its expected parsed output.

The protocol seems to be:
* write to handle 0xf / characteristic 0xffe0
* read via ble notifications
* two byte address (address 0x0103)
* one byte message length (length excluding itself, the address, and the crc)
* ending with a two byte crc

Most values seem to be two bytes long

An example Grafana dashboard, solar panels were plugged in around 12:50 and batteries accepted about 18AH before they hit the full setting of 14V:

![graphs from Grafana](https://github.com/ddrown/ble-solar/blob/main/example-graphs.png?raw=true)
