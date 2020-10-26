#TIC-TAC-TOE Console Game

"""
author = "Alvin Saini"
Gmail = "Codewithalvin@gmail.com"
"""

# import
"""
only random to get random number
 for bot's choice
"""
from random import choice

class Game:
	"""
	Constructor to initalise objects
	here the methods are initalized
	in thier order
	so they work in systematic way
	
	"""
	def __init__(self):
		self.winner=None
		self.continueGame=True		
		self.CreateDict()
		self.board()
		self.StartGame()
		self.printWinner()			

	"""Creating board of game
	  this board is shown om screen"""	
	def board(self):
		print(f"""{self.value[1]}|{self.value[2]}|{self.value[3]}		1|2|3\n-+-+-		-+-+-\n{self.value[4]}|{self.value[5]}|{self.value[6]}		4|5|6\n-+-+-		-+-+-\n{self.value[7]}|{self.value[8]}|{self.value[9]}		7|8|9""")
				
	"""create dictonary this provide value to board to update
	   board get value from this using f string see "board"
	   to clear doubts
	"""
	def CreateDict(self):
		self.value={0:"-",
					1:"-",
					2:"-",
					3:"-",
					4:"-",
					5:"-",
					6:"-",
					7:"-",
					8:"-",
					9:"-"
					}
		self.choiceList=[1,2,3,4,5,6,7,8,9]
	
	"""this method update Dictonary "self.value"
	therefore resulting in update the board
	"""
	def UpdateDict(self,i,v):
		if i==None or v==None:
			None
		else:
			self.value[i]=v
	"""
	This method is to genrate computer choice with user
	"""
	def Bot(self):
		if len(self.choiceList)==0:
			return None
		myChoice=choice(self.choiceList)	
		self.choiceList.remove(myChoice)
		self.UpdateDict(myChoice,"0")
	
	"""
	this method take user input &&
	also catches errors that user can make
	like(entering a non int,entering a value that already exists in board)
	"""	
	def User(self):					
		while True:
			if len(self.choiceList)==0:
				break
			userInput=input("\nenter the number\n")
			try:
				userInput=int(userInput)
				if userInput not in self.choiceList:
					print("please enter a number that is not choisen before")
				else:
					self.UpdateDict(userInput,"X")
					self.choiceList.remove(userInput)
					break
			except:
				print("\nenter a valid number\n")

	"""
	checks if any one win diagonally or linely
	by call method
	"""
	def checkWinner(self):
		self.check([1,4,7],1)
		self.check([1,2,3],3)
		self.check([1],4)
		self.check([3],2)
			
	
	"""
	method to check if anyone win
	"""
	def check(self,listI,increment):
		"""
		123 >> increment of 1
		456 √√ increment of 3
		789 \\ increment of 4
		    // increment of 2
		"""
		for i in listI:
			if self.value[i]==self.value[i+increment]==self.value[i+(2*increment)] and self.value[i]!="-":
				self.continueGame=False
				self.winner=self.value[i]
				break
			else:
				None
	
	"""
	here most methods are integrated and 
	leading the game toward final result
	"""
	def StartGame(self):
		for i in range(5):
			print("\nbot chance\n")
			self.Bot()
			self.board()
			self.checkWinner()
			if self.continueGame==False:
				break	
			print("\nuser chance\n")
			self.User()
			self.board()
			self.checkWinner()
			if self.continueGame==False:
				break
	
	"""
	print the winner in last
	after ending of loop
	"""			
	def printWinner(self):
		if self.winner=="X":
			print("\n\nCongratulations You Won!!")
		elif self.winner=="0":
			print("\n\nBot win Try Harder Next Time")
		else:
			print("\n\nMatch Tie")	


#making object
tic=Game()



