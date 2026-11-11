import random
import tkinter as tk


CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
GAME_SPEED = 110


class SnakeGame:
	def __init__(self, root):
		self.root = root
		root.title("Snake")
		root.resizable(False, False)

		self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
		self.score_label.pack(pady=(8, 2))
		self.canvas = tk.Canvas(
			root,
			width=GRID_WIDTH * CELL_SIZE,
			height=GRID_HEIGHT * CELL_SIZE,
			bg="#151515",
			highlightthickness=0,
		)
		self.canvas.pack(padx=10, pady=5)
		self.message = tk.Label(root, text="Arrow keys to move · Space to pause · R to restart")
		self.message.pack(pady=(2, 8))

		root.bind("<Key>", self.on_key)
		self.reset()

	def reset(self):
		self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2),
					  (GRID_WIDTH // 2 - 1, GRID_HEIGHT // 2),
					  (GRID_WIDTH // 2 - 2, GRID_HEIGHT // 2)]
		self.direction = (1, 0)
		self.next_direction = self.direction
		self.score = 0
		self.paused = False
		self.game_over = False
		self.food = self.place_food()
		self.score_label.config(text="Score: 0")
		self.message.config(text="Arrow keys to move · Space to pause · R to restart")
		self.draw()
		self.tick()

	def place_food(self):
		empty = [
			(x, y)
			for x in range(GRID_WIDTH)
			for y in range(GRID_HEIGHT)
			if (x, y) not in self.snake
		]
		return random.choice(empty) if empty else None

	def on_key(self, event):
		key = event.keysym
		directions = {
			"Up": (0, -1),
			"Down": (0, 1),
			"Left": (-1, 0),
			"Right": (1, 0),
		}
		if key.lower() == "r":
			self.reset()
		elif key == "space" and not self.game_over:
			self.paused = not self.paused
			self.message.config(text="Paused · press Space to continue" if self.paused else
								"Arrow keys to move · Space to pause · R to restart")
			if not self.paused:
				self.tick()
		elif key in directions and not self.game_over and not self.paused:
			new_direction = directions[key]
			if new_direction != (-self.direction[0], -self.direction[1]):
				self.next_direction = new_direction

	def tick(self):
		if self.paused or self.game_over:
			return

		self.direction = self.next_direction
		head_x, head_y = self.snake[0]
		dx, dy = self.direction
		new_head = (head_x + dx, head_y + dy)
		growing = new_head == self.food
		body = self.snake if growing else self.snake[:-1]

		if (not 0 <= new_head[0] < GRID_WIDTH
				or not 0 <= new_head[1] < GRID_HEIGHT
				or new_head in body):
			self.game_over = True
			self.message.config(text=f"Game over! Score: {self.score} · Press R to restart")
			self.draw()
			return

		self.snake.insert(0, new_head)
		if growing:
			self.score += 1
			self.score_label.config(text=f"Score: {self.score}")
			self.food = self.place_food()
			if self.food is None:
				self.game_over = True
				self.message.config(text="You win! Press R to play again")
		else:
			self.snake.pop()

		self.draw()
		if not self.game_over:
			self.root.after(GAME_SPEED, self.tick)

	def draw(self):
		self.canvas.delete("all")
		if self.food:
			self.draw_cell(self.food, "#ef5350")
		for index, segment in enumerate(self.snake):
			self.draw_cell(segment, "#8bc34a" if index == 0 else "#4caf50")
		if self.game_over:
			self.canvas.create_text(
				self.canvas.winfo_reqwidth() // 2,
				self.canvas.winfo_reqheight() // 2,
				text="GAME OVER" if self.food is not None else "YOU WIN!",
				fill="white",
				font=("Arial", 24, "bold"),
			)

	def draw_cell(self, position, color):
		x, y = position
		inset = 2
		self.canvas.create_rectangle(
			x * CELL_SIZE + inset,
			y * CELL_SIZE + inset,
			(x + 1) * CELL_SIZE - inset,
			(y + 1) * CELL_SIZE - inset,
			fill=color,
			outline="",
		)


if __name__ == "__main__":
	window = tk.Tk()
	SnakeGame(window)
	window.mainloop()
