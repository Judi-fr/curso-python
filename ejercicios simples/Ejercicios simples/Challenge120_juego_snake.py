from tkinter import *
from random import randint
from PIL import Image, ImageTk


movement = 20
steps_per_sec = 10
speed = 1100 // steps_per_sec


class Snake(Canvas):
    def __init__(self):
        super().__init__(
            width=700, 
            height=700, 
            background='#53ff1a', 
            highlightthickness=0
        )

        self.snake_pos = [(100, 80), (80, 100), (80, 100)]
        self.food_pos = self.set_new_food_pos()
        self.direction = 'Right'

        self.score = 0

        self.load_img()
        self.create_objects()

        self.bind_all('<Key>', self.on_key_press)

        self.pack()

        self.after(speed, self.perform_actions)

    def load_img(self):
        try:
            self.snake_body = ImageTk.PhotoImage(Image.open('game.png'))
            self.food = ImageTk.PhotoImage(Image.open('game.png'))
        except IOError as error:
            ws.destroy()
            raise

    def create_objects(self):
        self.create_text(
            35, 
            12, 
            text=f'Score: {self.score}', 
            tag='score', 
            fill='black', 
            font=10
        )

        for x_position, y_position in self.snake_pos:
            self.create_image(
                x_position, 
                y_position, 
                image=self.snake_body, 
                tag='snake'
            )

        self.create_image(
            *self.food_pos, 
            image=self.food, 
            tag='food'
            )
        self.create_rectangle(
            7, 
            27, 
            690, 
            690, 
            outline='#d9d8d7'
            )

    def finish_game(self):
        self.delete(ALL)
        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2,
            text=f'Game over! You have scored {self.score}!',
            fill='black',
            font=20
        )

    def consume_food(self):
        if self.snake_pos[0] == self.food_pos:
            self.score += 10
            self.snake_pos.append(self.snake_pos[-1])

            self.create_image(
                *self.snake_pos[-1], 
                image=self.snake_body, 
                tag='snake'
            )
            self.food_pos = self.set_new_food_pos()
            self.coords(
                self.find_withtag('food'), 
                *self.food_pos
                )

            score = self.find_withtag('score')
            self.itemconfigure(
                score, 
                text=f'Score: {self.score}', 
                tag='score'
                )
    
    def boundry(self):
        head_x_position, head_y_position = self.snake_pos[0]

        return (
            head_x_position in (0, 700)
            or head_y_position in (20, 700)
            or (head_x_position, head_y_position) in self.snake_pos[1:]
        )

    def snake_movement(self):
        head_x_position, head_y_position = self.snake_pos[0]

        if self.direction == 'Left':
            new_head_position = (head_x_position - movement, head_y_position)
        elif self.direction == 'Right':
            new_head_position = (head_x_position + movement, head_y_position)
        elif self.direction == 'Down':
            new_head_position = (head_x_position, head_y_position + movement)
        elif self.direction == 'Up':
            new_head_position = (head_x_position, head_y_position - movement)

        self.snake_pos = [new_head_position] + self.snake_pos[:-1]

        for segment, position in zip(self.find_withtag('snake'), self.snake_pos):
            self.coords(segment, position)

    def on_key_press(self, e):
        new_direction = e.keysym

        all_directions = (
            'Up', 
            'Down', 
            'Left', 
            'Right'
            )
        opposites = (
            {'Up', 'Down'}, 
            {'Left', 'Right'}
            )

        if (
            new_direction in all_directions
            and {new_direction, self.direction} not in opposites
        ):
            self.direction = new_direction

    def perform_actions(self):
        if self.boundry():
            self.finish_game()

        self.consume_food()
        self.snake_movement()

        self.after(speed, self.perform_actions)

    def set_new_food_pos(self):
        while True:
            x_position = randint(1, 29) * movement
            y_position = randint(3, 30) * movement
            food_pos = (x_position, y_position)

            if food_pos not in self.snake_pos:
                return food_pos


ws = Tk()
ws.title('PythonGuides - Snake Game')
ws.resizable(False, False)

board = Snake()

ws.mainloop()











exit()
import tkinter as tk
import random

# Configuración de la ventana del juego
WIDTH = 500
HEIGHT = 500

# Configuración de la serpiente y la comida
SNAKE_SIZE = 10
FOOD_SIZE = 10

