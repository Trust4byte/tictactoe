class TicTacToe:
    def __init__(self):
        self.spielfeld = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9"]

        # TicTacToe players, default x, o
        self.player1 = "x"
        self.player2 = "o"

        # Starts the game automatically
        self.game()

    def print_spielfeld(self):
        """Prints out the playing field"""

        print("")
        print(self.spielfeld[0] + " |", self.spielfeld[1] + " |", self.spielfeld[2])
        print(self.spielfeld[3] + " |", self.spielfeld[4] + " |", self.spielfeld[5])
        print(self.spielfeld[6] + " |", self.spielfeld[7] + " |", self.spielfeld[8])
        print("")

    def input_number(self):
        """Processes all numeric inputs"""
        while True:
            number = input("Type in field: ")
            try:
                number = int(number)

                if 1 <= number <= 9:
                    return number
                else:
                    print(str(number) + " is not in range 1 - 9")
            except:
                print("Sry, please use a number between 1 - 9")

    def welcome_message(self):
        print("\nWelcome to TicTacToe!")
        print("Made by: Trust4byte")
        print("Join us: dc.zonenetwork.de")
        print("\n--------------------------")


    def check_win(self):
        """Checks if somebody wins"""

        #Vertikal - Check
        if self.spielfeld[0] == self.spielfeld[1] == self.spielfeld[2]:
            return self.spielfeld[0]
        if self.spielfeld[3] == self.spielfeld[4] == self.spielfeld[5]:
            return self.spielfeld[3]
        if self.spielfeld[6] == self.spielfeld[7] == self.spielfeld[8]:
            return self.spielfeld[6]

        #Horizontal - Check
        if self.spielfeld[0] == self.spielfeld[3] == self.spielfeld[6]:
            return self.spielfeld[0]
        if self.spielfeld[1] == self.spielfeld[4] == self.spielfeld[7]:
            return self.spielfeld[1]
        if self.spielfeld[2] == self.spielfeld[5] == self.spielfeld[8]:
            return self.spielfeld[2]

        #Diagonal - Check
        if self.spielfeld[0] == self.spielfeld[4] == self.spielfeld[8]:
            return self.spielfeld[4]
        if self.spielfeld[6] == self.spielfeld[4] == self.spielfeld[2]:
            return self.spielfeld[4]

    def p_player1(self):
        """Checks if player1 is allowed to draw on a specific field"""

        print("You are playing as player: " + self.player1)
        while True:
            x = self.input_number()
            x -= 1

            if self.spielfeld[x] != self.player1 and self.spielfeld[x] != self.player2:

                self.spielfeld[x] = self.player1
                self.print_spielfeld()
                break

            else:
                print("There is already a: " + self.spielfeld[x])

    def p_player2(self):
        """Checks if player2 is allowed to draw on a specific field"""

        print("You are playing as player: " + self.player2)
        while True:
            o = self.input_number()
            o -= 1

            if self.spielfeld[o] != self.player1 and self.spielfeld[o] != self.player2:

                self.spielfeld[o] = self.player2
                self.print_spielfeld()
                break

            else:
                print("There is already a: " + self.spielfeld[o])

    def game(self):
        """Handles the game"""
        self.welcome_message()
        self.print_spielfeld()

        while self.check_win() != "None":
            self.p_player1()
            winner = self.check_win()
            if winner:
                print("Player " + winner + " win")
                break

            self.p_player2()
            winner = self.check_win()
            if winner:
                print("Player " + winner + " win")
                break

t = TicTacToe()