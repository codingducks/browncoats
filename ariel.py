def in_ariel(town_size):
    board = []
    for row_num in range(town_size):
        row = []
        for col_num in range(town_size):
            row.append(". ")
        board.append(row)
  #{Alliance HQ
    for x in range(35,44): 
        board[0][x] = "--"
        board[10][x] = "--"
    for x in range(0,10):
        board[x][35] = "|"
        board[x][44] = "|"   
    for x in range(39,40):
        board[10][x] = "^^"            
    for x in range(1,10):
        for y in range(36,44):
            board[x][y] = "  "
  # }
  #{ BAR
    for x in range(30,44):
        board[town_size -1][x] = "--"
        board[town_size -6][x] = "--"
    for x in range(town_size-2,town_size-6,-1):
        board[town_size-16][x] = "--"
    board[town_size-16][town_size-1] = "-"
    for x in range(town_size - 2,town_size -6,-1):
        board[x][30] = "| "
    for x in range(town_size-1,town_size-16,-1):
        board[x][town_size-1] = "|"
        board[x][town_size-5] = "| "
    board[town_size-1][town_size-5] = "--"
    for x in range(town_size-2,town_size-6,-1):
        for y in range(town_size-2,town_size-15,-1):
            board[x][y] = "  "
    for x in range(town_size-5,town_size-16,-1):
        for y in range(town_size-2,town_size-5,-1):
            board[x][y] = "  "
    board[town_size-3][30] = "> "
    board[town_size-16][town_size-3] = "V-"
  # }

    board[40][25] = "@ "#arlo
  
    return board

def in_ariel_hq(town_size):
    board = []
    for row_num in range(town_size):
        row = []
        for col_num in range(town_size):
            row.append(". ")
        board.append(row)
    board[town_size -1][9] ="| "
    board[town_size -1][11] ="| "
    board[town_size -2][9] ="| "
    board[town_size -2][11] ="| "
    for x in range(town_size):
        board[13][x] = "##"
    board[13][10] = "~"
    board[13][9] = "#["
    board[13][11] = "]#"
    board[14][11] = "@ "
    return board

def in_bar(town_size):
    board = []
    for row_num in range(town_size):
        row = []
        for col_num in range(town_size):
            row.append(". ")
        board.append(row)
    for x in range(0,25):
        for y in range(0,25):
            board[x][y] = "  "
    for x in range(18,27):
        board[x][27] = "# "
    for x in range(16,27):
        board[27][x] = "##"
    board[27][27] = "# "
    for x in range(25,27):
     #   board[17][x] = "##"
        board[x][16] = "# "
    board[17][26] = "##"
    board[17][27] = "# "
    board[21][26] = "@ "
    board[town_size-3][0] = "__"
    board[town_size-5][0] = "__" 
    board[town_size-3][1] = "__"
    board[town_size-5][1] = "__"
    board[1][town_size-3] = "| "
    board[1][town_size-5] = "| " 
    board[0][town_size-3] = "| "
    board[0][town_size-5] = "| " 
    
    return board
