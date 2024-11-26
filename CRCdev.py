def crc(data,divisor):
    dt = []
    for bit in data:
        dt.append(int(bit))
    divs=[]
    for bit in divisor:
        divs.append(int(bit))
    data_len=len(data)
    divs_len=len(divisor)
    
    for i in range(data_len-divs_len+1):
        if(dt[i]==1):
            for j in range(divs_len):
                dt[i+j]^=divs[j]
    rem=''.join(str(bit) for bit in dt[-(divs_len-1):])
    return rem
     
def transmit():
    ogdata=input('enter the data')
    divisor=input('enter the divisor')
    data=ogdata+'0'*(len(divisor)-1)
    rem=crc(data,divisor)
    ans=ogdata+rem
    print('Transmitted data:',ans)
    
def reception():
    data=input('enter the data')
    divisor=input('enter the divisor')
    rem=crc(data,divisor)
    error=0
    for bit in rem:
        if bit!='0':
            error=1
    if(error!=0):
        print('Error')
    else:
        print('No error')
        
transmit()
reception()

