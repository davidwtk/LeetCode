class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # naive solution
        # Store entries in an array and check if there is a duplicate. If not then fill that spot
        # Check all 3 conditions: run through each list and check if any duplicates across row
        # Check each column
        # Check each box

        # Check each row of the board
        
        for i in range(9):
            test = [0] * 10
            for j in range(9):
                entry = board[i][j]
                if entry == ".":
                    continue
                
                elif int(entry) == test[int(entry)]:
                    return False
                else:
                    test[int(entry)] = int(entry)
        
        # Check each column of the board
        
        for i in range(9):
            test = [0] * 10
            for j in range(9):
                entry = board[j][i]
                if entry == ".":
                    continue
                elif int(entry) == test[int(entry)]:
                    return False
                else:
                    test[int(entry)] = int(entry)
        
        # Check each box in the board
        for l in range(0, 9, 3):
            for k in range(0, 9, 3):
                test = [0] * 10
                for i in range(l, l + 3):
                    for j in range(k, k + 3):
                        entry = board[i][j]
                        if entry == ".":
                            continue
                        elif int(entry) == test[int(entry)]:
                            return False
                        else:
                            test[int(entry)] = int(entry)
        return True