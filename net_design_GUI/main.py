import Netmiko_config as Netmiko_config
import Napal_config as Napal_config
from tkinter import *
import tkinter as tk

root = tk.Tk()

# Rahmen
text = 'Welcome in Network Configuration Helper'
space = " "
stern = "*"


def rahmen():
    lang = len(text)
    sternlang = lang + 4
    for i in range(sternlang):
        print('*', end=' ')


rahmen()
print('\n {1}{1}{1}{1}{2}{2}{2}{2}{2} {0} {2}{2}{2}{2}{2} {1}{1}{1}{1}\n'.format(text, '*', ' '))
rahmen()


def window(title, size: int):
    root.title(title)
    root.geometry(f'{size[0]}x{size[1]}')
    root.minsize(size[0], size[1])

    label_welcom = Label(master=root, text='Welcom to the Netzwerk Configuration  Manger \n',font=('Calibri 18 bold italic'),
                         background='gray44', foreground='misty rose')
    label_welcom.place(relx=0.1, rely=0.0, anchor='nw')
    root.mainloop()


def report_Choice():
    def forget():
        label.destroy()
        button_ip_int.destroy()
        button_mac_add.destroy()
        button_cdp_neigh.destroy()
        button_ip_rout.destroy()
        button_show_com.destroy()
        button_exit.destroy()
        button_back.destroy()
        root.quit()
    def button_ip_int():
        forget()
        command = 'show ip  interface brief '
        show_ip_comm = Netmiko_config.report(command)
        report_win = tk.Text(root,yscrollcommand=True,xscrollcommand=True,font=('Calibri 12 bold italic'),fg='SteelBlue3')

        report_win.insert("1.0",show_ip_comm)#tk.END
        report_win.pack(fill="both", expand=True)

    def button_mac_add():
        forget()
        command = 'show mac address-table'
        Netmiko_config.report(command)
    def button_cdp_neigh():
        forget()
        command = 'show cdp neighbors '
        Netmiko_config.report(command)
    def button_ip_rout():
        forget()
        command = 'show ip route '
        Netmiko_config.report(command)
    def button_show_com():
        forget()
        command = input('geben Sie den gewünschte show comand ,\n>>')
        Netmiko_config.report(command)

    def button_back():
        forget()
        login_Choice()

    label = Label(master=root, text='\n   Welche Information  wollen Sie for Ihre Devices  : ',
                  font=('Calibri 16  italic'), foreground='Lightpink3')
    label.place(relx=0.0, rely=0.1)
    button_ip_int = Button(master=root, text=' Show Ip Interface brief ', command=button_ip_int,font=('Calibri 13 bold italic'), foreground='Lightpink1', background='gray26')
    button_ip_int.place(relx=0.10, rely=0.25, width=270, height=50)
    button_mac_add = Button(master=root, text=' Show Mac_address Table(bei Switch)  ', command=button_mac_add,
                            font=('Calibri 13 bold italic'), foreground='MediumPurple2', background='gray26')
    button_mac_add.place(relx=0.47, rely=0.38, width=270, height=50)
    button_cdp_neigh = Button(master=root,text=' Show CDP Neighbors \n(**bei non Cisco Env,enabling LLDP und geben Sie bei Option 6 "show lldp neighbors) ',
                              command=button_cdp_neigh, font=('Calibri 12 bold italic'), foreground='Lightpink1',background='gray26')
    button_cdp_neigh.place(relx=0.10, rely=0.50, width=270, height=50)
    button_ip_rout = Button(master=root, text='Show Ip Route (bei Router &L3 SW ))', command=button_ip_rout,font=('Calibri 12 bold italic'), foreground='MediumPurple2', background='gray26')
    (button_ip_rout.place(relx=0.40, rely=0.63, width=280, height=50))
    button_show_com = Button(master=root, text=' Eigene Show Command) ', command=button_show_com,font=('Calibri 13  bold italic'), foreground='Lightpink1', background='gray26')
    button_show_com.place(relx=0.10, rely=0.78, width=270, height=50)
    button_back = Button(master=root, text=' Back  ', command=button_back, font=('Calibri 15 bold italic'),
                         foreground='Lightpink3')
    button_back.place(relx=0.15, rely=0.89, width=150, height=50)
    button_exit = Button(master=root, text='  Exit   ', command=root.destroy, font=('Calibri 15 bold italic'),
                         foreground='MediumPurple2')
    button_exit.place(relx=0.50, rely=0.89, width=150, height=50)

    window('Report', (600, 500))


