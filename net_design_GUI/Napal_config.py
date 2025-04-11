import getpass
import json
import time
from napalm import get_network_driver
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

def open_connection(host, user, password, secret, net_driver, optional_args):# the Connection Bau to the Device
    if user != ' ':
        pass
    else:
        user=simpledialog.askstring('User Name',f'enter User name for {host}:')
        #user = input(f'enter User name for {host}:\n>>')
    if password != ' ':
        pass
    else:
        password =simpledialog.askstring('Password',f'bitte enter user {user} Password :', show='*')
            #getpass.getpass(prompt=f'bitte enter user {user} Password :\n >>'))

    if secret != ' ':
        pass
    else:
        secret = simpledialog.askstring(f'bitte enter Enable Password for Host {host} :', show='*')
            #getpass.getpass(prompt=f'bitte enter Enable Password for Host {host} :\n >>'))

    driver = get_network_driver(net_driver)  # Driver used for different modell& network Venders ,(z.b with meistens cisco sw und router  is 'ios' ,there is also 'ios-xr'&'nx-os' )
    device_ios = driver(host, user, password,optional_args=optional_args)  # api or ssh(bei ios) connection to the device
    device_ios.open()
    return device_ios
def replace_config():
    #ask the user if he want to give the file from openBox or select the file according to hostIp
    ask=messagebox.askquestion(message='wollen Sie die Configuration file für jede Device auswählen.dann "Yes", oder lassen Sie das Programm Ihre vorhierige vorbeireitet Files(mit host Ip als Name,z.b 192.168.52.120.cfg verwenden`,dann "No"')
    json_file = filedialog.askopenfilename(title='wählen Sie den json File,mit Device Liste ,aus',initialdir='.')  # ,filetypes=("Json File","*.json")
    with open(json_file, 'r') as f: # open the Device list
        user_data = json.load(f)
    for item in user_data:#read the information for each device
        host = item['host']
        user = item['username']
        password = item['password']
        secret = item['secret']
        net_driver = item['net_driver']
        optional_args = {'secret': secret}
        #messagebox.showinfo(message=f'connecting to Host{host}')
        print(f'\n connecting to Host{host}')
        device_ios = open_connection(host, user, password, secret, net_driver, optional_args)
        if ask =='yes':
            filename = filedialog.askopenfilename(title='wählen Sie den Configuration File aus')#,filetypes='*.*'
        elif ask == 'no':
            filename=f'{host}_new.cfg'

        print('applied the new configuration')
        #messagebox.showinfo('applied the new configuration')

        device_ios.load_replace_candidate(filename) #process to replace the configuration from Napalm
        diffrent = device_ios.compare_config()  # compare the new configuration with the old one
        if len(diffrent) > 0:
            print('die neue Konfiguration ist : \n>> ')
            print(diffrent)
            while True:
                answer = messagebox.askquestion(message='Wollen Sie diese neue Konfiguration bestigegen(commit Configuration),bei ja drucken Sie yes bei neine drucken Sie no: \n >>')
                if answer == 'yes':
                    device_ios.commit_config()
                    # print(device_ios.has_pending_commit())
                    # device_ios.confirm_commit()
                    time.sleep(10)
                    print('Done,the configuration is committed')
                    break
                elif answer == 'no':
                    device_ios.discard_config()
                    break

        print(f'disconnecting from Host{host}...')
        #messagebox.showinfo(message=f'disconnecting from Host{host}...')
        device_ios.close()
    quit()


def merge_config():
    # ask the user if he want to give the file from openBox or select the file according to hostIp
    ask = messagebox.askquestion(message='wollen Sie die Configuration file für jede Device auswählen.dann  "Yes", oder lassen Sie das Program Ihre vorhierige vorbeireitet Files(mit host Ip als Name,z.b 192.168.52.120.cfg verwenden`,dann  "No"')
    json_file=filedialog.askopenfilename(title='wählen Sie den json File,mit Device Liste ,aus',initialdir='.')#,filetypes=("Json File","*.json")
    with open(json_file, 'r') as f:
        user_data = json.load(f)
    for item in user_data:
        host = item['host']
        user = item['username']
        password = item['password']
        secret = item['secret']
        net_driver = item['net_driver']
        optional_args = {'secret': secret}
        print(f'\n connecting to Host{host}')
        device_ios = open_connection(host, user, password, secret, net_driver,optional_args)  # open ssh connection to each device& returen value from open_connection
        if ask =='yes':
            filename = filedialog.askopenfilename(title='wählen Sie den Configuration File aus')#filetypes='*.*'
        elif ask == 'no':
            filename=f'{host}.txt'
        device_ios.load_merge_candidate(filename)  # load the config file

        diffrent = device_ios.compare_config()  # compare the new configuration with the old one
        if len(diffrent) > 0:
            print('die neue Konfiguration ist : \n>> ')
            print(diffrent)
            while True:
                answer =messagebox.askquestion (message='Wollen Sie diese neue Konfiguration bestigegen(commit Configuration),bei ja drucken Sie yes bei neine drucken Sie no:  >>')
                if answer == 'yes':
                    device_ios.commit_config()
                    #print(device_ios.has_pending_commit())
                    #device_ios.confirm_commit()
                    time.sleep(10)
                    messagebox.showinfo(message='Done,the configuration is committed')
                    break
                elif answer == 'no':
                    device_ios.discard_config()
                    break

        else:
            messagebox.showinfo('keine Konfiguration Unterschied ,no changes requiered ')

        device_ios.close()
        print(f'disconnecting from Host{host}')
    quit()



def restore_config():
    with open('list_device_nap.json', 'r') as f:
        user_data = json.load(f)
    for item in user_data:
        host = item['host']
        user = item['username']
        password = item['password']
        secret = item['secret']
        net_driver = item['net_driver']
        optional_args = {'secret': secret}
        print(f'\n connecting to Host{host}')
        device_ios = open_connection(host, user, password, secret, net_driver, optional_args)  # open ssh connection to each device &returen value from open_connection
        print('Rollback the old Configuration begint')
        device_ios.rollback()
        print(f'disconnecting from Host{host}')
        device_ios.close()
    quit( )


