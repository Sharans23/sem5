# done

def transmission():
    par=int(input('1) for even parity 0) for odd parity'))
    sentData=[]
    for i in range(4):
        sentData.append(int(input(f'enter bit {i+1}')))
    data=[0]*7
    
    data[2],data[4],data[5],data[6]=sentData[0],sentData[1],sentData[2],sentData[3]
    
    if par==1:
        data[0]=data[2]^data[4]^data[6]
        data[1]=data[2]^data[5]^data[6]
        data[3]=data[4]^data[5]^data[6]
    else:
        data[0]=1-(data[2]^data[4]^data[6])
        data[1]=1-(data[2]^data[5]^data[6])
        data[3]=1-(data[4]^data[5]^data[6])
    
    for i in range(len(data)):
        print(data[i],'')
        
def reception():
    par=int(input('1) for even parity 0) for odd parity'))
    data=[]
    for i in range(7):
        data.append(int(input(f'enter bit {i+1} : ')))
    ideal_data=[0]*4
    
    if par==1:
        ideal_data[0]=data[2]^data[4]^data[6]^data[0]
        ideal_data[1]=data[2]^data[5]^data[6]^data[1]
        ideal_data[2]=data[4]^data[5]^data[6]^data[3]
    else:
        ideal_data[0]=1-(data[2]^data[4]^data[6]^data[0])
        ideal_data[1]=1-(data[2]^data[5]^data[6]^data[1])
        ideal_data[2]=1-(data[4]^data[5]^data[6]^data[3])
    e=4*ideal_data[2]+2*ideal_data[1]+ideal_data[0]    
    
    if(e==0):
        print('no error')
    else:
        data[e-1]=1-data[e-1]
        for i in range(len(data)):
            print(data[i])
            
transmission()
reception()
    