def new_config():  # function for new configuration
    def forget():
        label.destroy()
        button_cor_sw.destroy()
        button_dis_sw.destroy()
        button_acce_sw.destroy()
        button_list_sw.destroy()
        button_exit.destroy()
        button_back.destroy()
        root.quit()

    # new_choice=int(input('\n  ,\n "1" Core Layer Switches ,\n "2" Distribution Layer Switches ,\n "3" Access Layer Switches ,\n "4" Network Device according to Managemenet IP Liste ,\n "5" quit \n>>'))
    def button_cor_sw():
        Netmiko_config.core_Sw()
        forget()

    def button_dis_sw():
        Netmiko_config.dist_Sw()
        forget()

    def button_acce_sw():
        Netmiko_config.acc_Sw()
        forget()

    def button_list_sw():
        forget()
        Netmiko_config.list_Sw()


    def button_back():
        forget()
        login_Choice()

    # new_choice=int(input('\n Welche Switches or Device Wollen Sie konfigurieren ,\n "1"  ,\n "2"  ,\n "3"  ,\n "4"  ,\n "5" quit \n>>'))
    label = Label(master=root, text='\n   Welche Switches or Device Wollen Sie konfigurieren  : ',
                  font=('Calibri 16  italic'), foreground='OrangeRed3')
    label.place(relx=0.0, rely=0.1)

    button_cor_sw = Button(master=root, text=' Core Layer Switches ', command=button_cor_sw,
                           font=('Calibri 15 bold italic'), foreground='Lightpink1', background='gray26')
    button_cor_sw.place(relx=0.10, rely=0.25, width=270, height=50)
    button_dis_sw = Button(master=root, text=' Distribution Layer Switches  ', command=button_dis_sw,
                           font=('Calibri 15 bold italic'), foreground='snow', background='gray26')
    button_dis_sw.place(relx=0.47, rely=0.40, width=270, height=50)
    button_acce_sw = Button(master=root, text=' Access Layer Switches ', command=button_acce_sw,
                            font=('Calibri 15 bold italic'), foreground='Coral2', background='gray26')
    button_acce_sw.place(relx=0.10, rely=0.55, width=270, height=50)
    button_list_sw = Button(master=root, text='Network Device according to \n Managemenet IP Liste)',
                            command=button_list_sw, font=('Calibri 12 bold italic'), foreground='Salmon2',background='gray26')
    (button_list_sw.place(relx=0.40, rely=0.70, width=280, height=50))
    button_back = Button(master=root, text='  Back  ', command=button_back, font=('Calibri 14 bold italic'),foreground='OrangeRed3')
    button_back.place(relx=0.25, rely=0.85, width=100, height=50)
    button_exit = Button(master=root, text='  Exit   ', command=root.destroy, font=('Calibri 14 bold italic'),foreground='Lightpink2')
    button_exit.place(relx=0.50, rely=0.85, width=100, height=50)

    window('New Configuration', (600, 500))


