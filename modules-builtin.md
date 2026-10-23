*Modules Builtin*
---- Sent utf8 encoded message: "help('modules')\r" ----
help('modules')
__main__          hifive            neopixel          this
antigravity       love              network           time
array             machine           os                ubluetooth
audio             math              radio             ucollections
builtins          microbit          random            usocket
collections       micropython       speech            ustruct
esp32             mqtt              struct            utime
gc                music             sys
Plus any modules on the filesystem

import  antigravity
+-xkcd.com/353---------------------------------------------------+
|                                                                |
|                                                    \0/         |
|                                                  /   \         |
|        You're flying!                  MicroPython!  /|        |
|            How?                                      \ \       |
|            /                                                   |
|          0                                                     |
|         /|\                                                    |
|          |                                                     |
|-----____/_\______________________________----------------------|
|                                                                |
+----------------------------------------------------------------+
>>> 
---- Sent utf8 encoded message: "dir(antigravity)\r" ----
dir(antigravity)
['__name__', '__init__']

import array
>>> 
---- Sent utf8 encoded message: "dir(array)\r" ----
dir(array)
['__name__', 'array']

import audio
>>> 
---- Sent utf8 encoded message: "dir(audio)\r" ----
dir(audio)
['__name__', 'stop', 'play', 'is_playing', 'AudioFrame']

