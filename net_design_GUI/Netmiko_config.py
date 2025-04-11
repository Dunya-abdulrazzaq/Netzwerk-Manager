from netmiko import ConnectHandler
import json
import time
from netmiko import file_transfer
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def execute(device, command_list):  # open ssh connection and execute command
    try:
        net_connect = ConnectHandler(**device)
        net_connect.enable()  # entering the enable mode
        output = net_connect.send_config_set(command_list)
        print(output)
        print(f'connection to Host{host} will be disconnect')
        net_connect.disconnect()
    except:
        print(f'\n the Host {device} is DOWN!!\n')


def report(command: str):
    end_name = command.replace(' ', '_')  # give name to the report from the show comand

    report = ''
    json_file = filedialog.askopenfilename(title='wählen Sie den json File,mit Device Liste ,aus', initialdir='.')
    with open(json_file, 'r') as f:
        device_list = json.load(f)
    for item in device_list:
        host = item['host']
        print(f'connecting to Host {host}')
        try:
            net_connect = ConnectHandler(**item)
            net_connect.enable()  # entering the enable mode
            output = net_connect.send_command(command, )  # use_textfsm=True,
            print(output)
            filename = f'{host}_{end_name}.txt'
            with open(filename, 'w') as f:  # # saving the outputs to files
                f.write(output)

            print(f'connection to Host{host} will be disconnect')
            net_connect.disconnect()
            report = report + f'\n \n  Report Output from Host  {host}  for {end_name}Command \n \n ' + output
        except:
            print(f'\n the Host {host} is DOWN!!\n')

    print(report)

    return report


def core_Sw():  # for Core Layer Switch
    core_sw = filedialog.askopenfilename(title='wählen Sie den Configuration txt Datei für Ihre Core Switches aus',
                                         initialdir='.')
    with open(core_sw) as f:
        co_lines = f.read().splitlines()  # read the command as list
    print(co_lines)
    json_file = filedialog.askopenfilename(title='wählen Sie den json File,mit Device Liste ,aus', initialdir='.')
    with open(json_file, 'r') as f:
        core_sw_list = json.load(f)
    for item in core_sw_list:
        host = item['host']
        print(f'connecting to Host {host}  ')
        execute(item, co_lines)


def dist_Sw():  # for Distribution Layer Switch
    dist_sw = filedialog.askopenfilename(
        title='wählen Sie den Configuration txt Datei für Ihre Distribution Layer Switches aus', initialdir='.')
    with open(dist_sw) as f:
        dis_lines = f.read().splitlines()  # read the command as list
    print(dis_lines)
    json_file = filedialog.askopenfilename(title='wählen Sie den json File,mit Device Liste ,aus', initialdir='.')
    with open(json_file, 'r') as f:
        dist_sw_list = json.load(f)
        for item in dist_sw_list:
        host = item['host']
        print(f'connecting to Host {host}  ')
        execute(item, dis_lines)


def acc_Sw():  # for Acess Layer Switch
    acces_sw = filedialog.askopenfilename(
        title='wählen Sie den Configuration txt Datei für Ihre Access Layer Switches aus', initialdir='.')
    with open(acces_sw) as f:
        acc_lines = f.read().splitlines()  # read the command as list
    print(acc_lines)
    json_file = filedialog.askopenfilename(title='wählen Sie den json File,mit Device Liste ,aus', initialdir='.')
    with open(json_file, 'r') as f:
        acc_sw_list = json.load(f)
    for item in acc_sw_list:
        host = item['host']
        print(f'connecting to Host {host}  ')
        execute(item, acc_lines)


def list_Sw():  # for Switch from list with Management IP
    json_file = filedialog.askopenfilename(title='wählen Sie den json File,mit Device Liste ,aus', initialdir='.')
    with open(json_file, 'r') as f:
        dev_list = json.load(f)
    for item in dev_list:
        host = item['host']
        print(f'connecting to Host {host}  ')
        ask = messagebox.askquestion(message='wollen Sie die Configuration file für jede Device auswählen.dann "Yes", oder lassen Sie das Programm Ihre vorhierige vorbeireitet Files(mit host Ip als Name,z.b 192.168.52.120.cfg verwenden`,dann
        with open(f'{host}.txt') as f:
            list_lines = f.read().splitlines()  ## read the command as list
            print(list_lines)
        execute(item, list_lines)


def scp_file_transfer():
    json_file = filedialog.askopenfilename(title='wählen Sie den json File,mit Device Liste ,aus', initialdir='.')
    with open(json_file, 'r') as f:
        dev_list = json.load(f)
    for item in dev_list:
        host = item['host']
        sourcefile = input('enter the Source File Name(with path,in Case it is in another directory) :\n >>')
        destinationfile = input('enter the destination File Name :\n >>')
        filesystem = input('enter the destination File system (z.b flash2: or disck1: :\n >>')
        try:
            print(f'connecting to Host {host} and transfer file ')
            net_connect = ConnectHandler(**item)  # connect to device uber ssh
            transfer = file_transfer(net_connect, source_file=sourcefile, dest_file=destinationfile,
                                     file_system=filesystem, direction='put',
                                     overwrite_file=True, )  # scp identifacation
            print(transfer)
            print(f'connection to Host{host} will be disconnect')
            net_connect.disconnect()

        except:
            print(f'\n the Host {host} is DOWN!!\n')
