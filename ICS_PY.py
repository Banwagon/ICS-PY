#!/usr/bin/env python3
#
import sys, time, os
from random import *
#from pymodbus.client import ModbusTcpClient as ModbusClient
#from pymodbus.exceptions import ConnectionException
from pyModbusTCP.client import ModbusClient
#
## Collored Text
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
ipv4address = "10.0.2.7" # Local IP for debug testing
port = "502"
unitId = "1" #unitId = slave number
registry = "0"
coil = "0"
registry_value = "0"
coil_value = "0"
readmin = 0
readmax = 16
client = ModbusClient(host=str(ipv4address), port=int(port), auto_open=True)
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
  print('9. '+RedAscii+'OPERATION: MISHAP'+ResetColor+' ('+YellowAscii+'Flood Coils and Registers with Random Values'+ResetColor+')')
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
  global ipv4address, client
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
        client = ModbusClient(host=str(ipv4address), port=int(port), auto_open=True)
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
  global port, client
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
        client = ModbusClient(host=str(ipv4address), port=int(port), auto_open=True)
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
  clear_screen()
  while True:
    #clear_screen()
    information_spash()
    print()
    print(RedAscii+48*'-'+ResetColor)
    print()
    registry_value=input('Please enter a value, example - '+YellowAscii+'0'+ResetColor+' - '+YellowAscii+'100'+ResetColor+'.  Enter q to break: ')
    if registry_value=='q':
      registry_value='0'
      break
    if registry_value!='' and registry_value[0].lower() in ['-','0','1','2','3','4','5','6','7','8','9']:
      if int(registry_value)>=100:
        registry_value='100'
        clear_screen()
        print()
        print('Value cannot be greater than '+YellowAscii+'100'+ResetColor)
        client.write_register(address=int(registry), value=int(registry_value), slave=int(unitId))
        print()
        input('Press enter to continue...')
      else:
        client.write_register(address=int(registry), value=int(registry_value), slave=int(unitId))
        print()
        print('Wrote value of '+YellowAscii+str(registry_value)+ResetColor+' to registry ['+CyanAscii+registry+ResetColor+']')
        time.sleep(2)
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
  timerDelay = 0
  while True:
    information_spash()
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
      random_value = randint(50, 100)
      registry_value = random_value
      client.write_register(address=int(registry), value=int(registry_value), slave=int(unitId))
      information_spash()
      print()
      print(RedAscii+48*'-'+ResetColor)
      print()
      print('- Wrote value of '+YellowAscii+str(random_value)+ResetColor+' to register ['+CyanAscii+registry+ResetColor+'], Ctrl+C to break.')
      print()
      for i in range(int(timerDelay)):
        time.sleep(1)
        sys.stdout.write(RedAscii+'.'+ResetColor)
        sys.stdout.flush()
  except KeyboardInterrupt:
    pass
  clear_screen()
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
      print('Value is now 0, Ctrl+C to break or wait 30 seconds.')
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
      print('Value is now 100, Ctrl+C to break or wait 30 seconds.')
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
  global coil_value,ipv4address,coil,port, unitId
  while True:
    q=input('\n'+RedAscii+'WARNING: '+ResetColor+YellowAscii+'Sending a value of 0 to a coil will turn it off and may result in manually reseting the PLC.'+ResetColor+'\n\nPress enter to continue or q to break: \n')
    if q:
      break
    client.write_coil(address=int(coil), value=int(coil_value), slave=int(unitId))
    print ('Wrote coil value '+YellowAscii+str(coil_value)+ResetColor+' on address ['+LightPurpleAscii+coil+ResetColor+'] to unit ['+CyanAscii+unitId+ResetColor+']')
    print()
    input('Press enter to continue...')
    print()
    break
  client.close