import builtins
>>> 
---- Sent utf8 encoded message: "dir(builtins)\r" ----
dir(builtins)
['__name__', '__build_class__', '__import__', '__repl_print__', 'bool', 'bytes', 'bytearray', 'dict', 'enumerate', 'filter', 'float', 'frozenset', 'int', 'list', 'map', 'object', 'range', 'reversed', 'set', 'slice', 'str', 'super', 'tuple', 'type', 'zip', 'classmethod', 'staticmethod', 'Ellipsis', 'abs', 'all', 'any', 'bin', 'callable', 'chr', 'dir', 'divmod', 'eval', 'exec', 'getattr', 'setattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'isinstance', 'issubclass', 'iter', 'len', 'locals', 'max', 'min', 'next', 'oct', 'ord', 'pow', 'print', 'repr', 'round', 'sorted', 'sum', 'BaseException', 'ArithmeticError', 'AssertionError', 'AttributeError', 'EOFError', 'Exception', 'GeneratorExit', 'ImportError', 'IndentationError', 'IndexError', 'KeyboardInterrupt', 'KeyError', 'LookupError', 'MemoryError', 'NameError', 'NotImplementedError', 'OSError', 'OverflowError', 'RuntimeError', 'StopIteration', 'SyntaxError', 'SystemExit', 'TypeError', 'UnicodeError', 'ValueError', 'ZeroDivisionError', 'open']

import collections
>>> 
---- Sent utf8 encoded message: "dir(collections)\r" ----
dir(collections)
['__name__', 'namedtuple', 'OrderedDict']

import esp32
>>> 
---- Sent utf8 encoded message: "dir(esp32)\r" ----
dir(esp32)
['test', 'reset', 'version', 'deep_sleep', 'echo_off', 'echo_on', 'restore', 'get_uart_current', 'get_uart_default', 'set_sleep_mode', 'get_sysram', 'get_sysflash', 'set_rf_power', 'raw_cmd', 'raw_ble_cmd', 'set_wifi_mode', 'get_wifi_mode', 'connect', 'get_connection', 'list_aps', 'disconnect', 'get_configuration', 'get_ips', 'get_dhcp', 'set_dhcp', 'set_auto_conn', 'start_smartconfig', 'stop_smartconfig', 'set_wps_mode', 'get_hostname', 'set_hostname', 'get_status', 'set_domain', 'get_dns_servers', 'get_station_mac', 'set_station_mac', 'get_softap_mac', 'set_softap_mac', 'get_station_ip', 'get_softap_ip', 'conn_open_tcp', 'conn_open_udp', 'conn_open_ssl', 'conn_close', 'cip_send', 'cip_send_multi', 'get_local_ip', 'get_conn_mux', 'set_conn_mux', 'get_max_connections', 'set_max_connections', 'get_trans_mode', 'set_trans_mode', 'get_tcp_timeout', 'set_tcp_timeout', 'set_cip_dinfo', 'get_sntp_server', 'get_sntp_time', 'ping', 'get_ble_init', 'set_ble_init', 'get_ble_addr', 'set_ble_addr', 'get_ble_name', 'set_ble_name', 'get_ble_scan_param', 'set_ble_scan_mode', 'set_ble_scan_resp', 'get_ble_adv_data', 'set_ble_adv_data', 'ble_start_adv', 'ble_stop_adv', 'get_ble_conn', 'get_ble_conn_param', 'ble_conn_disconnect', 'get_ble_mtu_len', 'ble_create_services', 'ble_start_services', 'ble_stop_services', 'get_ble_discover_services', 'get_ble_discover_char', 'hid_init', 'get_hid_init']

import gc
>>> 
---- Sent utf8 encoded message: "dir(gc)\r" ----
dir(gc)
['__name__', 'collect', 'disable', 'enable', 'isenabled', 'mem_free', 'mem_alloc', 'threshold']

import hifive
>>> 
---- Sent utf8 encoded message: "dir(hifive)\r" ----
dir(hifive)
['__name__', 'Image', 'display', 'button_a', 'button_b', 'accelerometer', 'compass', 'i2c', 'uart', 'spi', 'reset', 'sleep', 'running_time', 'panic', 'temperature', 'pin0', 'pin1', 'pin2', 'pin3', 'pin4', 'pin5', 'pin6', 'pin7', 'pin8', 'pin9', 'pin10', 'pin11', 'pin13', 'pin14', 'pin15', 'pin16', 'pin19', 'pin20']

import love
>>> 
---- Sent utf8 encoded message: "dir(love)\r" ----
dir(love)
['__name__', '__init__', 'badaboom']

import  machine
>>> 
---- Sent utf8 encoded message: "dir(machine)\r" ----
dir(machine)
['__name__', 'unique_id', 'reset', 'freq', 'disable_irq', 'enable_irq', 'mem8', 'mem16', 'mem32', 'time_pulse_us']

import math
>>>
---- Sent utf8 encoded message: "dir(math)\r" ----
dir(math)
['__name__', 'e', 'pi', 'sqrt', 'pow', 'exp', 'log', 'cos', 'sin', 'tan', 'acos', 'asin', 'atan', 'atan2', 'ceil', 'copysign', 'fabs', 'floor', 'fmod', 'frexp', 'ldexp', 'modf', 'isfinite', 'isinf', 'isnan', 'trunc', 'radians', 'degrees']

import microbit
>>> 
---- Sent utf8 encoded message: "dir(microbit)\r" ----
dir(microbit)
['__name__', 'Image', 'display', 'button_a', 'button_b', 'accelerometer', 'compass', 'i2c', 'uart', 'spi', 'reset', 'sleep', 'running_time', 'panic', 'temperature', 'pin0', 'pin1', 'pin2', 'pin3', 'pin4', 'pin5', 'pin6', 'pin7', 'pin8', 'pin9', 'pin10', 'pin11', 'pin13', 'pin14', 'pin15', 'pin16', 'pin19', 'pin20']

import micropython
>>> 
---- Sent utf8 encoded message: "dir(micropython)\r" ----
dir(micropython)
['__name__', 'const', 'opt_level', 'mem_info', 'qstr_info', 'stack_use', 'heap_lock', 'heap_unlock', 'kbd_intr']

import mqtt
>>> 
---- Sent utf8 encoded message: "dir(mqtt)\r" ----
dir(mqtt)
['__name__', 'MQTT', 'QOS_AT_MOST_ONCE', 'QOS_AT_LEAST_ONCE', 'QOS_EXACTLY_ONCE', 'SCHEME_TCP', 'SCHEME_SSL_NO_CERT', 'SCHEME_WEBSOCK_TCP', 'SCHEME_WEBSOCK_SSL']

import music
>>> 
---- Sent utf8 encoded message: "dir(music)\r" ----
dir(music)
['__name__', '__init__', 'reset', 'set_tempo', 'get_tempo', 'play', 'pitch', 'stop', 'DADADADUM', 'ENTERTAINER', 'PRELUDE', 'ODE', 'NYAN', 'RINGTONE', 'FUNK', 'BLUES', 'BIRTHDAY', 'WEDDING', 'FUNERAL', 'PUNCHLINE', 'PYTHON', 'BADDY', 'CHASE', 'BA_DING', 'WAWAWAWAA', 'JUMP_UP', 'JUMP_DOWN', 'POWER_UP', 'POWER_DOWN']

import neopixel
>>> 
---- Sent utf8 encoded message: "dir(neopixel)\r" ----
dir(neopixel)
['__name__', 'NeoPixel']

import network
>>> 
---- Sent utf8 encoded message: "dir(network)\r" ----
dir(network)
['__name__', 'WLAN', 'ESP32', 'STA_IF', 'AP_IF']

import os
>>> 
---- Sent utf8 encoded message: "dir(os)\r" ----
dir(os)
['__name__', 'remove', 'listdir', 'size', 'uname']

import radio
>>> 
---- Sent utf8 encoded message: "dir(radio)\r" ----
dir(radio)
['__name__', 'on', 'off', 'send_bytes', 'receive_bytes', 'send', 'receive', 'receive_bytes_into']

import random
>>> 
---- Sent utf8 encoded message: "dir(random)\r" ----
dir(random)
['__name__', 'getrandbits', 'seed', 'randrange', 'randint', 'choice', 'random', 'uniform']

import speech
>>> 
---- Sent utf8 encoded message: "dir(speech)\r" ----
dir(speech)
['__name__', 'say', 'sing', 'pronounce', 'translate']

import struct
>>> 
---- Sent utf8 encoded message: "dir(struct)\r" ----
dir(struct)
['__name__', 'calcsize', 'pack', 'pack_into', 'unpack', 'unpack_from']

import sys
>>> 
---- Sent utf8 encoded message: "dir(sys)\r" ----
dir(sys)
['__name__', 'version', 'version_info', 'implementation', 'platform', 'byteorder', 'exit', 'print_exception']

import this
>>> 
---- Sent utf8 encoded message: "dir(this)\r" ----
dir(this)
['__name__', '__init__', 'authors']

import time
>>> 
---- Sent utf8 encoded message: "dir(time)\r" ----
dir(time)
['__name__', 'sleep', 'sleep_ms', 'sleep_us', 'ticks_ms', 'ticks_us', 'ticks_add', 'ticks_diff']

import ubluetooth
>>> 
---- Sent utf8 encoded message: "dir(ubluetooth)\r" ----
dir(ubluetooth)
['__name__', 'BLE', 'Client', 'Server', 'SEC_NONE', 'SEC_ENCRYPT', 'SEC_ENCRYPT_NO_MITM', 'SEC_ENCRYPT_MITM', 'NO_BOND', 'BOND', 'MITM', 'SC_ONLY', 'SC_BOND', 'SC_MITM', 'SC_MITM_BOND', 'DISPLAY_ONLY', 'DISPLAY_YES_NO', 'KEYBOARD_ONLY', 'NO_INPUT_NO_OUTPUT', 'KEYBOARD_DISPLAY']

import ucollections
>>> 
---- Sent utf8 encoded message: "dir(ucollections)\r" ----
dir(ucollections)
['__name__', 'namedtuple', 'OrderedDict']

import usocket
>>> 
---- Sent utf8 encoded message: "dir(usocket)\r" ----
dir(usocket)
['__name__', 'socket', 'getaddrinfo', 'inet_pton', 'inet_ntop', 'AF_INET', 'SOCK_TCP', 'SOCK_UDP', 'SOCK_SSL', 'IPPROTO_TCP', 'IPPROTO_UDP']

import ustruct
>>> 
---- Sent utf8 encoded message: "dir(ustruct)\r" ----
dir(ustruct)
['__name__', 'calcsize', 'pack', 'pack_into', 'unpack', 'unpack_from']

import utime
>>> 
---- Sent utf8 encoded message: "dir(utime)\r" ----
dir(utime)
['__name__', 'sleep', 'sleep_ms', 'sleep_us', 'ticks_ms', 'ticks_us', 'ticks_add', 'ticks_diff']

