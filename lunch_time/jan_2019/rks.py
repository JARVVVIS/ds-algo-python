

def isPossible(num,row,col,board):

    for i in range(row-1,0,-1):
        if board[i][col] == 1:
            return False
    
    for i in range(row+1,num):
        if board[i][col] == 1:
            return False
    
    for i in range(col-1,0,-1):
        if board[row][i] == 1:
            return False

    for i in range(col+1,num):
        if board[row][i] == 1:
            return False
    
    return True


def queenHelper(num,row,board,solution=[]):
    if(row==num):
        total = len(solution)
        print(total,end=' ')
        for i in solution:
            print(i,end=' ')
        print(' ')
        solution = []
        return


    for j in range(num):
        print(board[row][j])
        if(isPossible(num,row,j,board) and board[row][j]==0):
            board[row][j]=1
            solution.append(row+1)
            solution.append(j+1)
            queenHelper(num,row+1,board,solution)
            board[row][j]=0
        else:
            queenHelper(num,row+1,board,solution)    
    return
            


def main():
    t = int(input())
    while(t):
        num,k = [int(x) for x in input().split()]
        board = [[0 for i in range(num)] for i in range(num)]
        while(k):
            r,c =[int(x) for x in input().split()]
            board[r-1][c-1]=1
            k-=1
        queenHelper(num,0,board)
        t-=1




if __name__ == '__main__':
    main()