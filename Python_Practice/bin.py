def make_list():
    result=[]
    in_val=0
    while in_val >= 0:
        in_val = int(input("enter integer(-quits):"))
        if in_val >= 0:
            result = result + [in_val] 
    return result

def main():
    col = make_list()
    print(col)
main()
