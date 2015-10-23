#echo off
#set PATH_PYTHON="C:\Python27\python.exe"
#set PATH_SCRIPT_PY="c:\Users\jzavala\Documents\code\ArduinostandAlone\create_compilation_recipe.py"
#%PATH_PYTHON% %PATH_SCRIPT_PY%
#pause

import os
#files to compile with avr-g++
PATH_AVR_COMPILER="C:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\tools\\avr\\bin\\"
OUTPUT_PATH=" C:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\out\\"
INCLUDE_PATH_0=" -IC:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino"
INCLUDE_PATH_1=" -IC:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\variants\\eightanaloginputs"
COMPI_FLAGS_AVRGPP=" -c -g -Os -w -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -MMD -mmcu=atmega328p -DF_CPU=16000000L -DARDUINO=10605 -DARDUINO_AVR_MINI -DARDUINO_ARCH_AVR"
COMPI_FLAGS_AVRGCC=" -c -g -Os -w -ffunction-sections -fdata-sections -MMD -mmcu=atmega328p -DF_CPU=16000000L -DARDUINO=10605 -DARDUINO_AVR_MINI -DARDUINO_ARCH_AVR"
COMPI_FLAGS_AVRASM=" -c -g -x assembler-with-cpp -mmcu=atmega328p -DF_CPU=16000000L -DARDUINO=10605 -DARDUINO_AVR_MINI -DARDUINO_ARCH_AVR"

files_to_compile_with_avrgpp=[
" c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\main.cpp",
" c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\abi.cpp",
" c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\CDC.cpp",
" c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\HardwareSerial.cpp",
" c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\HardwareSerial0.cpp",
" c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\HardwareSerial1.cpp",
" c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\HardwareSerial2.cpp",
" c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\HardwareSerial3.cpp",
" c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\HID.cpp",
" c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\IPAddress.cpp",
" c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\new.cpp",
" c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\Print.cpp",
" c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\Stream.cpp",
" c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\Tone.cpp",
" c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\USBCore.cpp",
" c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\WMath.cpp",
" c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\WString.cpp",
]
files_to_compile_with_avrgcc=[
"c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\hooks.c",
"c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\WInterrupts.c",
"c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\wiring.c",
"c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\wiring_analog.c",
"c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\wiring_digital.c",
"c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\wiring_pulse.c",
"c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\wiring_shift.c",
]
files_to_compile_with_avrgcc_assembler=[
"c:\\Users\\jzavala\\Documents\\code\\ArduinostandAlone\\hardware\\arduino\\avr\\cores\\arduino\\wiring_pulse.S",
]
"""
for item in files_to_compile_with_avrgpp:
	full_path = item.split("\\")
	filename =full_path[-1]
	print PATH_AVR_COMPILER+"avr-g++.exe"+COMPI_FLAGS_AVRGPP,
	print INCLUDE_PATH_0+INCLUDE_PATH_1,
	print item,
	print " -o "+OUTPUT_PATH+filename+".o"
	
for item in files_to_compile_with_avrgcc:
	full_path = item.split("\\")
	filename =full_path[-1]
	print PATH_AVR_COMPILER+"avr-gcc.exe"+COMPI_FLAGS_AVRGCC,
	print INCLUDE_PATH_0+INCLUDE_PATH_1,
	print item,
	print " -o "+OUTPUT_PATH+filename+".o"	
	
for item in files_to_compile_with_avrgcc_assembler:
	full_path = item.split("\\")
	filename =full_path[-1]
	print PATH_AVR_COMPILER+"avr-gcc.exe"+COMPI_FLAGS_AVRASM,
	print INCLUDE_PATH_0+INCLUDE_PATH_1,
	print item,
	print " -o "+OUTPUT_PATH+filename+".o"	
print "pause"

