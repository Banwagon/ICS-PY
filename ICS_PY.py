#!/usr/bin/env python3
#
import sys, time, os
from random import *
from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.exceptions import ConnectionException
#
# Declare Variables #
ipv4address = "192.168.1.20" # Standard Use
#ipv4address = "10.0.0.10" # Local IP for debug testing
registry = "3"
coil = "1"
registry_value = "0"
coil_value = "0"
port = "502"
readmin = 0
readmax = 16
#
## Clear screan
def clear_screen():
  clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
  clearConsole()
#
## Menu
def print_menu():
  clear_screen()
  print()
  print(8*'-','DSG Modbus Python Toolkit',8*'-')
  print()
  print('Current IP address: ',ipv4address)
  print()
  print('Current registry: ',registry)
  print()
  print('Current registry value: ',registry_value)
  print()
  print('Current coil: ',coil)
  print()
  print('Current Coil Value: ',coil_value)
  print()
  print('Current port: ',port)
  print()
  print(5*'-','Menu Options:',5*'-')
  print()
  print('1. Set Variables [IP, registry, coil, port]')
  print('2. Run Discovery (Coils, Registers, Direct Input)')
  print('3. Send Manual Register Value (1-100)')
  print('4. Send Random Register Value (70-100)')
  print('5. Force ON - (Registry @ 100 for 30s)')
  print('6. Force Off - (Registry @ 0 for 30s)')
  print('7. Send Coil Value (0 = Off, 1 = On)')
  print('8. Exit')
  print()
  print(43*'-')
  print()
#
## Settings Sub-Menu
def print_settings_menu():
  clear_screen()
  print()
  print(8*'-','DSG Modbus Python Toolkit',8*'-')
  print()
  print('Current IP address: ',ipv4address)
  print()
  print('Current registry: ',registry)
  print()
  print('Current registry value: ',registry_value)
  print()
  print('Current coil: ',coil)
  print()
  print('Current Coil Value: ',coil_value)  
  print()
  print('Current port: ',port)
  print()
  print(5*'-','Menu Options:',5*'-')
  print()
  print('1. Set All Variables?')
  print('2. Set IP Address')
  print('3. Set Registry Number')
  print('4. Set Coil Number')
  print('5. Set Coil Value')
  print('6. Set Port Number')
  print('7. Exit')
  print()
  print(43*'-')
  print()
#
## Set IPv4 address
def set_ipv4_address():
  global ipv4address
  while True:
    clear_screen()
    print_settings_menu()
    ipv4address=input('Please enter an IPv4 adderss, example - 192.168.1.20: ')
    if ipv4address!='' and ipv4address[0].lower() in ['0','1','2','3','4','5','6','7','8','9','.']:
      if ipv4address:
        print()
        print('-IPv4 address is now set to '+ipv4address)
        print()
        break
    else:
      print()
      print('-Entry cannot be blank and must contain a number')
      print()
      input('Press enter to continue...')
      print()
#
## Set registry
def set_registry():
  global registry
  while True:
    clear_screen()
    print_settings_menu()
    registry=input('Please enter a registry number, example - 3: ')
    if registry!='' and registry[0].lower() in ['0','1','2','3','4','5','6','7','8','9']:
      if registry:
        print()
        print('-Registry is now set to '+registry)
        print()
        break
    else:
      print()
      print('-Entry cannot be blank and must contain a number')
      print()
      input('Press enter to continue...')
      print()
#
## Set coil
def set_coil():
  global coil
  while True:
    clear_screen()
    print_settings_menu()
    coil=input('Please enter a coil number, example - 1: ')
    if coil!='' and coil[0].lower() in ['0','1','2','3','4','5','6','7','8','9']:
      if coil:
        print()
        print('-Coil is now set to '+coil)
        print()
        break
    else:
      print()
      print('-Entry cannot be blank and must contain a number')
      print()
      input('Press enter to continue...')
      print()
#
## Set Coil Value
def set_coil_value():
  global coil_value
  while True:
    clear_screen()
    print_settings_menu()
    coil_value=input('Please enter a binary coil value, example - 0 or 1: ')
    if coil_value!='' and coil_value[0].lower() in ['0','1']:
      if coil_value:
        print()
        print('-Coil value is now set to '+coil_value)
        print()
        break
    else:
      print()
      print('-Entry cannot be blank and must be in binary (0 or 1)')
      print()
      input('Press enter to continue...')
      print()