def mana_config():
    def forget():
        label.destroy()
        button_back_con.destroy()
        button_merg_con.destroy()
        button_repl_con.destroy()
        button_rest_conf.destroy()
        button_back.destroy()
        button_exit.destroy()
        root.quit()

    def button_back_con():
        forget()
        command = 'show run '
        Netmiko_config.report(command)

    def button_repl_con():
        forget()
        Napal_config.replace_config()

    def button_merg_con():
        forget()
        Napal_config.merge_config()

    def button_rest_conf():
        forget()
        Napal_config.restore_config()

    def button_back():
        forget()
        login_Choice()

    label = Label(master=root, text='\n Welche Configuration Management Aufgabe wollen Sie  : ',
                  font=('Calibri 16  italic'), foreground='PaleVioletRed1')
    label.place(relx=0.0, rely=0.1)

    button_back_con = Button(master=root, text=' Backup confguration  ', command=button_back_con,
                             font=('Calibri 15 bold italic'), foreground='PaleVioletRed1', background='gray26')
    button_back_con.place(relx=0.10, rely=0.25, width=270, height=50)
    button_repl_con = Button(master=root, text=' Replace Configuration  ', command=button_repl_con,
                             font=('Calibri 15 bold italic'), foreground='DeepSkyBlue3', background='gray26')
    button_repl_con.place(relx=0.47, rely=0.40, width=270, height=50)
    button_merg_con = Button(master=root, text=' Merge Configuration ', command=button_merg_con,
                             font=('Calibri 15 bold italic'), foreground='PaleVioletRed1', background='gray26')
    button_merg_con.place(relx=0.10, rely=0.55, width=270, height=50)
    button_rest_conf = Button(master=root, text='Restore last Configuration\n(after merge or Replace Configu Process)',
                              command=button_rest_conf, font=('Calibri 12 bold italic'), foreground='DeepSkyBlue3',
                              background='gray26')
    (button_rest_conf.place(relx=0.40, rely=0.70, width=280, height=50))
    button_back = Button(master=root, text='  Back  ', command=button_back, font=('Calibri 14 bold italic'),
                         foreground='PaleVioletRed1')
    button_back.place(relx=0.25, rely=0.85, width=100, height=50)
    button_exit = Button(master=root, text='  Exit   ', command=root.destroy, font=('Calibri 14 bold italic'),foreground='DeepSkyBlue3')
    button_exit.place(relx=0.50, rely=0.85, width=100, height=50)

    window('Management Configuration', (600, 500))


def login_Choice():
    def forget():
        label.destroy()
        button_new_con.destroy()
        button_man_con.destroy()
        button_scp.destroy()
        button_repo.destroy()
        button_exit.destroy()
        root.quit()

    def button_new_con():
        forget()
        new_config()

    def button_man_con():
        forget()
        mana_config()

    def button_repo():
        forget()
        report_Choice()

    def button_scp():
        forget()
        Netmiko_config.scp_file_transfer()

    label = Label(master=root, text='\n Welche Aufgabe wollen Sie erledigen : ',
                  font=('Calibri 16  italic'), foreground='IndianRed1')
    label.place(relx=0.0, rely=0.1)

    button_new_con = Button(master=root, text=' New Configuration  ', command=button_new_con,
                            font=('Calibri 15 bold italic'), foreground='IndianRed1', background='gray26')
    button_new_con.place(relx=0.10, rely=0.25, width=250, height=50)
    button_man_con = Button(master=root, text=' Manage Configuration  ', command=button_man_con,
                            font=('Calibri 15 bold italic'), foreground='SkyBlue2', background='gray26')
    button_man_con.place(relx=0.47, rely=0.40, width=250, height=50)
    button_repo = Button(master=root, text=' Report ', command=button_repo, font=('Calibri 15 bold italic'),
                         foreground='IndianRed1', background='gray26')
    button_repo.place(relx=0.10, rely=0.55, width=250, height=50)
    button_scp = Button(master=root, text=' Secure File Transfer (SCP)  ', command=button_scp,
                        font=('Calibri 15 bold italic'), foreground='SkyBlue2', background='gray26')
    button_scp.place(relx=0.47, rely=0.70, width=250, height=50)
    button_exit = Button(master=root, text='  Exit   ', command=root.destroy, font=('Calibri 15 bold italic'),
                         foreground='IndianRed1')
    button_exit.place(relx=0.25, rely=0.85, width=250, height=50)

    window('Main Option', (600, 500))


def main():
    login_Choice()


main()
