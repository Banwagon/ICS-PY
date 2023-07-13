#!/usr/bin/env python3
#
import sys, time, os
from random import *
from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.exceptions import ConnectionException
#
## Collored Text
#def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
#def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
#def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
#def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
#def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
#def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
#def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
#def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
RedAscii = "\033[91m"
GreenAscii = "\033[92m"
YellowAscii = "\033[93m"
LightPurpleAscii = "\033[94m"
PurpleAscii = "\033[95m"
CyanAscii = "\033[96m"
LightGreyAscii = "\033[97m"
BlackAscii = "\033[98m"
ResetColor = "\033[00m"
#
# Declare Variables #
#ipv4address = "192.168.1.20" # Standard Use
ipv4address = "10.0.3.5" # Local IP for debug testing
port = "502"
unitId = "0" #unitId = slave number
registry = "0"
coil = "0"
registry_value = "0"
coil_value = "0"
readmin = 0
readmax = 16
address = 'address='+registry
value = 'value='+registry_value
slave = 'slave='+unitId
#
##
client = ModbusClient(host=str(ipv4address), port=int(port), autoopen=True, debug=False)
#
## Clear screan
def clear_screen():
  clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
  clearConsole()
#
## Information Spashscreen
def information_spash():
  clear_screen()
  print(RedAscii+12*'-'+' '+'Modbus Python Toolkit'+' '+12*'-'+ResetColor)
  print()
  print('Server IP: ',YellowAscii+str(ipv4address)+ResetColor)
  print('---- Port: ',CyanAscii+str(port)+ResetColor)
  print('- Unit_ID: ',LightPurpleAscii+str(unitId)+ResetColor)
  print()
  print('Current registry: ',YellowAscii+str(registry)+ResetColor)
  print('- Registry value: ',GreenAscii+str(registry_value)+ResetColor)
  print()
  print('Current coil: ',YellowAscii+str(coil)+ResetColor)
  print('- Coil Value: ',GreenAscii+str(coil_value)+ResetColor)
#
## Main Menu
def main_menu():
  print()
  print(16*'-',CyanAscii+'Menu Options:'+ResetColor,16*'-')
  print()
  print('1. Set Variables ['+YellowAscii+'IP, PORT, UNIT_ID, REGISTRY, COIL'+ResetColor+']')
  print('2. Run Discovery ['+YellowAscii+'REGISTERS, COILS'+ResetColor+']')
  print('3. Write Register Value ('+YellowAscii+'1-100'+ResetColor+')')
  print('4. Write Random Register Value ('+YellowAscii+'50-100'+ResetColor+')')
  print('5. Force ON - (write.register='+YellowAscii+'100'+ResetColor+' for '+CyanAscii+'30'+ResetColor+'s)')
  print('6. Force Off - (write.register='+YellowAscii+'0'+ResetColor+' for '+CyanAscii+'30'+ResetColor+'s)')
  print('7. Write Coil Value ('+RedAscii+'0'+ResetColor+' = Off, '+GreenAscii+'1'+ResetColor+' = On)')
  print('8. Write Multiple Coil Values ('+RedAscii+'0'+ResetColor+' = Off, '+GreenAscii+'1'+ResetColor+' = On)')
  print('9. Flood Coils and Registers with Random Values')
  print('0. Exit')
  print()
  print(48*'-')
  print()
#
## Variables Sub-Menu
def variable_settings_menu():
  print()
  print(16*'-',CyanAscii+'Menu Options:'+ResetColor,16*'-')
  print()
  print('1. Set All Variables?')
  print('2. Set IP Address')
  print('3. Set Port Number')
  print('4. Set UnitId')        
  print('5. Set Registry Number')
  print('6. Set Coil Number')
  print('7. Set Coil Value')
  print('8. Exit')
  print()
  print(48*'-')
  print()
#
## Set IPv4 address
def set_ipv4_address():
  global ipv4address
  while True:
    clear_screen()
    information_spash()
    print()
    print(48*'-')
    print()
    ipv4address=input('Please enter an IPv4 adderess, example - '+YellowAscii+'192.168.1.20'+ResetColor+': ')
    if ipv4address!='' and ipv4address[0].lower() in ['0','1','2','3','4','5','6','7','8','9','.']:
      if ipv4address:
        print()
        print('-IPv4 address is now set to '+YellowAscii+ipv4address+ResetColor)
        print()
        time.sleep(1.5)
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
    information_spash()
    print()
    print(48*'-')
    print()
    port=input('Please enter a port number, example - '+YellowAscii+'502'+ResetColor+': ')
    if port!='' and port[0].lower() in ['0','1','2','3','4','5','6','7','8','9']:
      if port:
        print()
        print('-Port number is now set to '+YellowAscii+port+ResetColor)
        print()
        time.sleep(1.5)
        break
    else:
      print()
      print('-Entry cannot be blank and must contain a number')
      print()
      input('Press enter to continue...')
      print()
