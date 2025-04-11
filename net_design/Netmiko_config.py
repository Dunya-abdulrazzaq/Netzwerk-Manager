from netmiko import ConnectHandler
import json
import time
from netmiko import file_transfer

def execute(device, command_list):#open ssh connection and execute command
    try:
        net_connect = ConnectHandler(**device)
        net_connect.enable() # entering the enable mode
        output = net_connect.send_config_set(command_list)
        print(output)
        print(f'connection to Host{host} will be disconnect')
        net_connect.disconnect()
    except:
        print(f'\n the Host {device} is DOWN!!\n')
def report(command:str):
    end_name =command.replace(' ','_')#give name to the report from the show comand
    with open('report_to_device.json', 'r') as f:
        device_list = json.load(f)
    for item in device_list:
        host = item['host']
        print(f'connecting t Host {host}')
        try:
            net_connect = ConnectHandler(**item)
            net_connect.enable()  # entering the enable mode
            output = net_connect.send_command(command, use_textfsm=True)
            print(output)
            filename = f'{host}_{end_name}.txt'
            with open(filename, 'w') as f:  # # saving the outputs to files
                f.write(output)
            print(f'connection to Host{host} will be disconnect')
            net_connect.disconnect()
        except :
            print(f'\n the Host {host} is DOWN!!\n')

def core_Sw(): #for Core Layer Switch
    with open('core_sw_command.txt') as f:
        co_lines = f.read().splitlines()# read the command as list
    print(co_lines)
    with open('cor_sw_device.json', 'r') as f:
        core_sw_list = json.load(f)
    for item in core_sw_list:
        host = item['host']
        print(f'connecting to Host {host}  ')
        execute(item,co_lines)

def dist_Sw(): # for Distribution Layer Switch
    with open('dist_sw_command.txt') as f:
        dis_lines = f.read().splitlines()# read the command as list
    print(dis_lines)
    with open('dist_sw_device.json', 'r') as f:
        dist_sw_list = json.load(f)
    for item in dist_sw_list:
        host = item['host']
        print(f'connecting to Host {host}  ')
        execute(item, dis_lines)

def acc_Sw(): #for Acess Layer Switch
    with open('acc_sw_command.txt') as f:
        acc_lines = f.read().splitlines()# read the command as list
    print(acc_lines)
    with open('acc_sw_device.json', 'r') as f:
        acc_sw_list = json.load(f)
    for item in acc_sw_list:
        host = item['host']
        print(f'connecting to Host {host}  ')
        execute(item,acc_lines)

def list_Sw(): #for Switch from list with Management IP
     with open('list_device_net.json', 'r') as f:
        dev_list = json.load(f)
     for item in dev_list :
         host=item['host']
         print(f'connecting to Host {host}  ')
         with open(f'{host}.txt') as f:
            list_lines = f.read().splitlines()## read the command as list
            print(list_lines)
         execute(item,list_lines)

def scp_file_transfer():
    with open('list_device_net.json', 'r') as f:
        dev_list = json.load(f)
    for item in dev_list:
        host = item['host']
        sourcefile=input('enter the Source File Name(with path,in Case it is in another directory) :\n >>')
        destinationfile = input('enter the destination File Name :\n >>')
        filesystem=input('enter the destination File system (z.b flash2: or disck1: :\n >>')
        try:
            print(f'connecting to Host {host} and transfer file ')
            net_connect = ConnectHandler(**item)# connect to device uber ssh
            transfer = file_transfer(net_connect,source_file=sourcefile,dest_file=destinationfile,file_system=filesystem,direction='put',overwrite_file=True, )#scp identifacation
            print(transfer)
            print(f'connection to Host{host} will be disconnect')
            net_connect.disconnect()

        except :
            print(f'\n the Host {host} is DOWN!!\n')




