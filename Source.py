import pygame
import numpy as np
import random
import math
import time

pygame.init()

WIDTH, HEIGHT = 600, 600
BOARD_SIZE = 8
CELL_SIZE = WIDTH // BOARD_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DELAY = 0.5

QUEEN_IMAGE = pygame.image.load("queen.png")
QUEEN_IMAGE = pygame.transform.scale(QUEEN_IMAGE, (CELL_SIZE, CELL_SIZE))

def draw_board(board):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("8-Queens Problem")
    screen.fill(WHITE)
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            if board[row] == col:
                screen.blit(QUEEN_IMAGE, (col * CELL_SIZE, row * CELL_SIZE))
    pygame.display.update()
    time.sleep(DELAY)

def generate_initial_board():
    return np.random.randint(0, BOARD_SIZE, BOARD_SIZE)

def count_conflicts(board):
    conflicts = 0
    for i in range(BOARD_SIZE):
        for j in range(i + 1, BOARD_SIZE):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def hill_climbing():
    board = generate_initial_board()
    print("Initial board: ", board)
    while True:
        draw_board(board)
        current_conflicts = count_conflicts(board)
        print("Current board: ", board, " Conflicts: ", current_conflicts)
        neighbors = []
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row] != col:
                    new_board = board.copy()
                    new_board[row] = col
                    neighbors.append((new_board, count_conflicts(new_board)))
        best_neighbor = min(neighbors, key=lambda x: x[1])
        if best_neighbor[1] >= current_conflicts:
            return board
        board = best_neighbor[0]

def simulated_annealing():
    board = generate_initial_board()
    print("Initial board: ", board)
    temp = 100.0
    cooling_rate = 0.99
    while temp > 0.1:
        draw_board(board)
        print("Current board: ", board, " Conflicts: ", count_conflicts(board), " Temperature: ", temp)
        new_board = board.copy()
        row1, row2 = random.sample(range(BOARD_SIZE), 2)
        new_board[row1], new_board[row2] = new_board[row2], new_board[row1]
        delta = count_conflicts(new_board) - count_conflicts(board)
        if delta < 0:
            board = new_board
        else:
            probability = math.exp(-delta / temp)
            if random.uniform(0, 1) < probability:
                board = new_board
                print("Bad move accepted with probability: ", probability)
        temp *= cooling_rate
    return board
def local_beam_search(k):
    boards = [generate_initial_board() for _ in range(k)]
    print("Initial boards: ", boards)
    while True:
        boards.sort(key=count_conflicts)
        draw_board(boards[0])
        print("Current best board: ", boards[0], " Conflicts: ", count_conflicts(boards[0]))
        if count_conflicts(boards[0]) == 0:
            return boards[0]
        successors = []
        for board in boards:
            for row in range(BOARD_SIZE):
                for col in range(BOARD_SIZE):
                    if board[row] != col:
                        new_board = board.copy()
                        new_board[row] = col
                        successors.append((new_board, count_conflicts(new_board)))
        successors.sort(key=lambda x: x[1])
        boards = [s[0] for s in successors[:k]]

def main():
    while True:
        print("\n8-Queens Problem Solver")
        print("1. Hill Climbing")
        print("2. Simulated Annealing")
        print("3. Local Beam Search")
        print("4. Exit")
        choice = input("Enter your choice : ")

        if choice == "1":
            pygame.init()
            board = hill_climbing()
            print("Final Hill Climbing Solution :", board)
            pygame.quit()
        elif choice == "2":
            pygame.init()
            board = simulated_annealing()
            print("Final Simulated Annealing Solution :", board)
            pygame.quit()
        elif choice == "3":
            k = int(input("Enter the value of k for Local Beam Search : "))
            pygame.init()
            board = local_beam_search(k)
            print("Final Local Beam Search Solution : ", board)
            pygame.quit()
        elif choice == "4":
            break
        else:
            print("Enter Correct Choice...")

if __name__ == "__main__":
    main()
