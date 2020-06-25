import AdminSys
import NotePadReceipt
import SystemCoding

clients = {}
sys_code = []
deposition = 0
withdrawal = 0
ch = ""
temp = 0.0
type_method = []



def default_val():
    print("Invalid!\n")

# This is where the user will choose different types of options.
# Whether it be deposit, withdraw, and Transfer of funds.
def client_deposit_or_withdraw(choice, client_name):
    try:
        amount = float(input("How Much: "))
        temp = float(clients[client_name][0])
        if choice == "1":
            temp -= amount
            if temp < 500:
                print("Account must have at least 500 Pesos!")
            else:
                type_method.append("Withdraw")
                type_method.append(amount)
                save_all(client_name, temp)
        elif choice == "2":
            temp += amount
            type_method.append("Deposit")
            type_method.append(amount)
            save_all(client_name,temp)
        elif choice == "3":

            pin_client_tran = int(input("Enter the pin of the account: \n"))
            AccFound = False
            for index, name_c in enumerate(clients):
                check_pin = int(clients[name_c][2])

                if pin_client_tran == check_pin:
                    AccFound = True
                    temp -= amount
                    clients[client_name][0] = temp
                    save_all(client_name, temp)

                    money_of_client = float(clients[name_c][0])
                    money_of_client += amount
                    clients[name_c][0] = money_of_client
                    print("Money has been transferred to: " + clients[name_c][1])
                    type_method.append("Transferred Funds")
                    type_method.append(amount)
                    save_all(name_c, clients[name_c][0])
                    break

            if not AccFound:
                print("Account does Not Exist!")

    except ValueError:
        print("Invalid Value")

# Save all the changes in the text file
def save_all(client_name, temp):
    clients[client_name][0] = temp
    read_text(client_name)
    write_text()

# This like a switch case but in python it is a dictionary that has key on it.
# I used lambda because the method was called more than once.
def options_2(opt, client_name):
    opt2 = {
        "1": lambda: client_deposit_or_withdraw(opt, client_name),
        "2": lambda: client_deposit_or_withdraw(opt, client_name),
        "3": lambda: client_deposit_or_withdraw(opt, client_name)
    }
    f = opt2.get(opt, default_val)
    return f()

# This is where created accounts are made using a dictionary that maps the user's name
# to its money, pin, and code.
def create_acc():
    name = input("Enter Name: ")
    while True:
        try:
            client_balance = float(input("Enter Starting Money: "))
            if client_balance >= 500:
                break
            else:
                print("Starting money must be at least 500 and above!")
        except ValueError:
            print("Invalid Money")
    try:
        while True:
            if len(clients) == 0:
                pin = int(input("Enter Pin: "))
                break
            else:
                count_same_pin = 0
                pin = int(input("Enter Pin: "))
                for var in clients:
                    check = int(clients[var][2])
                    if pin == check:
                        count_same_pin += 1
                        print("That PIN has already taken!")

                if count_same_pin == 0:
                    break
    except ValueError:
        print("It must be numeric")
    if len(clients) == 0:
        code = SystemCoding.generateCode(0)
    else:
        code = SystemCoding.read_save_codes()
    client_info = [client_balance,code,pin]
    clients[name] = client_info
    append_createdAcc(name) # appends the created account to the text file


# Menu option of the user
def acc_client(pin):
    for var in clients:
        if pin == clients[var][2]:
            while True:
                print("\nWelcome", var + "!")
                print("Current Balance: ", "{:.2f}".format(float(clients[var][0])), "\n")
                print("1 - Withdraw\n2 - Deposit\n3 - Transfer Money\n4 - Logout")
                ch = input("Enter Choice: ")
                if ch == "4":
                    if len(type_method) != 0:
                        print("Showing Receipt...\n")
                        NotePadReceipt.cr_rec(var)
                        type_method.clear()
                    break
                else:
                    options_2(ch, var)



def login_acc():
    input_client_pin = input("Enter pin: ")
    if "#" in input_client_pin:
        AdminSys.admin_sys(input_client_pin)
    else:
        acc_client(input_client_pin)


def options(num_op):
    selector = {
        "1": create_acc,
        "2": login_acc
    }
    func = selector.get(num_op, default_val)
    return func()


def read_text(client_name):
    with open("Client_File", "r") as FileRead:
        for i, line in enumerate(FileRead, 0):
            if line == client_name:
                FileRead[i + 1] = str(clients[client_name][0])
    FileRead.close()


def write_text():
    with open("Client_File", "w") as FileWrite:
        for name in clients:
            FileWrite.writelines(name + "\n")
            for name_info in clients[name]:
                FileWrite.writelines(str(name_info) + "\n")
    FileWrite.close()


def append_createdAcc(name):
    with open("Client_File", "a") as Filehandle:
        Filehandle.write(name + "\n")
        for var in clients[name]:
            Filehandle.writelines(str(var) + "\n")
    Filehandle.close()



