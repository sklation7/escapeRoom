from picoboy import PicoBoy
import utime

# Constants
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64
BALL_SIZE = 4  # e.g., a 4x4 pixel ball
ACCEL_THRESHOLD = 0.3  # for detecting tilt
GAME_DELAY_MS = 50  # for game speed

# Maze Definition
maze_data = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1], # Row 1 (0-indexed)
    [1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1], # Row 2
    [1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1], # Row 3
    [1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1], # Row 4
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1], # Row 5
    [1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1], # Row 6 - Note: ensure path to exit
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]  # Row 7
]
CELL_WIDTH = SCREEN_WIDTH // len(maze_data[0]) # Should be 128 / 16 = 8
CELL_HEIGHT = SCREEN_HEIGHT // len(maze_data)   # Should be 64 / 8 = 8
start_pos = {"row": 1, "col": 1} # Example starting position (in maze grid coordinates)
end_pos = {"row": 6, "col": 14}   # Example ending position (in maze grid coordinates)

# PicoBoy Initialization
pb = PicoBoy()

# Player State
player_row = start_pos["row"]
player_col = start_pos["col"]

# Game Loop
while True:
    # Input
    ax = pb.xAcc()
    ay = pb.yAcc()

    # Movement Logic
    next_row, next_col = player_row, player_col

    # Tilting "down" (top of device downwards) makes ball move down screen
    if ay > ACCEL_THRESHOLD:
        next_row += 1
    # Tilting "up" (bottom of device downwards) makes ball move up screen
    elif ay < -ACCEL_THRESHOLD:
        next_row -= 1
    
    # Tilting "right" (right side of device downwards) makes ball move right
    if ax > ACCEL_THRESHOLD: # Accelerometer X-axis might be inverted depending on mounting
        next_col += 1
    # Tilting "left" (left side of device downwards) makes ball move left
    elif ax < -ACCEL_THRESHOLD:
        next_col -= 1

    # Boundary Check for player movement (maze grid coordinates)
    if next_row < 0:
        next_row = 0
    if next_row >= len(maze_data):
        next_row = len(maze_data) - 1
    if next_col < 0:
        next_col = 0
    if next_col >= len(maze_data[0]):
        next_col = len(maze_data[0]) - 1

    # Collision Detection
    if maze_data[next_row][next_col] == 0: # If it's a path
        player_row, player_col = next_row, next_col

    # Win Condition
    if player_row == end_pos["row"] and player_col == end_pos["col"]:
        pb.fill(1)  # White screen

        # Blink green LED
        for _ in range(3):
            pb.LED_GREEN.on()
            utime.sleep_ms(100)
            pb.LED_GREEN.off()
            utime.sleep_ms(100)
        pb.LED_GREEN.off() # Ensure LED is off

        win_text = "You Win!"
        # Using text_width for potentially more accurate centering if text changes
        text_width = len(win_text) * 8 # Approximate width of text for 8x8 font
        pb.text(win_text, (SCREEN_WIDTH - text_width) // 2, (SCREEN_HEIGHT - 8) // 2, 0) # Black text
        pb.show()
        utime.sleep_ms(2000)
        player_row, player_col = start_pos["row"], start_pos["col"]  # Reset to start

    # Rendering
    pb.fill(0)  # Clear screen to black

    # Draw maze
    for r in range(len(maze_data)):
        for c in range(len(maze_data[0])):
            if maze_data[r][c] == 1:  # If it's a wall
                pb.fill_rect(c * CELL_WIDTH, r * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT, 1) # White wall

    # Draw end point (small box within the cell)
    pb.rect(end_pos["col"] * CELL_WIDTH + (CELL_WIDTH // 4), 
            end_pos["row"] * CELL_HEIGHT + (CELL_HEIGHT // 4), 
            CELL_WIDTH // 2, CELL_HEIGHT // 2, 1) # White box

    # Draw start point (single pixel in the center of the cell)
    pb.pixel(start_pos["col"] * CELL_WIDTH + CELL_WIDTH // 2, start_pos["row"] * CELL_HEIGHT + CELL_HEIGHT // 2, 1)

    # Draw player (ball)
    # Ensure ball is drawn centered within its potential cell space if smaller than cell
    # For now, top-left aligned with BALL_SIZE dimensions
    pb.fill_rect(player_col * CELL_WIDTH, player_row * CELL_HEIGHT, BALL_SIZE, BALL_SIZE, 1) # White ball

    pb.show()

    # Delay
    utime.sleep_ms(GAME_DELAY_MS)
