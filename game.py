def sum(x,y,z):
    return x+y+z

def printboard(xState,zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)

    print(f"{zero} | {one} | {two}")
    print("------------")
    print(f"{three} | {four} | {five}")
    print("------------")
    print(f"{six} | {seven} | {eight}")

def win(xState,zState):
    w=[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in w:
        if (sum(xState[i[0]],xState[i[1]],xState[i[2]])==3):
            print("x won")
            return 1
        if(sum(zState[i[0]], zState[i[1]], zState[i[2]]) == 3):
            print("O won")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    chance=1
    print("Welcome to Tic Tac Toe")
    while(True):
        printboard(xState,zState)
        if chance==1:
            print("x turn")
            x=int(input())
            xState[x]=1
        else:
            print("o turn")
            o=int(input())
            zState[o]=1
        
        c=win(xState,zState)
        if(c != -1):
            print("match over")
            break
        chance=1-chance 