#
## Send Multiple Coil Values
def send_coils_values():
  global unitId, coil
  coil_length = ''
  try:
    while True:
      if int(len(coil_length))>10:
        coil_length = ''
        information_spash()
        print()
        print(CyanAscii+48*'-'+ResetColor)
        print()
        print('Coil length exceeds '+YellowAscii+'10'+ResetColor+' bits in length.')
        print()
        input('Press enter to continue...')
        print()  
      if int(len(coil_length))==10:
        information_spash()
        print()
        print(CyanAscii+48*'-'+ResetColor)
        print()
        print('Coil bits: '+YellowAscii+str(coil_length)+ResetColor)
        print()
        coil_max=input('Coil value equals '+YellowAscii+'10'+ResetColor+' bits in length, would you like to ['+CyanAscii+'r'+ResetColor+']eset or ['+CyanAscii+'c'+ResetColor+']ontinue? CTRL+C to break. ')
        if coil_max!='' and coil_max[0].lower() in ['r']:
          coil_length = ''
        if coil_max!='' and coil_max[0].lower() in ['c']:
          break
      information_spash()
      print()
      print(CyanAscii+48*'-'+ResetColor)
      print()
      print('Coil bits: '+YellowAscii+str(coil_length)+ResetColor)
      print()
      coil_number=input('Enter up to a '+YellowAscii+'10'+ResetColor+' bit coil value. Enter ['+YellowAscii+'c'+ResetColor+'] to continue, Ctrl+C to break: ')
      if coil_number!='' and coil_number[0].lower() in ['c']:
        client.write_coil(address=int(coil), value=int(coil_value), slave=int(unitId))
        #print ('Coil value is now '+str(coil_value))
        #print()
        #input('Press enter to continue...')
        #print()
        break
      if coil_number!='' and coil_number[0].lower() in ['0', '1']:
        coil_length += coil_number
      else:
        print()
        print('-Please enter a ['+YellowAscii+'1'+ResetColor+'] or ['+YellowAscii+'0'+ResetColor+']')
        print()
        input('Press enter to continue...')
        print()
    while True:
      information_spash()
      print()
      print(CyanAscii+48*'-'+ResetColor)
      print()
      client.write_coils(address=int(coil), values=tuple(map(int,coil_length)), slave=int(unitId))
      print ('Wrote coil value '+YellowAscii+str(coil_length)+ResetColor+' on address ['+LightPurpleAscii+coil+ResetColor+'] to unit ['+CyanAscii+unitId+ResetColor+']')    
      print()
      input('Press enter to continue...')
      print()
      break
  except KeyboardInterrupt:
    pass  
  client.close
#
## Flood all Servers with random values
#
def send_flood_values():
  global flood_speed, flood_speed_float, unitId_array
  print()
  try:
    unitId_array = []
    unitId_array.clear()
    while True:
      clear_screen()
      information_spash()
      main_menu()
      print(RedAscii+'WARNING: '+ResetColor)
      print()
      continue_flood=input(' This will flood random values registry and coil values for each unit selected. Please enter ['+YellowAscii+'Y'+ResetColor+']es to continue or ['+RedAscii+'N'+ResetColor+']o to break: ')
      if continue_flood!='' and continue_flood[0].lower() in ['n','o']:
        break
      if continue_flood!='' and continue_flood[0].lower() in ['y','e','s']:
        while True:
          information_spash()
          print()
          print(RedAscii+48*'-'+ResetColor)
          print()
          print('Current Array: '+str(unitId_array))
          print()
          unitId_number=input('Enter the unit numbers ('+YellowAscii+'one at a time'+ResetColor+') of the server devices you would like to flood. Enter ['+YellowAscii+'f'+ResetColor+'] to begin flood, Ctrl+C to break: ')
          if unitId_number!='' and unitId_number[0].lower() in ['f']:          
            break
          if unitId_number!='' and unitId_number[0].lower() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            unitId_array.append(unitId_number)   
        while True:
          information_spash()
          print()
          print(RedAscii+48*'-'+ResetColor)
          print()
          flood_speed=input('Enter flood speed: ')
          if flood_speed!='' and flood_speed[0].lower() in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            break
          else:
            print()
            print('-Please enter a valid number, example: ('+YellowAscii+'1'+ResetColor+') or ('+YellowAscii+'.5'+ResetColor+')')
            print()
            input('Press enter to continue...')
            print() 
        while True:
          coil_random = randint(0,9)
          coil_value_random = randint(0, 1)
          registry_random = randint(0, 4)
          registry_value_random = randint(1, 99)
          unitId_random = randint(0, (len(unitId_array))-1)
          unitId = unitId_array[unitId_random]
          client.write_register(address=int(registry_random), value=int(registry_value_random), slave=int(unitId))
          client.write_coil(address=int(coil_random), value=int(coil_value_random), slave=int(unitId))
          #time.sleep(1)
          time.sleep(float(flood_speed))
          print(str('Wrote value of ['+YellowAscii+str(coil_value_random)+ResetColor+']').ljust(29),str('on coil ['+CyanAscii+str(coil_random)+ResetColor+'] of unit number ['+LightPurpleAscii+unitId+ResetColor+']').rjust(54))
          print(str('Wrote value of ['+YellowAscii+str(registry_value_random)+ResetColor+']').ljust(29),str('on register ['+CyanAscii+str(registry_random)+ResetColor+'] of unit number ['+LightPurpleAscii+unitId+ResetColor+']').rjust(54))
      else:
        print()
        print('-Please enter [Yes] or [No]')
        print()
        input('Press enter to continue...')
        print()
  except KeyboardInterrupt:
    pass
  client.close
