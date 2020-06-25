import System as sysmain
import os


# This reads the Client_File.txt so that we won't have to recreate an account
# Basically its like a database of the banking system in a text file
def read_save_acc():
    c_file = {}
    c_name = ""
    c_mon = 0.0
    c_pin = 0
    c_code =""
    with open("C:/Users/Lance Parantar/PycharmProjects/Python/Banking System/Client_File", "r") as FileReader:
        for i, line in enumerate(FileReader,0):
            line = line.strip()
            if i == 0 or i % 4 == 0:
                c_name = line
            else:
               if "." in line:
                   c_mon = line
               elif (i + 1) % 4 == 0:
                   c_pin = line
               else:
                   c_code = line
            c_info = [c_mon,c_code,c_pin]
            c_file[c_name] = c_info
            sysmain.clients = c_file.copy()
        FileReader.close()



if __name__ == '__main__':
    while True:
        if os.stat("C:/Users/Lance Parantar/PycharmProjects/Python/Banking System/Client_File").st_size != 0:
            read_save_acc()
        print("Welcome to Lance Banking System")
        print("1 - Open an Account\n2 - Login")
        print(sysmain.clients)
        n = input("Enter Choice: ")
        sysmain.options(n)