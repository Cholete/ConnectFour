from ConnectFour import *

def main():
    c4 = ConnectFour([5,5])
    c4.print_board()

    is_game_over = False
    while not is_game_over:
        # get move
        move = input("Enter move[color, position]:")
        move_as_list = move.split(" ")

        # make the move
        c4.drop_piece(int(move_as_list[0]), int(move_as_list[1]))
        
        # print results
        c4.print_board()
        print("")

        # check if game is done
        is_game_over = c4.is_game_over()
    
    print("bye!")


    

main()