#
## Set unitId
def set_unitId():
  global unitId
  while True:
    clear_screen()
    information_spash()
    print()
    print(48*'-')
    print()
    unitId=input('Please enter a server number, example - '+YellowAscii+'2'+ResetColor+': ')
    if unitId!='' and unitId[0].lower() in ['0','1','2','3','4','5','6','7','8','9']:
      if unitId:
        print()
        print('-UnitId is now set to '+YellowAscii+unitId+ResetColor)
        print()
        time.sleep(1.5)
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
    information_spash()
    print()
    print(48*'-')
    print()
    registry=input('Please enter a registry number, example - '+YellowAscii+'3'+ResetColor+': ')
    if registry!='' and registry[0].lower() in ['0','1','2','3','4','5','6','7','8','9']:
      if registry:
        print()
        print('-Registry is now set to '+YellowAscii+registry+ResetColor)
        print()
        time.sleep(1.5)
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
    information_spash()
    print()
    print(48*'-')
    print()
    coil=input('Please enter a coil number, example - '+YellowAscii+'1'+ResetColor+': ')
    if coil!='' and coil[0].lower() in ['0','1','2','3','4','5','6','7','8','9']:
      if coil:
        print()
        print('-Coil is now set to '+YellowAscii+coil+ResetColor)
        print()
        time.sleep(1.5)
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
    information_spash()
    print()
    print(48*'-')
    print()
    coil_value=input('Please enter a binary coil value, example - '+YellowAscii+'0'+YellowAscii+' or '+YellowAscii+'1'+ResetColor+': ')
    if coil_value!='' and coil_value[0].lower() in ['0','1']:
      if coil_value:
        print()
        print('-Coil value is now set to '+YellowAscii+coil_value+ResetColor)
        print()
        time.sleep(1.5)
        break
    else:
      print()
      print('-Entry cannot be blank and must be in binary ('+YellowAscii+'0'+ResetColor+' or '+YellowAscii+'1'+ResetColor+')')
      print()
      input('Press enter to continue...')
      print()
#
## Set value manual
def set_value_man():
  global client, registry_value, unitId
  while True:
    clear_screen()
    information_spash()
    registry_value=input('Please enter a value, example - 0 - 100.  Press q to break: ')
    if registry_value=='q':
      registry_value='0'
      break
    if registry_value!='' and registry_value[0].lower() in ['-','0','1','2','3','4','5','6','7','8','9']:
      if int(registry_value)>=100:
        registry_value='100'
        print()
        print('Value cannot be greater than 100')
        client.write_register(address=int(registry), count=int(registry_value), slave=(unitId))
        print()
        input('Press enter to continue...')
      else:
        client.write_register(address=int(registry), count=int(registry_value), slave=(unitId))
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
  global client, registry_value, registry, unitId
  clear_screen()
  information_spash()
  timerDelay = 0
  while True:
    print()
    print(RedAscii+48*'-'+ResetColor)
    timerDelay=input('\nPlease enter the timer delay in seconds, example - '+YellowAscii+'3'+ResetColor+': ')
    if timerDelay!='' and timerDelay[0].lower() in ['0','1','2','3','4','5','6','7','8','9']:
      if timerDelay:
        print()
        print('-Timer delay set to '+YellowAscii+timerDelay+ResetColor+' seconds')
        print()
        time.sleep(1.5)
        break
    else:
      print()
      print('-Entry cannot be blank and must contain a number')
      print()
      input('Press enter to continue...')
      print()
  try:
    while True:
      clear_screen()
      random_value = randint(50, 100)
      registry_value = random_value
      client.write_register(address=int(registry), value=int(registry_value), slave=int(unitId))
      information_spash()
      print()
      print(RedAscii+48*'-'+ResetColor)
      print()
      print('- Value is now '+YellowAscii+str(random_value)+ResetColor+', Ctrl+C to break.')
      print()
      for i in range(int(timerDelay)):
        time.sleep(1)
        sys.stdout.write(RedAscii+'.'+ResetColor)
        sys.stdout.flush()
      #time.sleep(int(timerDelay))
  except KeyboardInterrupt:
    pass  
  client.close
