import tkinter as tk
from board import TicTacToeBoard


class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.board = TicTacToeBoard()
        self.current_player = 'X'

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', font=('normal', 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.board.make_move(row, col, self.current_player):
            self.buttons[row][col].config(text=self.current_player)
            if self.board.is_winner(self.current_player):
                print(f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.board.is_board_full():
                print("It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        self.board.reset_board()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')
        self.current_player = 'X'

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
