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
    def winner(self, player=None) :
        """Display end game text depends on player attribute
        and shutdown the game"""
        center = CANVAS_SIZE // 2
        if player :
            text = f"Winner: {player}"
        else :
            text = "Winner is friendship!"
        self.canvas.create_text(center, center, text=text, fill="blue", font="Arial 50")
        self.canvas.unbind('<Button-1>')
    def check_winner(self) :
        # if self.board[0][0] == self.board[0][1] == self.board[0][2] != None or self.board[1][0] == self.board[1][1] == self.board[1][2] != None or self.board[2][0] == self.board[2][1] == self.board[2][2] != None:
        for i in range(3) :
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != None :
                self.winner(self.board[i][0])
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != None :
                self.winner(self.board[0][i])
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != None or self.board[0][2] == self.board[1][1] == self.board[2][0] != None :
            self.winner(self.board[1][1])
        l = []
        for i in range(3) :
            for j in range(3) :
                l.append(self.board[i][j])
        if not None in l :
            self.winner()
    def click_event(self, event) :
        x_coord = event.x // FIGURE_SIZE
        y_coord = event.y // FIGURE_SIZE
        self.make_move(x_coord, y_coord)
        # print(x_coord, y_coord)
    def make_move(self, x, y) :
        position = {0: 0, 1: 200, 2: 400}
        current_player = self.current_player
        if self.board[y][x] == EMPTY :
            if current_player == X :
                self.render_cross(position[x], position[y])
                self.current_player = O
                self.board[y][x] = X
            elif current_player == O :
                self.render_circle(position[x], position[y])
                self.current_player = X
                self.board[y][x] = O
            self.check_winner()
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
# Run the game
game_v1.mainloop()