# Configuración de los movimientos de la serpiente
MOVEMENT_INCREMENT = 10
MOVEMENT_INTERVAL = 100
print("https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/key-names.html")
class SnakeGame(tk.Canvas):
    def __init__(self):
        super().__init__(width=WIDTH, height=HEIGHT, background="black", highlightthickness=0)
        print(WIDTH, HEIGHT)
        self.snake_positions = [(100, 100), (90, 100), (80, 100)]
        self.food_position = self.set_new_food_position()
        self.direction = "Right"
        self.bind_all("<Key>", self.on_key_press)
        self.score = 0
        self.score_text = self.create_text(50, 10, text=f"Score: {self.score}", tag="score", fill="#fff", font=("Arial", 14))
        self.game_loop()
        # ~ self.mainloop()
    def game_loop(self):
        self.move_snake()
        if self.check_collisions():
            self.end_game()
            return
        self.update_score()
        self.after(MOVEMENT_INTERVAL, self.game_loop)

    def move_snake(self):
        head_x, head_y = self.snake_positions[0]
        if self.direction == "Left":
            new_head_position = (head_x - MOVEMENT_INCREMENT, head_y)
        elif self.direction == "Right":
            new_head_position = (head_x + MOVEMENT_INCREMENT, head_y)
        elif self.direction == "Up":
            new_head_position = (head_x, head_y - MOVEMENT_INCREMENT)
        elif self.direction == "Down":
            new_head_position = (head_x, head_y + MOVEMENT_INCREMENT)
        self.snake_positions = [new_head_position] + self.snake_positions[:-1]
        for segment, position in zip(self.find_withtag("snake"), self.snake_positions):
            self.coords(segment, position)
    
    def on_key_press(self, e):
        new_direction = e.keysym
        all_directions = ("Up", "Down", "Left", "Right")
        opposites = ({"Up", "Down"}, {"Left", "Right"})
        if (new_direction in all_directions and {new_direction, self.direction} not in opposites):
            self.direction = new_direction

    def check_collisions(self):
        head_x, head_y = self.snake_positions[0]
        return (head_x in (0, WIDTH) or
                head_y in (20, HEIGHT) or
                (head_x, head_y) in self.snake_positions[1:])

    def set_new_food_position(self):
        while True:
            x, y = random.randint(0, WIDTH), random.randint(20, HEIGHT)
            food_position = (x, y)
            if food_position not in self.snake_positions:
                return food_position

    def update_score(self):
        new_food_position = self.check_food_collision()
        if new_food_position:
            self.create_rectangle(*new_food_position, *new_food_position, fill="#fff", tag="food")
            self.snake_positions.append(self.snake_positions[-1])
            self.food_position = self.set_new_food_position()
            self.score += 10
            self.itemconfig(self.find_withtag("score"), text=f"Score: {self.score}")


    def check_food_collision(self):
        if self.snake_positions[0] == self.food_position:
            self.delete("food")
            return self.set_new_food_position()

    def end_game(self):
        self.delete(tk.ALL)
        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2,
            text=f"Game Over. Score: {self.score}",
            fill="#fff",
            font=("Arial", 24),
            tag="gameover"
        )
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Snake Game")
    root.resizable(False, False)
    game = SnakeGame()
    game.pack()
    root.mainloop()
x=SnakeGame()
    # ~ self.create_text(WIDTH / 2, HEIGHT / 2, text=f"Game Over! Final Score: {self.score}", fill="#fff", font=("Arial", 14))import tkinter as tk
# ~ import random

# ~ # configuración de la ventana principal
# ~ ventana = tk.Tk()
# ~ ventana.title("Snake")
# ~ ventana.resizable(False, False)

# ~ # configuración del tablero
# ~ tablero = tk.Canvas(ventana, width=300, height=300, bg="black")
# ~ tablero.pack()

# ~ # configuración del jugador
# ~ jugador = tablero.create_rectangle(10, 10, 20, 20, fill="white")
# ~ x = 0
# ~ y = 0

# ~ # función de movimiento del jugador
# ~ def mover(event):
    # ~ global x, y
    # ~ tecla = event.keysym
    # ~ if tecla == "Up":
        # ~ x = 0
        # ~ y = -10
    # ~ elif tecla == "Down":
        # ~ x = 0
        # ~ y = 10
    # ~ elif tecla == "Left":
        # ~ x = -10
        # ~ y = 0
    # ~ elif tecla == "Right":
        # ~ x = 10
        # ~ y = 0

