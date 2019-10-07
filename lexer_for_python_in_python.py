class token:
    def __init__(self):
        self.row= 0
        self.col = 0
        self.type = -1
        self.block_order=1
        self.block_number=1
        self.name = ""

def iskeyword(nextword):
    keywords = ["while","if","else","elif","for","def","and","or","not"]
    if nextword in keywords:
        return getSymbolId("s_"+nextword)
    else:
        return getSymbolId("s_id")

def getSymbolId(symbol):
    symbols = symbols = ["s_@","s_string", "s_id","s_in", "s_zno", "s_qno", "s_le", "s_ne", "s_lt", "s_ge", "s_gt", "s_iseq", "s_eq", "s_divit", "s_div", "s_mulit",
    "s_mul", "s_addit", "s_add", "s_subit", "s_sub", "s_modit", "s_mod", "s_parop", "s_parclose", "s_brop", "s_brclose", "s_abop", "s_abclose",
    "s_if", "s_while", "s_else", "s_elif", "s_for", "s_def", "s_not", "s_colon", "s_and", "s_or", "s_dot", "s_como","s_True","s_Fals","s_class",
               "s_finally","s_is","s_return","s_None","s_continue","s_for","s_lambda","s_tr","s_def","s_from","s_nonlocal","s_while","s_and",
               "s_del","s_global","s_not","s_with","s_as","s_elif","s_if","s_or","s_yield","s_assert","s_else","s_import","s_pass","s_break",
               "s_except","s_in","s_raise"]
    return symbols.index(symbol.lower())

def SymbolIs(idn):
    symbols = ["s_@","s_string", "s_id", "s_in", "s_zno", "s_qno", "s_le", "s_ne", "s_lt", "s_ge", "s_gt", "s_iseq", "s_eq",
               "s_divit", "s_div", "s_mulit",
               "s_mul", "s_addit", "s_add", "s_subit", "s_sub", "s_modit", "s_mod", "s_parop", "s_parclose", "s_brop",
               "s_brclose", "s_abop", "s_abclose",
               "s_if", "s_while", "s_else", "s_elif", "s_for", "s_def", "s_not", "s_colon", "s_and", "s_or", "s_dot",
               "s_como", "s_True", "s_Fals", "s_class",
               "s_finally", "s_is", "s_return", "s_None", "s_continue", "s_for", "s_lambda", "s_tr", "s_def", "s_from",
               "s_nonlocal", "s_while", "s_and",
               "s_del", "s_global", "s_not", "s_with", "s_as", "s_elif", "s_if", "s_or", "s_yield", "s_assert",
               "s_else", "s_import", "s_pass", "s_break",
               "s_except", "s_in", "s_raise"]
    return symbols[idn]

