# Matrix (4*4) + 1 
arr = ["x1" , "x2" , "x3" , "x4",
        "x5" , "x6" , "x7" , "x8",
        "x9" , "x10" , "x11" , "x12",
        "x13" , "x14" , "x15" , "x16" , "x_final"]

def main (n):
    
    ''' 

    xn is position in matrix. 
    x_final is stop position .

    '''

    print("Exit program. (b)")
    r = False
    arr[int(n)-1] = "O"
    if n == "1":
        # ROS x,y,z,w
        r = True
    
    return r 
        
if __name__ == '__main__':
    while(1):
        print("********** EGAT WAREHOUSE **********\n") 
        print(f"\t|{arr[0]} | {arr[4]} | {arr[8]}  | {arr[12]} |\t")
        print(f"\t|{arr[1]} | {arr[5]} | {arr[9]} | {arr[13]} |\t")
        print(f"\t|{arr[2]} | {arr[6]} | {arr[10]} | {arr[14]} |\t")
        print(f"\t|{arr[3]} | {arr[7]} | {arr[11]} | {arr[15]} |\t\n")
        print(f"\t\t -- {arr[16]}--")
        user = input("Enter point (1-16) : ")
        if (user == "E" or user == "e") : break
        r = main(user)
        print(arr)

        if (r):
            print("Done")
            arr[int(user)-1] = f"x{user}"

        else:
            print("Not Done.")