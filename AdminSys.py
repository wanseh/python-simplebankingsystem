import System
import xlsxwriter

admin_pass = "#"


def display_Acc():
    for i, var in enumerate(System.clients):
        print((i + 1), "-", var)


def delete_Acc(num):
    acc_list = list(System.clients.keys())
    del System.clients[acc_list[num - 1]]
    System.write_text()


def admin_sys(admin_pin):
    while True:
        if len(System.clients) == 0:
            print("There are no available accounts!\n")
            break
        else:
            print("\nAvailable Accounts:\n0 - Exit\n ")
            display_Acc()
            choice = input("Input Number to delete Account: ")
            if choice == "0":
                break
            ch = input("Are you sure to delete this account? Y/N: ")
            try:
                if ch.upper() == "Y":
                    delete_Acc(int(choice))
                elif ch.upper() == "N":
                    return admin_sys(admin_pass)
            except ValueError:
                print("Invalid Value")

