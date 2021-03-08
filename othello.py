#  -1: white, 1: black

import string
import random

import numpy as np


class Othello:
    #  盤面の初期化
    def __init__(self, size=8, order="random"):
        #  盤面のサイズ
        self.size = min(size, 10)
        self.board = np.zeros((self.size, self.size))

        #  初期の石を配置
        size_half = self.size // 2 - 1
        self.board[size_half, size_half] = -1
        self.board[size_half + 1, size_half + 1] = -1
        self.board[size_half + 1, size_half] = 1
        self.board[size_half, size_half + 1] = 1

        #  先攻後攻
        if order == "black":
            self.color = 1
        elif order == "white":
            self.color = -1
        else:
            random.seed()
            self.color = random.choice([-1, 1])

        #  現在の手番: black から
        self.order = 1

    #  盤面の表示
    def showBoard(self):
        rock = {-1: "O", 0: " ", 1: "X"}
        print("  " + " ".join(string.ascii_letters[: self.size]), end="\n\n")
        for i in range(self.size):
            print(str(i + 1) + " " + " ".join(list([rock[p] for p in self.board[i, :]])))

    #  1つの入力を完結させる関数
    def putStone(self):
        #  人なのか，
        #  置けるのかの確認

        #  石を置く

        #  ひっくり返す


if __name__ == "__main__":
    oth = Othello(8)
    oth.showBoard()
