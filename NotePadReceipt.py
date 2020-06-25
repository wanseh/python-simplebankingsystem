import System
import datetime
import random
import os
letter_Code = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cr_rec(client_name):
    total_ams = 0
    x = datetime.datetime.now()
    fileName = client_name.replace(" ","")+ "_client" + str(x.strftime("%Y")) + str(random.choice(letter_Code)) + str(random.randrange(0,100))
    path_dir = "C:/Users/Lance Parantar/PycharmProjects/Python/Banking System/Receipt Folder/"
    path_filename = os.path.join(path_dir, fileName)
    with open(path_filename, "w") as FileWrite:
        FileWrite.writelines("Lance Banking Receipt\n" + str(x.strftime("%m/%d/%Y : %H:%M:%S")) +"\n\n" )
        FileWrite.writelines("Client Name: " + client_name + "\n\n")
        FileWrite.writelines("Bank Activities: \n-----------------------\n")
        for index, methods in enumerate(System.type_method):
            if index == 0:
                if methods == "Transferred Funds":
                    FileWrite.writelines(str(methods) + ": ")
                else:
                    FileWrite.writelines(str(methods) + ":\t   ")
            else:
                if index % 2 == 0:
                    FileWrite.writelines("\n")
                    if methods == "Deposit":
                        FileWrite.writelines(str(methods) + ":\t   ")
                    elif methods == "Transferred Funds":
                        FileWrite.writelines(str(methods) + ": ")
                    else:
                        FileWrite.writelines(str(methods) + ":\t   ")
                else:
                    total_ams += methods
                    FileWrite.writelines(str(methods) + " ")

        FileWrite.writelines("\n\nTotal:   " + str(total_ams) +"\n\n")

        FileWrite.writelines("Current Balance: " + "{:.2f}".format(float(System.clients[client_name][0])) + "\n")
        FileWrite.writelines("Please Come Again!")
    FileWrite.close()
    openFile(path_filename)

def openFile(fileName):
    os.system("notepad.exe " + fileName)