#
## MAIN ##
def main():
  clear_screen()
  while True:
    information_spash()
    main_menu()
    choice=input('Enter your choice [1-0]: ')
    #
    # Item 1: Change Variables
    if choice==str(1):     
      #print()
      #print('-Set Variables [IP, registry, port] has been selected')
      while True:
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
          #loop=False # This will make the while loop to end as not value of loop is set to False
          break
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
      time.sleep(1.5)
      while True:
        ## Call Discover Registers
        discover_registers()
        break  
    #
    # Item 3: Manually Set Value
    elif choice==str(3):
      print()
      print ('-Manualy Set Value has been selected')
      time.sleep(1.5)
      while True:
        ## Call Set Manual Value
        set_value_man()
        #break
    #
    # Item 4: Randomize Value
    elif choice==str(4):
      print()
      print ('-Randomly Set Value has been selected')
      time.sleep(1.5)
      ## Call Deploy Template
      while True:
        send_value_auto()
        break
    #
    # Item 5: Force On
    elif choice==str(5):
      print()
      print ('-Force on has been selected')
      time.sleep(1.5)
      ## Call Force On
      while True:
        send_force_on()
        break
    #
    # Item 6: Force Off
    elif choice==str(6):
      print()
      print ('-Force off has been selected')
      time.sleep(1.5)
      ## Call Force Off
      while True:
        send_force_off()
        break
    #     
    # Item 7: Coil Value
    elif choice==str(7):
      print()
      print ('-Send Coil Value has been selected')
      time.sleep(1.5)
      ## Call Coil Values
      while True:
        send_coil_value()
        break
    # 
    # Item 8: Coils Value
    elif choice==str(8):
      print()
      print ('-Send Coil Values has been selected')
      time.sleep(1.5)
      ## Call Force Off
      while True:
        send_coils_values()
        break
    # 
    # Item 9: Flood Values
    elif choice==str(9):
      print()
      print ('-Flood Values has been selected')
      time.sleep(1.5)
      ## Call Send Flood Values
      while True:
        send_flood_values()
        break
    # 
    # Item 10: Exit
    elif choice==str(0):
      print()
      print ('-Now exiting...')
      time.sleep(1.5)           
      break # This will make the while loop to end as not value of loop is set to False
    else:
      # Any integer inputs other than values 1-5 we print an error message
      print()
      input('Wrong option selection. Enter any key to try again..')
      clear_screen()
    #
#
if __name__ == "__main__":
  main()
#
##############################################################################################

#ChangeLog
# (Line5) pymodbus.client.sync to pymodbus.client - Sync no longer required.
# Added print('2. Discover Registers') to menu, updated other numbers.
# Added coil value and menu item, settings submenu.
# 7.12.2023 - Massive changes implemented, refer to git for differences.
