import getpass
import json
import time
from napalm import get_network_driver


def open_connection(host, user, password, secret, net_driver, optional_args):
    if user != ' ':
        pass
    else:
        user = input(f'enter User name for {host}:\n>>')
    if password != ' ':
        pass
    else:
        password = getpass.getpass(prompt=f'bitte enter user {user} Password :\n >>')

    if secret != ' ':
        pass
    else:
        secret = getpass.getpass(prompt=f'bitte enter Enable Password for Host {host} :\n >>')
    driver = get_network_driver(net_driver)  # Driver used for different modell& network Venders ,(z.b with meistens cisco sw und router  is 'ios' ,there is also 'ios-xr'&'nx-os' )
    device_ios = driver(host, user, password,optional_args=optional_args)  # api or ssh(bei ios) connection to the device
    device_ios.open()
    return device_ios


def replace_config():
    with open('list_device_nap.json', 'r') as f:
        user_data = json.load(f)
    for item in user_data:
        host = item['host']
        user = item['username']
        password = item['password']
        secret = item['secret']
        net_driver = item['net_driver']
        optional_args = {'secret': secret}
        print(f'connecting to Host{host}')
        device_ios = open_connection(host, user, password, secret, net_driver, optional_args)
        print('applied the new configuration')
        device_ios.load_replace_candidate(filename=f'{host}.cfg')
        diffrent = device_ios.compare_config()  # compare the new configuration with the old one
        if len(diffrent) > 0:
            print('die neue Konfiguration ist : \n>> ')
            print(diffrent)
            while True:
                answer = input(
                    'Wollen Sie diese neue Konfiguration bestigegen(commit Configuration),bei ja drucken Sie yes bei neine drucken Sie no: \n >>')
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
                else:
                    print('falshe Eingabe ,versuchen Sie nochmal')

        print(f'disconnecting from Host{host}...')
        device_ios.close()


def merge_config():
    with open('list_device_nap.json', 'r') as f:
        user_data = json.load(f)
    for item in user_data:
        host = item['host']
        user = item['username']
        password = item['password']
        secret = item['secret']
        net_driver = item['net_driver']
        optional_args = {'secret': secret}
        print(f'connecting to Host{host}')
        device_ios = open_connection(host, user, password, secret, net_driver,optional_args)  # open ssh connection to each device& returen value from open_connection
        device_ios.load_merge_candidate(filename='config.cfg')  # load the config file
        diffrent = device_ios.compare_config()  # compare the new configuration with the old one
        if len(diffrent) > 0:
            print('die neue Konfiguration ist : \n>> ')
            print(diffrent)
            while True:
                answer = input('Wollen Sie diese neue Konfiguration bestigegen(commit Configuration),bei ja drucken Sie yes bei neine drucken Sie no: \n >>')
                if answer == 'yes':
                    device_ios.commit_config()
                    #print(device_ios.has_pending_commit())
                    #device_ios.confirm_commit()
                    time.sleep(10)
                    print('Done,the configuration is committed')
                    break
                elif answer == 'no':
                    device_ios.discard_config()
                    break
                else:
                    print('falshe Eingabe ,versuchen Sie nochmal')
        else:
            print('keine Konfiguration Unterschied ,no changes requiered ')

        device_ios.close()
        print(f'disconnecting from Host{host}')


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
        print(f'connecting to Host{host}')
        device_ios = open_connection(host, user, password, secret, net_driver, optional_args)  # open ssh connection to each device &returen value from open_connection
        print('Rollback the old Configuration begint')
        device_ios.rollback()
        print(f'disconnecting from Host{host}')
        device_ios.close()

        # device_ios.traceroute(destination=,source=)