#
## Set Force Off
def send_force_off():
  global client, break_time
  information_spash()
  break_time=0
  print()
  try:  
    while True:
      break_time+=1
      if break_time==30:break
      client.write_register(address=int(registry), value=int(0), slave=int(unitId))
      time.sleep(1.1)
      print('Value is now '+str(registry_value)+", Ctrl+C to break or wait 30 seconds.")
  except KeyboardInterrupt:
    pass
  client.close
#
## Set Force On
def send_force_on():
  global client, registry_value, break_time
  information_spash()
  break_time=0
  try:  
    while True:
      break_time+=1
      if break_time==30:break
      client.write_register(address=int(registry), value=int(100), slave=int(unitId))
      time.sleep(1.1)
      print('Value is now '+str(registry_value)+", Ctrl+C to break or wait 30 seconds.")
  except KeyboardInterrupt:
    pass
#
## Discover Registers
def discover_registers():
  global client, ipv4address, port, readmax, readmin
  information_spash()
  while True:
    print()
    print(CyanAscii+48*'-'+ResetColor)
    print()
    readcoils = client.read_coils(address=int(0), count=int(10), slave=int(unitId))
    print (YellowAscii+'Reading from Coils...\n'+ResetColor)
    coil_booleans = readcoils.bits
    coil_boolean_to_int_conversion = [int(item) for item in coil_booleans]
    print(coil_boolean_to_int_conversion)
    print()
    print(CyanAscii+48*'-'+ResetColor)
    print()
    readregisters = client.read_holding_registers(address=int(0), count=int(5), slave=int(unitId))
    print (YellowAscii+'Reading from Registers...\n'+ResetColor)
    print (readregisters.registers)
    print()
    input('Press enter to continue...')
    print()
    break
#
## Error State
def send_coil_value():
  global coil_value,ipv4address,coil,port
  #client = ModbusClient(ipv4address, port)
  #client.connect()
  while True:
    q=input('\n'+RedAscii+'WARNING: '+ResetColor+YellowAscii+'Sending a value of 0 to a coil will turn it off and may result in manually reseting the PLC.'+ResetColor+'\n\nPress enter to continue or q to break: \n')
    if q:
      break
    client.write_coil(address=int(coil), value=int(coil_value), slave=int(unitId))
    print ('Coil value is now '+str(coil_value))
    print()
    input('Press enter to continue...')
    print()
    break
  client.close
#
## Send Multiple Coil Values
def send_coils_values():
  print()
#
## Flood all Servers with values
#
def send_flood_values():
  print()
#
## MAIN ##
def main():
  clear_screen()
  loop=True
  while loop:
    information_spash()
    main_menu()
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
        information_spash()
        variable_settings_menu()
        choice=input('Enter your choice [1-8]: ')
        if choice==str(1):
          print()
          # Call Set IPv4
          set_ipv4_address()
          # Call Set Port
          set_port()
          # Call Set UnitID
          set_unitId()
          # Call Set Registry
          set_registry()
          # Call Set Coil
          set_coil()
          # Call Set Coil Value
          set_coil_value()
          break
        elif choice==str(2):
          print()
          # Call Set IPv4
          set_ipv4_address()
          break
        elif choice==str(3):
          print()
          # Call Set port number
          set_port()
          break
        elif choice==str(4):
          print()
          # Call Set port number
          set_unitId()
          break            
        elif choice==str(5):
          print()
          # Call Set registry number
          set_registry()
          break
        elif choice==str(6):
          print()
          # Call Set coil number
          set_coil()
          break
        elif choice==str(7):
          print()
          # Call Set coil value
          set_coil_value()
          break      
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
      ## Call Coil Values
      send_coil_value()
    # 
    # Item 8: Coils Value
    elif choice==str(8):
      print()
      print ('-Send Coil Values has been selected')
      ## Call Force Off
      send_coils_values()
    # 
    # Item 9: Flood Values
    elif choice==str(9):
      print()
      print ('-Flood Values has been selected')
      ## Call Send Flood Values
      send_flood_values()
    # 
    # Item 10: Exit
    elif choice==str(0):
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

if __name__ == "__main__":
  main()

##############################################################################################

#ChangeLog
# (Line5) pymodbus.client.sync to pymodbus.client - Sync no longer required.
# Added print('2. Discover Registers') to menu, updated other numbers.
# Added coil value and menu item, settings submenu.
# 7.12.2023 - Massive changes implemented, refer to git for differences.