import pexpect
import sys
import re

def waitNotification(ssh):
    ssh.expect("Notification handle")
    ssh.expect("> ")
    m = re.search("^ = 0x000f value: (.*?)\s*\r\n", ssh.before.decode())
    return m.group(1)

def cmd(ssh, cmd, lines):
    ssh.sendline(f"char-write-cmd 0xf {cmd}")
    values = []
    for i in range(0, lines):
        values.append(waitNotification(ssh))
    return values

def gather(host, mac):
    groups = []
    ssh = pexpect.spawn("ssh", [host,"gatttool","--device",mac,"--interactive"], timeout=2, logfile=sys.stdout.buffer)
    ssh.expect("> ")
    try:
        ssh.sendline("connect")
        ssh.expect("Connection successful")
        ssh.expect("> ")
        # subscribe to notifications
        ssh.sendline("char-write-req 0x10 0100")
        ssh.expect("Characteristic value was written successfully")
        ssh.expect("> ")

        # get group 1 data
        groups.append(cmd(ssh, "010301010013543b", 3))

        # get group 2 data
        groups.append(cmd(ssh, "010302010011e47e15c0", 2))

        # get group 3 data
        groups.append(cmd(ssh, "01030400000584f9", 1))

        # get group 4 data
        groups.append(cmd(ssh, "010301210001d5fc", 1))

        # disconnect
        ssh.sendline("disconnect")
        ssh.expect("> ")
        ssh.sendline("quit")
        ssh.expect(pexpect.EOF)
    except Exception as e:
        print(e)
        ssh.sendline("quit")

    return groups
