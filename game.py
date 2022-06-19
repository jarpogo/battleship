import board
import ship


def main():
    my_board = board.Board(8)

    my_board.print_board()
    my_board.update_tile(2, 3, True)
    my_board.update_tile(2, 3, True)
    my_board.update_tile(3, 3, False)

    my_board.print_board()


if __name__ == "__main__":
    main()