#
## Set port
def set_port():
  global port
  while True:
    clear_screen()
    print_settings_menu()
    port=input('Please enter a port number, example - 502: ')
    if port!='' and port[0].lower() in ['0','1','2','3','4','5','6','7','8','9']:
      if port:
        print()
        print('-Port number is now set to '+port)
        print()
        break
    else:
      print()
      print('-Entry cannot be blank and must contain a number')
      print()
      input('Press enter to continue...')
      print()
#
## Set value manual
def set_value_man():
  global registry_value
  client = ModbusClient(ipv4address, port)
  while True:
    clear_screen()
    print_menu()
    registry_value=input('Please enter a value, example - 0 - 100.  Press q to break: ')
    if registry_value=='q':
      registry_value='0'
      break
    if registry_value!='' and registry_value[0].lower() in ['-','0','1','2','3','4','5','6','7','8','9']:
      if int(registry_value)>=100:
        registry_value='100'
        print()
        print('Value cannot be greater than 100')
        client.connect()
        client.write_register(int(registry), int(registry_value))
        print()
        input('Press enter to continue...')
      else:
        client.connect()
        client.write_register(int(registry), int(registry_value))
        print()
    else:
      print()
      print('-Entry cannot be blank, must contain a number.  Press q to break')
      print()
      input('Press enter to continue...')
      print()
#
## Set value auto
def send_value_auto():
  global registry_value
  client = ModbusClient(ipv4address, port)
  while True:
    clear_screen()
    print_menu()
    random_value = randint(70, 100)
    registry_value=random_value
    client.connect()
    client.write_register(int(registry), int(registry_value))
    print()
    print('-Value is now '+str(random_value)+' .')
    print()
    q=input('Press enter to continue or q to break: ')
    if q:
      break
#
## Set Force Off
def send_force_off():
  global registry_value,break_time
  client = ModbusClient(ipv4address, port)
  registry_value=0
  break_time=0
  print()
  try:  
    #client.connect()
    while True:
      break_time+=1
      if break_time==30:break
      client.connect()
      client.write_register(int(registry), int(registry_value))
      time.sleep(1.1)
      print('Value is now '+str(registry_value)+", Ctrl+C to break or wait 30 seconds.")
      #value+=1
  except KeyboardInterrupt:
    pass
#
## Set Force On
def send_force_on():
  global registry_value,break_time
  client = ModbusClient(ipv4address, port)
  registry_value=100
  break_time=0
  #print()
  try:  
    #client.connect()
    while True:
      break_time+=1
      if break_time==30:break
      client.connect()
      client.write_register(int(registry), int(registry_value))
      time.sleep(1.1)
      print('Value is now '+str(registry_value)+", Ctrl+C to break or wait 30 seconds.")
  except KeyboardInterrupt:
    pass
#
## Discover Registers
def discover_registers():
  global ipv4address,port,readmax,readmin
  client = ModbusClient(ipv4address, port)
  while True:
    print ('\n*** Set min/max values for Coil discovey: ***')
    readint()
    readcoils = client.read_coils(int(readmin),int(readmax))
    print ('Reading from Coils...\n')
    print (readcoils)
    print ('\n*** Set min/max values for Register discovey: ***')
    readint()
    readregisters = client.read_holding_registers(int(readmin),int(readmax))
    print ('Reading from Registers...\n')
    print (readregisters)
    print ('\n*** Set min/max values for Discrete Input discovey: ***')
    readint()
    readdirectinputs = client.read_discrete_inputs(int(readmin),int(readmax))
    print ('Reading from Direct Outputs...\n')
    print (readdirectinputs)
    print()
    input('Press enter to continue...')
    print()
    break
#
## Error State
def send_coil_value():
  global coil_value,ipv4address,coil,port
  client = ModbusClient(ipv4address, port)
  while True:
    q=input('\n\nWARNING: Sending a value of 0 to Coil 1 will turn it off, placing the\nwall into an error state. This action forces a manual reset of the PLC.\n\n\nPress enter to continue or q to break: \n')
    if q:
      break
    client.connect()
    client.write_coil(int(coil), int(coil_value))
    print ('Coil value is now '+str(coil_value))
    print()
    input('Press enter to continue...')
    print()
    break

