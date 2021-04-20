from tkinter import *
#TODO: change import method, to from tkinter import module
# Constants
CANVAS_SIZE = 600
FIGURE_SIZE = 200
RATIO = CANVAS_SIZE // FIGURE_SIZE
BG_COLOR = "white"
EMPTY = None

# Players setup
X = "player 1"
O = "player 2"
FIRST_PLAYER = X
class Board(Tk):
    def __init__(self, start_player) :
        super().__init__()
        self.canvas = Canvas(height=CANVAS_SIZE, width=CANVAS_SIZE, bg=BG_COLOR)
        self.canvas.pack()
        self.figure_size = FIGURE_SIZE
        self.current_player = start_player
        self.canvas.bind("<Button-1>", self.click_event)
        self.board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    def draw_winner_line(self, c_player) :
        s1, s2, f1, f2 = self.find_winner_coordinates(c_player)
        self.canvas.create_line(s1 * FIGURE_SIZE, s2 * FIGURE_SIZE, f1 * FIGURE_SIZE, f2 * FIGURE_SIZE, fill="yellow", width=20)
    
    def find_winner_coordinates(self, player) :
        index_s = 0
        index_f = 0
        for y in range(3) :
            if self.board[y] == [player, player, player] :
                print("1")
                return y + 0.5, 0, y + 0.5, 3
            elif self.board[0][y] == self.board[1][y] == self.board[2][y] == player :
                print("2")
                return 0, y + 0.5, 3, y + 0.5
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player :
            print("3")
            return 0, 0, 3, 3
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == player :
            print("4")
            return 0, 3, 3, 0
        return index_s, index_f
    def winner(self, player=None) :
        """Display end game text depends on player attribute
        and shutdown the game"""
        center = CANVAS_SIZE // 2
        if player :
            text = f"Winner: {player}"
            self.draw_winner_line(player)
        else :
            text = "Winner is friendship!"
        self.canvas.create_text(center, center, text=text, fill="blue", font="Arial 50")
        self.canvas.unbind('<Button-1>')
    # def check_winner(self) :
    #     # if self.board[0][0] == self.board[0][1] == self.board[0][2] != None or self.board[1][0] == self.board[1][1] == self.board[1][2] != None or self.board[2][0] == self.board[2][1] == self.board[2][2] != None:
    #     for i in range(3) :
    #         if self.board[i][0] == self.board[i][1] == self.board[i][2] != None :
    #             self.winner(self.board[i][0])
    #         if self.board[0][i] == self.board[1][i] == self.board[2][i] != None :
    #             self.winner(self.board[0][i])
    #     if self.board[0][0] == self.board[1][1] == self.board[2][2] != None or self.board[0][2] == self.board[1][1] == self.board[2][0] != None :
    #         self.winner(self.board[1][1])
    #     l = []
    #     for i in range(3) :
    #         for j in range(3) :
    #             l.append(self.board[i][j])
    #     if not None in l :
    #         self.winner()
    def check_win(self, board, player) :
        for y in range(3) :
            if board[y] == [player, player, player] :
                return True
        for x in range(3) :
            if board[0][x] ==  board[1][x] == board[2][x] == player :
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player :
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == player :
            return True
        return False
    def check_draw(self, board) :
        for row in board :
            if EMPTY in row :
                return False
        return True
    def click_event(self, event) :
        x_coord = event.x // FIGURE_SIZE
        y_coord = event.y // FIGURE_SIZE
        if x_coord > CANVAS_SIZE - 1 :
            x_coord = event.x // FIGURE_SIZE - 1
        if y_coord > CANVAS_SIZE - 1 :
            y_coord = event.y // FIGURE_SIZE - 1
        self.make_move(x_coord, y_coord)
        # print(x_coord, y_coord)
    def make_move(self, x, y) :
        position = {0: 0, 1: 200, 2: 400, 3: 400}
        current_player = self.current_player

        if self.board[x][y] == EMPTY :
            self.update_board(x, y)
            self.change_player()
            if current_player == X :
                self.render_cross(position[x], position[y])
            elif current_player == O :
                self.render_circle(position[x], position[y])
            # self.check_winner()
        if self.board[x][y] == EMPTY :
            self.update_board(x, y)
    def change_player(self) :
        if self.current_player == X :
            self.current_player = O
        else :
            self.current_player = X
    def update_board(self, x, y) :
        c_player = self.current_player
        self.board[x][y] = c_player
        print(self.board)
        if self.check_win(self.board, c_player) :
            self.winner(c_player)
        elif self.check_draw(self.board) :
            self.winner()
    def build_grid(self, grid_color) :
        x = CANVAS_SIZE // RATIO
        y1 = 0
        y2 = CANVAS_SIZE
        for _ in range(RATIO - 1) :
            self.canvas.create_line(x, y1, x, y2, fill=grid_color)
            self.canvas.create_line(y1, x, y2, x, fill=grid_color)
            x += CANVAS_SIZE // RATIO
    def render_cross(self, posX, posY) :
        f_size = self.figure_size
        self.canvas.create_line(posX, posY, posX + f_size, posY + f_size, fill="red", width=5)
        self.canvas.create_line(posX + f_size, posY, posX, posY + f_size, fill="red", width=5)
    def render_circle(self, posX, posY) :
        """Magic num: 5 it's a gap between edges and figure render O on field"""
        f_size = self.figure_size - 5
        self.canvas.create_oval(posX + 5, posY + 5, posX + f_size, posY + f_size, outline="green", width=5)
# Initialize game object and execute require methods
game_v1 = Board(start_player=FIRST_PLAYER)
game_v1.build_grid("black")
#Testing
# game_v1.render_cross(0, 0)
# game_v1.render_cross(FIGURE_SIZE, FIGURE_SIZE)
# game_v1.render_cross(FIGURE_SIZE * 2, FIGURE_SIZE * 2)
# game_v1.render_circle(FIGURE_SIZE, 0)
# game_v1.winner("Test")
#TEST
# test_board = [[EMPTY, EMPTY, EMPTY], [X, X, X], [EMPTY, EMPTY, EMPTY]]
# game_v1.board = test_board
# Run the game
game_v1.mainloop()
