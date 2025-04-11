import Netmiko_config as Netmiko_config
import Napal_config as Napal_config


# Rahmen
text = 'Welcome in Network Configuration Helper'
space = " "
stern = "*"
def rahmen():
    lang = len(text)
    sternlang = lang + 6
    for i in range(sternlang):
        print('*', end=' ')

rahmen()
print('\n {1}{1}{1}{1}{2}{2}{2}{2}{2} {0} {2}{2}{2}{2}{2} {1}{1}{1}{1}\n'.format(text, '*', ' '))
rahmen()

def report_Choice():
    report_choice = int(input('\n Welche Information  wollen Sie for Ihre Devices  ,\n "1" Show Running-Config ,\n "2" Show Ip Interface brief ,\n "3" Show Mac_address Table(bei Switch)  ,\n "4" Show CDP Neighbors ( **bei non Cisco Env,enabling LLDP und geben Sie bei Option 6 "show lldp neighbors),\n "5" Show Ip Route (bei Router &L3 SW ) , \n "6" Eigene Show Command ,\n "7" quit \n>> '))
    if report_choice == 1:
        command='show run '
        Netmiko_config.report(command)
    elif report_choice == 2:
        command = 'show ip interface brief '
        Netmiko_config.report(command)
    elif report_choice == 3:
        command = 'show mac address-table'
        Netmiko_config.report(command)
    elif report_choice == 4:
        command = 'show cdp neighbors '
        Netmiko_config.report(command)
    elif report_choice == 5:
        command = 'show ip route '
        Netmiko_config.report(command)
    elif report_choice == 6:
        command = input('geben Sie den gewünschte show comand ,\n>>')
        Netmiko_config.report(command)
    elif report_choice == 7:
        quit()
    else:
        print('falsche Eingabe ,versuchen Sie nochmal')
        report_Choice()
def new_config(): # function for new configuration
    new_choice=int(input('\n Welche Switches or Device Wollen Sie konfigurieren ,\n "1" Core Layer Switches ,\n "2" Distribution Layer Switches ,\n "3" Access Layer Switches ,\n "4" Network Device according to Managemenet IP Liste ,\n "5" quit \n>>'))
    if new_choice == 1:
        Netmiko_config.core_Sw()
    elif new_choice == 2:
        Netmiko_config.dist_Sw()
    elif new_choice == 3:
        Netmiko_config.acc_Sw()
    elif new_choice == 4:
        Netmiko_config.list_Sw()
    elif new_choice == 5:
        quit()
    else:
        print('falsche Eingabe ,versuchen Sie nochmal')
        new_choice()

def mana_config():
    login_choice = int(input('\n Welche Konfiguration Management Aufgabe wollen Sie erledigen ?: ,\n "1" Backup confguration ,\n "2" Replace Configuration ,\n "3" Merge Configuration ,\n "4" Restore last Configuration(after merge or Reolace Configuration Process) , \n "5" quit \n>>'))
    if login_choice == 1:
        command = 'show run '
        Netmiko_config.report(command)

    elif login_choice == 2:
        Napal_config.replace_config()
    elif login_choice == 3:
       Napal_config.merge_config()
    elif login_choice == 4:
        Napal_config.restore_config()
    elif login_choice == 5:
        quit()
    else:
        print('falsche Eingabe ,versuchen Sie nochmal')
        login_Choice()
def login_Choice():
    login_choice = int(input('\n Welche Aufgabe wollen Sie erledigen ?: ,\n "1" Neue Konfiguration ,\n "2" Manage Konfiguration ,\n "3" Reporte  ,\n "4" Upgrade IOS File Transfer (SCP), \n "5" quit \n>>'))
    if login_choice == 1:
       new_config()
    elif login_choice == 2:
       mana_config()
    elif login_choice == 3:
        report_Choice()
    elif login_choice == 4:
        Netmiko_config.scp_file_transfer
    elif login_choice == 5:
        quit()
    else:
        print('falsche Eingabe ,versuchen Sie nochmal')
        login_Choice()

def main():
    login_Choice()

main()