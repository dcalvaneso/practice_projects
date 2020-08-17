import random
import string

boardState = {
"r1": ["   ", "   ", "   "],
"r2": ["   ", "   ", "   "],
"r3": ["   ", "   ", "   "]
}

remaining_moves = ['r1c1', 'r1c2', 'r1c3', 'r2c1', 'r2c2', 'r2c3', 'r3c1', 'r3c2', 'r3c3']

def draw_TTT_board():
	print("    _c1_  _c2_  _c3_")
	print(f"r1| {boardState['r1'][0]} | {boardState['r1'][1]} | {boardState['r1'][2]} |")
	print("   +----+-----+-----+")
	print(f"r2| {boardState['r2'][0]} | {boardState['r2'][1]} | {boardState['r2'][2]} |")
	print("   +----+-----+-----+")
	print(f"r3| {boardState['r3'][0]} | {boardState['r3'][1]} | {boardState['r3'][2]} |")
	print("   +----------------+")
	
def get_player_move():
	row = int(input("In which row will you place your X? (enter 1-3): "))
	column = int(input("In which column will you place your X? (enter 1-3:) "))
	if row not in range(1, 4) or column not in range(1, 4):
		print("Invalid input. Please enter 1-3.")
		get_player_move()
	player_move = ['r', str(row), 'c', str(column)]
	player_move = "".join(player_move)
	remaining_moves.remove(player_move)
	update_board_state(row, column, ' X ')

def opponent_move():
	if len(remaining_moves) > 0:
		cpu_move = random.choice(remaining_moves)
		remaining_moves.remove(cpu_move)
		update_board_state(int(cpu_move[1]), int(cpu_move[3]), ' O ')
	else:
		print("Strange game. The only winning move is not to play.")

def update_board_state(row, column, side):
	if row == 1:
		if column == 1:
			boardState['r1'][0] = side
		elif column == 2:
			boardState['r1'][1] = side
		elif column == 3:
			boardState['r1'][2] = side
	elif row == 2:
		if column == 1:
			boardState['r2'][0] = side
		elif column == 2:
			boardState['r2'][1] = side
		elif column == 3:
			boardState['r2'][2] = side
	elif row == 3:
		if column == 1:
			boardState['r3'][0] = side
		elif column == 2:
			boardState['r3'][1] = side
		elif column == 3:
			boardState['r3'][2] = side
	draw_TTT_board()
	check_win_state()
	
#Fixed. Positive elif statements preclude verifying other win states. Changed to if statements.
def check_win_state():
	#Check horizontal 1
	if boardState['r1'][0] == ' X ' or boardState['r1'][0] == ' O ':
		if boardState['r1'][0] == boardState['r1'][1] and boardState['r1'][1] == boardState['r1'][2]:
			print(f"{boardState['r1'][0][1]} wins!")
			quit()
	#Check horizontal 2
	if boardState['r2'][0] == ' X ' or boardState['r2'][0] == ' O ':
		if boardState['r2'][0] == boardState['r2'][1] and boardState['r2'][1] == boardState['r2'][2]:
			print(f"{boardState['r2'][0][1]} wins!")
			quit()
	#Check horizontal 3
	if boardState['r3'][0] == ' X ' or boardState['r3'][0] == ' O ':
		if boardState['r3'][0] == boardState['r3'][1] and boardState['r3'][1] == boardState['r3'][2]:
			print(f"{boardState['r3'][0][1]} wins!")
			quit()
	#Check vertical 1
	if boardState['r1'][0] == ' X ' or boardState['r1'][0] == ' O ':
		if boardState['r1'][0] == boardState['r2'][0] and boardState['r2'][0] == boardState['r3'][0]:
			print(f"{boardState['r1'][0][1]} wins!")
			quit()
	#Check vertical 2
	if boardState['r1'][1] == ' X ' or boardState['r1'][1] == ' O ':
		if boardState['r1'][1] == boardState['r2'][1] and boardState['r2'][1] == boardState['r3'][1]:
			print(f"{boardState['r1'][1][1]} wins!")
			quit()
	#Check vertical 3
	if boardState['r1'][2] == ' X ' or boardState['r1'][2] == ' O ':
		if boardState['r1'][2] == boardState['r2'][2] and boardState['r2'][2] == boardState['r3'][2]:
			print(f"{boardState['r1'][2][1]} wins!")
			quit()
	#Check diagonal 1
	if boardState['r1'][0] == ' X ' or boardState['r1'][0] == ' O ':
		if boardState['r1'][0] == boardState['r2'][1] and boardState['r2'][1] == boardState['r3'][2]:
			print(f"{boardState['r1'][0][1]} wins!")
			quit()
	#Check diagonal 2
	if boardState['r3'][0] == ' X ' or boardState['r3'][0] == ' O ':
		if boardState['r3'][0] == boardState['r2'][1] and boardState['r2'][1] == boardState['r1'][2]:
			print(f"{boardState['r3'][0][1]} wins!")
			quit()
	


#name = input("Please enter your name: ")
#print(f"Hello, {name}. Let's play Tic-Tac-Toe.")
draw_TTT_board()
while len(remaining_moves) > 0:
	get_player_move()
	opponent_move()
