# done
# done
def byte_stuffing(): 
    input_str = input("Enter the string: ") 
    sflag = input("Enter the start flag: ") 
    eflag = input("Enter the end flag: ") 
    esc = input("Enter the escape character: ") 
    res = sflag 
    for ch in input_str: 
        if ch == sflag or ch == eflag or ch == esc: 
            res += esc 
        res += ch 
    res += eflag 
    print("Stuffed String:", res) 
byte_stuffing()
