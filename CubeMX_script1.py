Import("env")
import os

env.Prepend(CCFLAGS=[
  "-IFreeModbus/port",
  "-IFreeModbus/modbus/include",
  "-IFreeModbus/modbus/rtu"
])
modbusfiles = [
  os.path.join("$BUILD_SRC_DIR",  "./FreeModbus/modbus/mb_m.c"),
  os.path.join("$BUILD_SRC_DIR",  "./FreeModbus/modbus/rtu/mbcrc.c"),
  os.path.join("$BUILD_SRC_DIR",  "./FreeModbus/modbus/rtu/mbrtu_m.c"),
  os.path.join("$BUILD_SRC_DIR",  "./FreeModbus/modbus/functions/mbfuncother.c"),
  os.path.join("$BUILD_SRC_DIR",  "./FreeModbus/modbus/functions/mbfuncinput_m.c"),
  os.path.join("$BUILD_SRC_DIR",  "./FreeModbus/modbus/functions/mbutils.c"),
  os.path.join("$BUILD_SRC_DIR",  "./FreeModbus/port/rtt/port.c"),
  os.path.join("$BUILD_SRC_DIR",  "./FreeModbus/port/rtt/portevent_m.c"),
  os.path.join("$BUILD_SRC_DIR",  "./FreeModbus/port/rtt/portserial_m.c"),
  os.path.join("$BUILD_SRC_DIR",  "./FreeModbus/port/rtt/porttimer_m.c"),
]
env.Append(PIOBUILDFILES= modbusfiles)