def readint():
  while True:
    readmin=input('\nPlease enter the minumum value for discovery, example - 1: ')
    if readmin!='' and readmin[0].lower() in ['0','1','2','3','4','5','6','7','8','9']:
      if readmin:
        print()
        print('-Minimum value for discovery is now set to '+readmin)
        print()
        break
    else:
      print()
      print('-Entry cannot be blank and must contain a number')
      print()
      input('Press enter to continue...')
      print()
  while True:
    readmax=input('Please enter the maximum value for discovery, example - 16: ')
    if readmax!='' and readmax[0].lower() in ['0','1','2','3','4','5','6','7','8','9']:
      if readmax:
        print()
        print('-Maximum number for discovery is now set to '+readmax)
        print()
        break
    else:
      print()
      print('-Entry cannot be blank and must contain a number')
      print()
      input('Press enter to continue...')
      print()
#
clear_screen()
loop=True
while loop:
  print_menu()
  choice=input('Enter your choice [1-8]: ')
  #
  # Item 1: Change Variables
  if choice==str(1):     
    #print()
    #print('-Set Variables [IP, registry, port] has been selected')
    loop2=True
    while loop2:
      # Clear screan
      clear_screen()
      print_settings_menu()
      choice=input('Enter your choice [1-7]:')
      if choice==str(1):
        print()
        # Call Set IPv4
        set_ipv4_address()
        # Call Set Registry
        set_registry()
        # Call Set Coil
        set_coil()
        # Call Set Coil Value
        set_coil_value()
        # Call Set Port
        set_port()
        break
      elif choice==str(2):
        print()
        # Call Set IPv4
        set_ipv4_address()
        break
      elif choice==str(3):
        print()
        # Call Set registry number
        set_registry()
        break
      elif choice==str(4):
        print()
        # Call Set coil number
        set_coil()
        break
      elif choice==str(5):
        print()
        # Call Set coil value
        set_coil_value()
        break      
      elif choice==str(6):
        print()
        # Call Set port number
        set_port()
        break
      elif choice==str(7):
        print()
        #print ('-Now exiting...')
        #print()            
        loop=False # This will make the while loop to end as not value of loop is set to False
        clear_screen()
      else:
        # Any integer inputs other than values 1-5 we print an error message
        print()
        input('Wrong option selection. Enter any key to try again..')
        clear_screen()
  #
  # Item 2: Discover Registers
  elif choice==str(2):
    print()
    print ('-Run Discovery has been selected')
    loop3=True
    while loop3:
      ## Call Discover Registers
      discover_registers()
      break  
  #
  # Item 3: Manually Set Value
  elif choice==str(3):
    print()
    print ('-Manualy Set Value has been selected')
    loop4=True
    while loop4:
      ## Call Set Manual Value
      set_value_man()
      break
  #
  # Item 4: Randomize Value
  elif choice==str(4):
    print()
    print ('-Randomly Set Value has been selected')
    ## Call Deploy Template
    send_value_auto()
  #
  # Item 5: Force On
  elif choice==str(5):
    print()
    print ('-Force on has been selected')
    ## Call Force On
    send_force_on()
  #
  # Item 6: Force Off
  elif choice==str(6):
    print()
    print ('-Force off has been selected')
    ## Call Force Off
    send_force_off()
  #     
  # Item 7: Coil Value
  elif choice==str(7):
    print()
    print ('-Send Coil Value has been selected')
    ## Call Force Off
    send_coil_value()
  # 
  # Item 8: Exit
  elif choice==str(8):
    print()
    #print ('-Now exiting...')
    #print()            
    loop=False # This will make the while loop to end as not value of loop is set to False
    clear_screen()
  else:
    # Any integer inputs other than values 1-5 we print an error message
    print()
    input('Wrong option selection. Enter any key to try again..')
    clear_screen()
  #
##############################################################################################

#ChangeLog
# (Line5) pymodbus.client.sync to pymodbus.client - Sync no longer required.
# Added print('2. Discover Registers') to menu, updated other numbers.
# Added coil value and menu item, settings submenu.
