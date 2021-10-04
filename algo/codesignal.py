#!/usr/bin/env python3

import random

NUMS = '０１２３４５６７８９ＡＢＣＤＥＦ' # FULLWIDTH LATIN
LETS = 'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐ' # SMALL LETTERS
TILE = '＇'
SIZE = 16

class String:
    def __init__(self, str): self.str = str
    def bold(self):  return f"\033[1m{self.str}\033[22m"
    def flip(self):  return f"\033[7m{self.str}\033[27m"
    def red(self):   return f"\033[31m{self.str}\033[0m"
    def green(self): return f"\033[32m{self.str}\033[0m"
    def brown(self): return f"\033[33m{self.str}\033[0m"
    def blue(self):  return f"\033[34m{self.str}\033[0m"
    def cyan(self):  return f"\033[36m{self.str}\033[0m"
    def gray(self):  return f"\033[37m{self.str}\033[0m"
    def bgred(self): return f"\033[41m{self.str}\033[0m"

 
class Cell:
    def __init__(self, has_mine=False):
        self.has_mine = has_mine
        self.revealed = False
        self.exploded = False
        self.count = 0
 
    def __str__(self):
        if not self.revealed:
            return String(TILE).flip()
        elif self.has_mine:
            return String('＊').bgred() if self.exploded else String(String('＊').flip()).blue()
        elif self.count == 0:
            return String(TILE).gray()
        elif self.count == 1:
            return String(String(NUMS[self.count]).bold()).cyan()
        elif self.count == 2:
            return String(String(NUMS[self.count]).bold()).green()
        else:
            return String(String(NUMS[self.count]).bold()).red()


class Board:
    def __init__(self, num_mines=SIZE):
        self.board = [[0] * SIZE for _ in range(SIZE)]
        self.to_do = SIZE * SIZE - num_mines
        nums = list(range(SIZE * SIZE))
        random.shuffle(nums)
        candidates = set(nums[:num_mines])
        for one in range(SIZE):
            for two in range(SIZE):
                comp = ((SIZE * one) + (two % SIZE)) in candidates
                self.board[one][two] = Cell(comp)
        
        for one in range(SIZE):
            for two in range(SIZE):
                cell = self.board[one][two]
                if not cell.has_mine:
                    cell.count = self.calculate(one, two)
 
    def render(self):
        print('\x1B')
        print('\n   💣 MINE SWEEPER\n', end='')
        print(String('\n ｀').brown(), end='')
        for n in range(SIZE):
            print(String(LETS[n]).brown(), end='')
        print('\n')
        for r, row in enumerate(self.board):
            print(' ' + String(NUMS[r]).brown(), end='')
            for cell in row:
                print(f"{cell}", end='')
            print('')

    # calculates the number of neighbors containing a mine
    def calculate(self, x, y) -> int:
        # *TODO: implement this method
        delta1 = [-1, 0, 1]
        delta2 = [-1, 0, 1]
        ans = 0
        for i in delta1:
            for j in delta2:
                if (x+i) >= 0 and (x+i) < SIZE and (y+j) >= 0 and (y+j) < SIZE:
                    if (i,j) != (0,0):
                        cell = self.board[x+i][y+j]
                        if cell.has_mine:
                            ans += 1
        return ans
                        
 
    # reveals the cell (x, y),
    # if its count is 0, then reveals all its neighbors,
    # if any of them also has count = 0, its neighbors are also revealed, and so on.
    def cascade(self, x, y):
        # *TODO: implement this method
        cell = self.board[x][y]
        if cell.revealed:
            return
        # reveal the cell first
        cell.revealed = True
        self.to_do -= 1
            
        # has number -> "boundry"
        if cell.count > 0:
            return
         
        # has count == 0
        delta1 = [-1, 0, 1]
        delta2 = [-1, 0, 1]
        for i in delta1:
            for j in delta2:
                if (x+i) >= 0 and (x+i) < SIZE and (y+j) >= 0 and (y+j) < SIZE:
                    if (i, j) != (0, 0):
                        cell = self.board[x+i][y+j]
                        if not cell.revealed:
                            self.cascade(x+i, y+j)
 
    def show_mines(self):
        for one in range(SIZE):
            for two in range(SIZE):
                cell = self.board[one][two]
                if cell.has_mine:
                    cell.revealed = True

        self.render()
 
    def check(self, str):
        y = ord(str[0]) - 97
        x = ord(str[1]) - 55
        if x < 10:
            x += 7
        if x not in range(SIZE) or y not in range(SIZE):
            print('\n  Invalid input.\n')
            return
        cell = self.board[x][y]
        if cell.has_mine:
            cell.exploded = True
            self.show_mines()
            print('\n You lost!\n')
            exit(0)
        elif not cell.revealed:
            self.cascade(x, y)
            if self.to_do < 1:
                self.show_mines()
                print('\n You won!\n')
                exit(0)

def r():
    myboard = Board()
    while True:
        myboard.render()
        print('\n > ', end='')
        myboard.check(input())
        print('\n')
 
r()
