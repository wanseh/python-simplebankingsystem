import System as sysmain

def read_save_codes():
    index = 0
    with open("Client_File", "r") as ReadCode:
        for var in range(len(sysmain.clients)):
            ReadCode.seek(0)
            code = ReadCode.readlines()[index + 2].rstrip()
            num_code = int(code[2])
            index += 4

    ReadCode.close()
    return generateCode(num_code)


def generateCode(sys_cl, sys_Num = 0):

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if sys_cl != 10:
        sys_cl += 1
        letter = letters[int(sys_Num)]
        complete_code = letter + str(sys_Num) + str(sys_cl)
    else:
        sys_Num += 1
    return complete_code







