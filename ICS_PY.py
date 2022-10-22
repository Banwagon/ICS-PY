#!/usr/bin/env python3

import sys, time, os
from random import *
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.exceptions import ConnectionException

#ip = sys.argv[1]
#registry = int(sys.argv[2])
#value = int(sys.argv[3])
#client = ModbusClient(ip, port=502)
#client.connect()
#client.write_register(registry, value)

# Declare Variables #
ipv4address = "192.168.1.20"
registry = "3"
value = "0"
port = "502"
#random_value = randint(1, 100)
client = ModbusClient(ipv4address, port)

## Clear screan
def clear_screen():
  clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
  clearConsole()

## Menu
def print_menu():
  clear_screen()
  print()
  print(8*'-','Modbus Python Toolkit',8*'-')
  print()
  print('Current IP address: ',ipv4address)
  print()
  print('Current registry: ',registry)
  print()
  print('Current port: ',port)
  print()
  print('Current value: ',value)
  print()
  print(5*'-','Menu Options:',5*'-')
  print()
  print('1. Set Variables [IP, registry, port]')
  print('2. Manualy Set Value')
  print('3. Randomly Set Value')
  print('4. Force ON')
  print('5. Force Off')
  print('6. Exit')
  print()
  print(50*'-')
  print()

## Set IPv4 address
def set_ipv4_address():
  global ipv4address
  while True:
    clear_screen()
    print_menu()
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

## Set registry
def set_registry():
  global registry
  while True:
    clear_screen()
    print_menu()
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

## Set port
def set_port():
  global port
  while True:
    clear_screen()
    print_menu()
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

## Set value manual
def set_value_man():
  global value
  #client.connect()
  while True:
    clear_screen()
    print_menu()
    value=input('Please enter a value, example - 0 - 100.  Press q to break: ')
    if value=='q':
      value='0'
      break
    if value!='' and value[0].lower() in ['-','0','1','2','3','4','5','6','7','8','9']:
      if int(value)>=100:
        value='100'
        print()
        print('Value cannot be greater than 100')
        client.connect()
        client.write_register(int(registry), int(value))
        print()
        input('Press enter to continue...')
      else:
        client.connect()
        client.write_register(int(registry), int(value))
        print()
    else:
      print()
      print('-Entry cannot be blank, must contain a number.  Press q to break')
      print()
      input('Press enter to continue...')
      print()

## Set value auto
def set_value_auto():
  global random_value,value,q
  #client.connect()
  while True:
    clear_screen()
    print_menu()
    random_value = randint(70, 100)
    value=random_value
    client.connect()
    client.write_register(int(registry), int(value))
    print()
    print('-Value is now '+str(random_value)+' .')
    print()
    q=input('Press enter to continue or q to break: ')
    if q:
      break

## Set Force Off
def set_force_off():
  global value,q,break_time
  value=0
  break_time=0
  print()
  try:  
    #client.connect()
    while True:
      break_time+=1
      if break_time==30:break
      client.connect()
      client.write_register(int(registry), int(value))
      time.sleep(1.1)
      print('Value is now '+str(value)+", Ctrl+C to break or wait 30 seconds.")
      #value+=1
  except KeyboardInterrupt:
    pass

## Set Force On
def set_force_on():
  global value,q,break_time
  value=100
  break_time=0
  #print()
  try:  
    #client.connect()
    while True:
      break_time+=1
      if break_time==30:break
      client.connect()
      client.write_register(int(registry), int(value))
      time.sleep(1.1)
      print('Value is now '+str(value)+", Ctrl+C to break or wait 30 seconds.")
  except KeyboardInterrupt:
    pass

clear_screen()
loop=True
while loop:
  print_menu()
  choice=input('Enter your choice [1-6]: ')
  #
  # Item 1: Change Variables
  if choice==str(1):     
    print()
    print('-Set Variables [IP, registry, port] has been selected')
    loop2=True
    while loop2:
      # Clear screan
      clear_screen()
      print_menu()
      print()
      # Call Set IPv4
      set_ipv4_address()
      # Call Set Registry
      set_registry()
      # Call Set Port
      set_port()
      break
  #
  # Item 2: Manually Set Value
  elif choice==str(2):
    print()
    print ('-Manualy Set Value has been selected')
    loop3=True
    while loop3:
      ## Call Set Manual Value
      set_value_man()
      break
  #
  # Item 3: Randomize Value
  elif choice==str(3):
    print()
    print ('-Randomly Set Value has been selected')
    ## Call Deploy Template
    set_value_auto()
  #
  # Item 4: Force On
  elif choice==str(4):
    print()
    print ('-Force on has been selected')
    ## Call Force On
    set_force_on()
  #
  # Item 4: Force Off
  elif choice==str(5):
    print()
    print ('-Force off has been selected')
    ## Call Force Off
    set_force_off()
  #     
  # Item 5: Exit
  elif choice==str(6):
    print()
    #print ('-Now exiting...')
    #print()            
    loop=False # This will make the while loop to end as not value of loop is set to False
    clear_screen()
  else:
    # Any integer inputs other than values 1-5 we print an error message
    print()
    input('Incorrect option selected. Enter any key to try again..')
    clear_screen()
  #
##############################################################################################
