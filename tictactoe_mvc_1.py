from dataclasses import dataclass, field
import random


# MODEL


@dataclass
class Desk:
    board: list = field(default_factory=lambda: ['', ' ', ' ', ' ', '_', '_', '_', '_', '_', '_'])
    win_conditions: tuple = field(default_factory=lambda: ((1, 2, 3), (4, 5, 6), (7, 8, 9),
                                                           (1, 4, 7), (2, 5, 8), (3, 6, 9),
                                                           (1, 5, 9), (3, 5, 7))
                                  )
    player_letter: str = 'X'
    ai_letter: str = 'O'
    is_space_free: bool = True


@dataclass
class GameState:
    play_again: bool = True
    result: str = ''


# VIEW

class View:
    def draw_board(self, board, game_state):
        print(f"{board[7]}|{board[8]}|{board[9]}\n"
              f"{board[4]}|{board[5]}|{board[6]}\n"
              f"{board[1]}|{board[2]}|{board[3]}")

        if game_state.result != '':
            print(game_state.result)


# Controller

@dataclass
class Controller:
    #    game_state: GameState
    #    desk: Desk

    def input_player_letter(self):  # Выбор чем играть, Х или О
        self.letter = ''
        while not (self.letter == 'X' or self.letter == 'O'):
            print('Выбор чем играть, Х или О:')
            self.letter = input().upper()
        if self.letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def first_turn_decide(self):  # Кто ходит первым
        if random.randint(0, 1) == 0:
            return 'Computer'
        else:
            return 'Human'

    def make_move(self, board, letter, cell_number):
        board[cell_number] = letter

    def is_winner(self, board, letter):
        for i in self.desk.win_conditions:
            if board[i[0]] == board[i[1]] == board[i[2]] == letter:
                return True
        else:
            return False

    def get_board_copy(self):  # Дублирование игрового поля
        board_copy = self.desk.board.copy()
        return board_copy

    def is_space_free(self, board, move):  # Проверка, свободна ли клетка
        return board[move] == ' ' or board[move] == '_'

    def random_turn_from_list(self, board, moves_list):  # РАндомный выбор клетки из списка возможных ходов
        available_moves = []
        for i in moves_list:
            if self.is_space_free(board, i):
                available_moves.append(i)
        if len(available_moves) != 0:
            return random.choice(available_moves)
        else:
            return None

    def player_move(self, board):  # ход игрока
        print('Next turn (1-9):')
        move = input()
        while move not in str(list(range(1, 10))) or not self.is_space_free(board, int(move)):
            print('Cell is not empty or wrong number. Next turn (1-9):')
            move = input()
        return int(move)

    def get_computer_move(self, ai_letter):  # ИИ ход компьютера
        for i in range(1, 10):  # Проверка приведет ли ход ИИ к победе, делает этот ход
            board_copy = self.get_board_copy()
            if self.is_space_free(board_copy, i):
                self.make_move(board_copy, ai_letter, i)
                if self.is_winner(board_copy, ai_letter):
                    return i

        for i in range(1, 10):  # Проверка клеток, приводящих к победе игрока
            board_copy = self.get_board_copy()
            if self.is_space_free(board_copy, i):
                self.make_move(board_copy, self.desk.player_letter, i)
                if self.is_winner(board_copy, self.desk.player_letter):
                    return i

        move = self.random_turn_from_list(self.desk.board, [1, 3, 7, 9])
        if move is not None:
            return move

        if self.is_space_free(self.desk.board, 5):
            return 5

        return self.random_turn_from_list(self.desk.board, [2, 4, 8, 6])

    def is_board_full(self, board):
        for i in range(1, 10):
            if self.is_space_free(board, i):
                return False
        return True

    def start_the_game(self):
        self.game_state = GameState()
        self.desk = Desk()
        self.desk.player_letter, self.desk.ai_letter = self.input_player_letter()

    def end_game(self):
        print()
        while True:
            question = input('Play again Y/N:')
            if question.lower().startswith('y'):
                return True
            if question.lower().startswith('n'):
                return False


if __name__ == '__main__':
    print('Game TicTacToe')
    cnt = Controller()
    view = View()
    while GameState.play_again is True:
        cnt.start_the_game()
        turn = cnt.first_turn_decide()
        print(f'Первым ходит {turn}')
        while cnt.game_state.result not in ['You win!', 'AI win!', 'Draw!']:
            if turn == 'Human':
                view.draw_board(cnt.desk.board, cnt.game_state)
                move = cnt.player_move(cnt.desk.board)
                cnt.make_move(cnt.desk.board, cnt.desk.player_letter, move)
                if cnt.is_winner(cnt.desk.board, cnt.desk.player_letter):
                    cnt.game_state.result = 'You win'
                    view.draw_board(cnt.desk.board, cnt.game_state)
                else:
                    if cnt.is_board_full(cnt.desk.board):
                        cnt.game_state.result = 'Draw'
                        view.draw_board(cnt.desk.board, cnt.game_state)
                    else:
                        turn = 'Computer'
            else:
                print('AI Turn')
                move = cnt.get_computer_move(cnt.desk.ai_letter)
                cnt.make_move(cnt.desk.board, cnt.desk.ai_letter, move)
                if cnt.is_winner(cnt.desk.board, cnt.desk.ai_letter):
                    cnt.game_state.result = 'AI win'
                    view.draw_board(cnt.desk.board, cnt.game_state)
                else:
                    if cnt.is_board_full(cnt.desk.board):
                        cnt.game_state.result = 'Draw'
                        view.draw_board(cnt.desk.board, cnt.game_state)
                    else:
                        turn = 'Human'
        GameState.play_again = cnt.end_game()
