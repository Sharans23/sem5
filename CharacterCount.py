# done

def character_count():

    frame=int(input("Enter no. of frames:"))
    transmitted_message=''

    for i in range(0,frame):
        data=input(f"Enter string {i+1}:")
        char_count=str(len(data)+1)+data
        transmitted_message+=char_count

    return transmitted_message