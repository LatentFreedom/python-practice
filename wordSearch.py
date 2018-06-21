# You are given a board (2 dimensional array) of characters and a word (string)
# Determine if the word can be found in the board.
# You can only move left, right, up, or down by one character.

class Search:

	def __init__(self,board,word):
		self.have_been = []
		self.current_index = None
		self.num_rows = 0
		self.num_cols = 0
		self.board = board
		self.word = word

	def set_row_col_len(self):
		# Set row count
		self.num_rows = len(self.board)
		if self.num_rows == 0:
			return False
			# Set column count
		self.num_cols = len(self.board[0])
		return False if self.num_cols == 0 else True

	def find_first_letter(self):
		# Loop through rows
		for row in range(self.num_rows):
			# Loop through columns
			for col in range(self.num_cols):
				# Determine if column has needed char
				if self.board[row][col] == self.word[0]:
					self.current_index = [row,col]
					self.have_been.append(self.current_index)
					return True

	def find_char_path(self):
		for i in range(1,len(self.word)):
			# Check left and right character
			if self.check_left_char(i):
				continue
			elif self.check_right_char(i):
				continue
			elif self.check_up_char(i):
				continue
			elif self.check_down_char(i):
				continue
			else:
				# Character not found given possible moves
				return False
		# We looped through and found each character in the board
		return True

	def check_left_char(self,word_index):
		left_col = self.current_index[1] - 1
		if left_col < 0:
			return False

		if self.board[self.current_index[0]][left_col] == self.word[word_index]:
			current_index = [self.current_index[0],left_col]
			if current_index in self.have_been:
				return False
			self.current_index = current_index
			self.have_been.append(current_index)
			return True
		else:
			return False

	def check_right_char(self,word_index):
		right_col = self.current_index[1] + 1
		if right_col >= self.num_cols:
			return False

		if self.board[self.current_index[0]][right_col] == self.word[word_index]:
			current_index = [self.current_index[0],right_col]
			if current_index in self.have_been:
				return False
			self.current_index = current_index
			self.have_been.append(current_index)
			return True
		else:
			return False

	def check_up_char(self,word_index):
		# Check left column
		up_row = self.current_index[0] - 1
		if up_row < 0:
			return False

		if self.board[up_row][self.current_index[1]] == self.word[word_index]:
			current_index = [up_row,self.current_index[1]]
			if current_index in self.have_been:
				return False
			self.current_index = current_index
			self.have_been.append(current_index)
			return True
		else:
			return False

	def check_down_char(self,word_index):
		# Check left column
		down_row = self.current_index[0] + 1
		if down_row < 0:
			return False

		if self.board[down_row][self.current_index[1]] == self.word[word_index]:
			current_index = [down_row,self.current_index[1]]
			if current_index in self.have_been:
				return False
			self.current_index = current_index
			self.have_been.append(current_index)
			return True
		else:
			return False


def find_word(board,word):
	# Create new search object
	search_obj = Search(board,word)
	# Prep search object
	if not search_obj.set_row_col_len():
		return False

	# Find the first character of the word
	if not search_obj.find_first_letter():
		return False

	# Search for the next letters
	if not search_obj.find_char_path():
		return False

	# We found the word in the board
	return True


if __name__ == '__main__':
	board = [
	['A','B','C','D'],
	['N','D','S','E'],
	['A','B','G','E']
	]
	word = 'AND'

	if find_word(board,word):
		print("True")
	else:
		print("False")