block_list=[1]
block_second_list=[1]
block_last_number=1
def lexer(intext):
    global index,block_last_number,rowno,colno,errors,block_order,block_number,flag
    block_order = len(block_list)
    block_number=1
    mytok = token()
    nextword = ""
    lastchar = '\0'
    state = 0
    while(index< len(intext)):
        nextword += intext[index]
        nextchar = intext[index]
        index+=1
        if (nextchar == '\n'):
            pass
        else:
            colno += 1
        if (state==0):
            if (nextchar == '\n'):
                rowno +=1
                colno =0
                flag=True
            else:
                pass
            if(nextchar == '\n' or nextchar == '\t' or nextchar==' '):
                pass
            elif(flag):
                flag=False
                temp_col_number=colno
                top_of_list=block_list[len(block_list)-1]
                while(top_of_list>temp_col_number):
                    block_list.pop()
                    block_second_list.pop()
                    top_of_list = block_list[len(block_list) - 1]
                if(top_of_list==temp_col_number):
                    block_order=len(block_list)
                    block_number=block_second_list[len(block_list)-1]
                else:
                    block_last_number+=1
                    block_list.append(temp_col_number)
                    block_second_list.append(block_last_number)
                    block_order = len(block_list)
                    block_number=block_last_number
                        
            if(nextchar == '\n' or nextchar == '\t' or nextchar==' '):
                nextword = ""
            elif((nextchar <= 'z' and nextchar >= 'a')or(nextchar <= 'Z' and nextchar>= 'A') or nextchar == '_'):
                state = 1
            elif(nextchar=='@'):
                mytok.name = nextword
                mytok.type = getSymbolId("s_@")
            elif(nextchar == '\''):
                state = 2
            elif (nextchar == '\"'):
                state = 10
            elif (nextchar >= '0' and nextchar <= '9'):
                state = 18
            elif (nextchar == '.'):
                state = 19
            elif (nextchar == '<'):
                state = 21
            elif (nextchar == '>'):
                state = 22
            elif (nextchar == '='):
                state = 23
            elif (nextchar == '!'):
                state = 24
            elif (nextchar == '/'):
                state = 25
            elif (nextchar == '*'):
                state = 26
            elif (nextchar == '+'):
                state = 27
            elif (nextchar == '-'):
                state = 28
            elif (nextchar == '%'):
                state = 29
            elif (nextchar == '('):
                mytok.name = nextword
                mytok.type = getSymbolId("s_parop")
                mytok.row = rowno
                mytok.col = colno
                mytok.block_order=block_order
                mytok.block_number=block_number
                return mytok
            elif (nextchar == ')'):
                mytok.name = nextword
                mytok.type = getSymbolId("s_parclose")
                mytok.row = rowno
                mytok.col = colno
                mytok.block_order=block_order
                mytok.block_number=block_number
                return mytok
            elif (nextchar == '['):
                mytok.name = nextword
                mytok.type = getSymbolId("s_brop")
                mytok.row = rowno
                mytok.col = colno
                mytok.block_order=block_order
                mytok.block_number=block_number
                return mytok
            elif (nextchar == ']'):
                mytok.name = nextword
                mytok.type = getSymbolId("s_brclose")
                mytok.row = rowno
                mytok.col = colno
                mytok.block_order=block_order
                mytok.block_number=block_number
                return mytok
            elif (nextchar == '{'):
                mytok.name = nextword
                mytok.type = getSymbolId("s_abop")
                mytok.row = rowno
                mytok.col = colno
                mytok.block_order=block_order
                mytok.block_number=block_number
                return mytok
            elif (nextchar == '}'):
                mytok.name = nextword
                mytok.type = getSymbolId("s_abclose")
                mytok.row = rowno
                mytok.col = colno
                mytok.block_order=block_order
                mytok.block_number=block_number
                return mytok
            elif (nextchar == ':'):
                mytok.name = nextword
                mytok.type = getSymbolId("s_colon")
                mytok.row = rowno
                mytok.col = colno
                mytok.block_order=block_order
                mytok.block_number=block_number
                return mytok
            elif (nextchar == ','):
                mytok.name = nextword
                mytok.type = getSymbolId("s_como")
                mytok.row = rowno
                mytok.col = colno
                mytok.block_order=block_order
                mytok.block_number=block_number
                return mytok
            elif (nextchar == '#'):
                state = 30
            else:
                errors += 1
                mytok.type = -1
                mytok.name = nextword
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order=block_order
                mytok.block_number=block_number
                return mytok
        elif(state==1):
            if ((nextchar <= 'z' and nextchar >= 'a') or (nextchar <= 'Z' and nextchar >= 'A') or (nextchar>='0' and nextchar <= '9') or (nextchar=='_')):
                state = 1
            else:
                index-=1
                mytok.type = iskeyword(nextword[:-1])
                mytok.name = nextword[:-1]
                mytok.row = rowno
                mytok.col = colno
                mytok.block_order=block_order
                mytok.block_number=block_number
                return mytok
        elif(state==2):
            if(nextchar=='\''):
                state = 5
            elif(nextchar=='\\'):
                state = 4
            else:
                state = 3
        elif(state==3):
            if(nextchar=='\''):
                mytok.type = getSymbolId("s_string")
                mytok.name = nextword[1:-1]
                mytok.row = rowno
                mytok.col = colno
                mytok.block_order=block_order
                mytok.block_number=block_number
                return mytok
            elif(nextchar=='\\'):
                state = 4
            else:
                state = 3
        elif(state==4):
            if(nextchar=='n'):
                nextword = nextword[:-2] + '\n'
                state = 3
            elif(nextchar=='t'):
                nextword = nextword[:-2] + '\t'
                state = 3
            elif (nextchar == '\\'):
                nextword = nextword[:-2] + '\\'
                state = 3
            elif (nextchar == '\''):
                nextword = nextword[:-2] + '\''
                state = 3
            elif (nextchar == '"'):
                nextword = nextword[:-2] + '"'
                state = 3
        elif(state == 5):
            if(nextchar == '\''):
                state = 6
            else:
                mytok.type = getSymbolId("s_string")
                mytok.name = ""
                mytok.row = rowno
                mytok.col = colno
                mytok.block_order=block_order
                mytok.block_number=block_number
                index -= 1
                return mytok
        elif(state == 6):
            if (nextchar == '\''):
                state = 7
            elif (nextchar =='\\'):
                state = 9
            else:
                state = 6
        elif (state == 7):
            if (nextchar == '\''):
                state = 8
            else:
                errors += 1
                mytok.type = -1
                mytok.name = nextword
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order=block_order
                mytok.block_number=block_number
                index-=1
                return mytok
        elif (state == 8):
            if (nextchar == '\''):
                mytok.type = getSymbolId("s_string")
                mytok.name = nextword[3:-3]
                mytok.row = rowno
                mytok.col = colno
                mytok.block_order=block_order
                mytok.block_number=block_number
                return mytok
            else:
                errors += 1
                mytok.type = -1
                mytok.name = nextword
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order=block_order
                mytok.block_number=block_number
                index-=1
                return mytok
        elif (state == 9):
            if(nextchar=='n'):
                nextword = nextword[:-2] + '\n'
                state = 6
            elif(nextchar=='t'):
                nextword = nextword[:-2] + '\t'
                state = 6
            elif (nextchar == '\\'):
                nextword = nextword[:-2] + '\\'
                state = 6
            elif (nextchar == '\''):
                nextword = nextword[:-2] + '\''
                state = 6
            elif (nextchar == '"'):
                nextword = nextword[:-2] + '"'
                state = 6
        elif(state==10):
            if(nextchar=='\"'):
                state = 13
            elif(nextchar=='\\'):
                state = 12
            else:
                state = 11
        elif(state==11):
            if(nextchar=='\"'):
                mytok.type = getSymbolId("s_string")
                mytok.name = nextword[1:-1]
                mytok.row = rowno
                mytok.col = colno
                mytok.block_order=block_order
                mytok.block_number=block_number
                return mytok
            elif(nextchar=='\\'):
                state = 12
            else:
                state = 11
        elif(state==12):
            if(nextchar=='n'):
                nextword = nextword[:-2] + '\n'
                state = 11
            elif(nextchar=='t'):
                nextword = nextword[:-2] + '\t'
                state = 11
            elif (nextchar == '\\'):
                nextword = nextword[:-2] + '\\'
                state = 11
            elif (nextchar == '\''):
                nextword = nextword[:-2] + '\''
                state = 11
            elif (nextchar == '"'):
                nextword = nextword[:-2] + '"'
                state = 11
        elif(state == 13):
            if(nextchar == '\"'):
                state = 14
            else:
                mytok.type = getSymbolId("s_string")
                mytok.name = ""
                mytok.row = rowno
                mytok.col = colno
                mytok.block_order = block_order
                index -= 1
                return mytok
        elif(state == 14):
            if (nextchar == '\"'):
                state = 15
            elif (nextchar =='\\'):
                state = 17
            else:
                state = 14
        elif (state == 15):
            if not(nextchar == '\"'):
                state = 16
                errors += 1
                mytok.type = -1
                mytok.name = nextword
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                index -= 1
                return mytok
            elif(nextchar == '\"'):
                state = 16
        elif (state == 16):
            if (nextchar == '\"'):
                mytok.type = getSymbolId("s_string")
                mytok.name = nextword[3:-3]
                mytok.row = rowno
                mytok.col = colno
                mytok.block_order = block_order
                return mytok
            else:
                errors += 1
                mytok.type = -1
                mytok.name = nextword
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                index -= 1
                return mytok
        elif (state == 17):
            if(nextchar=='n'):
                nextword = nextword[:-2] + '\n'
                state = 14
            elif(nextchar=='t'):
                nextword = nextword[:-2] + '\t'
                state = 14
            elif (nextchar == '\\'):
                nextword = nextword[:-2] + '\\'
                state = 14
            elif (nextchar == '\''):
                nextword = nextword[:-2] + '\''
                state = 14
            elif (nextchar == '"'):
                nextword = nextword[:-2] + '"'
                state = 14
        elif (state == 18):
            if (nextchar >= '0' and nextchar <= '9'):
                state = 18
            elif (nextchar == '.'):
                state = 20
            else:
                mytok.name = nextword[:-1]
                mytok.type = getSymbolId("s_zno")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                index -= 1
                return mytok
        elif (state == 19):
            if (nextchar >= '0' and nextchar <= '9'):
                state = 20
            else:
                mytok.name = nextword[:-1]
                mytok.type = getSymbolId("s_dot")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                index -= 1
                return mytok
        elif (state == 20):
            if (nextchar >= '0' and nextchar <= '9'):
                state = 20
            else:
                mytok.name = nextword[:-1]
                mytok.type = getSymbolId("s_qno")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                index -= 1
                return mytok
        elif (state == 21):
            if (nextchar == '='):
                mytok.name = nextword
                mytok.type = getSymbolId("s_le")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                return mytok
            elif (nextchar == '>'):
                mytok.name = nextword
                mytok.type = getSymbolId("s_ne")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                return mytok
            else:
                mytok.name = nextword[:-1]
                mytok.type = getSymbolId("s_lt")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                index -= 1
                return mytok
        elif (state == 22):
            if (nextchar == '='):
                mytok.name = nextword
                mytok.type = getSymbolId("s_ge")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                return mytok
            elif (nextchar == '<'):
                mytok.name = nextword
                mytok.type = getSymbolId("s_ne")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                return mytok
            else:
                mytok.name = nextword[:-1]
                mytok.type = getSymbolId("s_gt")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                index -= 1
                return mytok
        elif (state == 23):
            if (nextchar == '='):
                mytok.name = nextword
                mytok.type = getSymbolId("s_iseq")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                return mytok
            else:
                mytok.name = nextword[:-1]
                mytok.type = getSymbolId("s_eq")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                index -= 1
                return mytok
        elif (state == 24):
            if (nextchar == '='):
                mytok.name = nextword
                mytok.type = getSymbolId("s_ne")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                return mytok
            else:
                mytok.name = nextword[:-1]
                mytok.type = getSymbolId("s_not")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                index -= 1
                return mytok
        elif (state == 25):
            if (nextchar == '='):
                mytok.name = nextword
                mytok.type = getSymbolId("s_divit")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                return mytok
            else:
                mytok.name = nextword[:-1]
                mytok.type = getSymbolId("s_div")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                index -= 1
                return mytok
        elif (state == 26):
            if (nextchar == '='):
                mytok.name = nextword
                mytok.type = getSymbolId("s_mulit")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                return mytok
            else:
                mytok.name = nextword[:-1]
                mytok.type = getSymbolId("s_mul")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                index -= 1
                return mytok
        elif (state == 27):
            if (nextchar == '='):
                mytok.name = nextword
                mytok.type = getSymbolId("s_addit")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                return mytok
            else:
                mytok.name = nextword[:-1]
                mytok.type = getSymbolId("s_add")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                index -= 1
                return mytok
        elif (state == 28):
            if (nextchar == '='):
                mytok.name = nextword
                mytok.type = getSymbolId("s_subit")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                return mytok
            else:
                mytok.name = nextword[:-1]
                mytok.type = getSymbolId("s_sub")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                index -= 1
                return mytok
        elif (state == 29):
            if (nextchar == '='):
                mytok.name = nextword
                mytok.type = getSymbolId("s_modit")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                return mytok
            else:
                mytok.name = nextword[:-1]
                mytok.type = getSymbolId("s_mod")
                mytok.col = colno
                mytok.row = rowno
                mytok.block_order = block_order
                index -= 1
                return mytok
        elif (state == 30):
            if (nextchar == '\n'):
                state = 0
                index -= 1
            else:
                state = 30

