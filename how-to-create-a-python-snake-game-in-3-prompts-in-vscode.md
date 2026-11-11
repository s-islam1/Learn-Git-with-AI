# How to Create a Python Snake Game in 3 Prompts in VS Code

This guide explains the Snake game in [`hello.py`](./hello.py): a small desktop game built with Python's built-in `tkinter` library. You can use the three prompts below with an AI assistant in VS Code to build it in understandable steps.

## What you'll build

The game opens a window with a grid, a snake, and a piece of food. Use the arrow keys to steer the snake, eat food to grow and earn points, avoid the walls and your own body, press Space to pause, and press R to restart.

## Before you start

- Install Python 3.
- Use a Python installation that includes `tkinter`. On macOS, the system Python or a Conda Python may include it, while some Python installations do not.
- Open a folder in VS Code and create `hello.py`.
- If you use an AI assistant, ask it to explain the code as it writes it. Review and run each step before asking for the next one.

## Prompt 1: Create the window and draw the game

Ask:

> Create a small Python Snake game in `hello.py` using only the standard-library `tkinter` and `random` modules. Start with a 30-by-20 grid and 20-pixel cells. Make a non-resizable window with a dark canvas, a score label, and a controls label. Represent the snake as a list of grid coordinates, draw it as green rectangles, and draw the food as a red rectangle. Explain each part briefly.

This establishes the display and the game's data:

- `CELL_SIZE`, `GRID_WIDTH`, and `GRID_HEIGHT` define the grid. The canvas is 600 by 400 pixels.
- `SnakeGame.__init__` creates the window contents and binds keyboard events.
- The snake is a list of `(x, y)` grid coordinates. Its first coordinate is the head.
- `draw` clears and redraws the canvas. `draw_cell` converts grid coordinates to pixel coordinates.
- `place_food` chooses a random grid cell that the snake does not occupy.

Run the file to check that the window and initial snake appear before adding movement.

## Prompt 2: Add movement, food, and collisions

Ask:

> Add the game loop to the existing `hello.py`. Move the snake one grid cell every 110 milliseconds with `root.after`. Handle arrow-key direction changes but reject an immediate 180-degree reversal. When the snake eats food, grow it, increase and display the score, and place new food in an empty cell. End the game if the snake hits a wall or itself. Keep drawing through the existing methods and explain the update order.

The game loop is `tick`:

1. Apply the queued direction.
2. Compute the next head coordinate.
3. Check whether it reaches the food.
4. Check for wall or body collisions. If the snake is not growing, its tail moves away during this turn, so moving into that old tail cell is allowed.
5. Add the new head. If it did not eat food, remove the tail; otherwise, increase the score and place more food.
6. Redraw and schedule the next tick.

The `next_direction` value queues input until the next movement tick. Comparing it with the opposite of the current direction prevents an immediate reversal into the snake itself.

## Prompt 3: Add controls and finish the game states

Ask:

> Finish the existing Snake game in `hello.py`: Space should pause and resume, R should reset the snake and score, and filling every grid cell should show a win message instead of trying to place more food. Show a game-over message on collisions, display an overlay on the canvas, and make sure the game loop stops while paused or after the game ends. Explain how to launch the game.

In the finished version:

- `on_key` toggles pause, resumes movement, resets the game, and handles valid direction keys.
- `reset` returns the snake, direction, score, and game state to their starting values, places food, redraws, and starts movement.
- If `place_food` finds no empty cell, it returns `None`; `tick` treats that as a win.
- `game_over` prevents further movement after a collision or win.
- `draw` displays the end-state overlay and the current food and snake.

## Run and play

From the VS Code terminal, run:

```bash
python3 hello.py
```

If that Python reports `No module named '_tkinter'`, choose or install a Python distribution that includes Tk support, then run the file with that interpreter. On macOS, a warning that the system Tk version is deprecated is informational; it is separate from whether the game window can open.

Controls:

| Key | Action |
| --- | --- |
| Arrow keys | Steer the snake |
| Space | Pause or resume |
| R | Restart |

## Try it with an AI assistant in VS Code

After each prompt, read the suggested changes, run the game, and ask the assistant to fix any error you actually observe. For example, share the exact traceback or describe what happens when you press a key. This makes the three prompts a guided build rather than a blind copy-and-paste exercise.
