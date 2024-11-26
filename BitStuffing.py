# done
# done
def bit_stuffing(): 
    input_str = input("Enter the string: ") 
    flag = "01111110" 
    res = flag 
    onecnt = 0 
    for ch in input_str: 
        if ch == '1': 
            onecnt += 1 
            res += ch 
            if onecnt == 5: 
                res += '0' 
                onecnt = 0 
        else: 
            res += ch 
            onecnt = 0 
    res += flag 
    print("Stuffed String:", res) 
bit_stuffing() 