rowno = 0
colno = 0
index = 0
errors = 0

def main():
    global rowno, colno, index, errors,flag,block_last_number
    flag=False
    er = []
    filename = "text.txt"
    textfile = open(filename,"r")
    intext = textfile.read()
    intext = intext+" "
    mytok = token()
    f = open('out.txt','w')
    while(mytok):
        mytok = lexer(intext)
        if (mytok):
            if (mytok.type >= 0):
                print("token in word " + str(mytok.name) + " with type " + str(SymbolIs(mytok.type)) + " in ( Col: " + str(
                    mytok.col - len(mytok.name)) + " , Row: " + str(mytok.row) +" block number is: "+str(mytok.block_number)+ " block order is: "+str(mytok.block_order)+ " )")
                f.write("token in word " + str(mytok.name) + " with type " + str(SymbolIs(mytok.type)) + " in ( Col: " + str(
                    mytok.col - len(mytok.name)) + " , Row: " + str(mytok.row) +" block number is: "+str(mytok.block_number)+ " block order is: "+str(mytok.block_order)+ " )"+"\n")
            elif (mytok.type == -1):
                er.append(
                    "error in word " + str(mytok.name) + " in ( Col: " + str(mytok.col - len(mytok.name)) + " , Row: " + str(
                        mytok.row) + " block order is: "+str(mytok.block_order)+" block number is: "+str(mytok.block_number)+" )")

    print("have " + str(errors) + " error(s)")
    for i in er:
        print(i)
        f.write(i+"\n")
    f.close()    
main()