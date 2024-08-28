import random

class Die:

    def __init__(self,):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value

class Player:
    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        return self._die.roll()

class DiceGame:
    def __init__(self, player, computer):
        self._computer = computer
        self._player = player

    def play(self):
      print("==============================================")
      print("🎲🎲Welcome to Roll the Dice!")
      print("===================================")
      while True:
          self.play_round()
          #TO DO: implement game over

    def play_round(self):
        #welcome the user
        print("---------New Round-----------")
        input(" 🎲🎲Press any key to roll the dice.🎲🎲")

        #roll the dice

        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        #show the values

        print(f"Your die: {player_value}")
        print(f"computer die:{computer_value}")

        #Determine winner and loser

        if player_value > computer_value:
            print("You won the round!")
            self._player.decrement_counter()  #winner
            self._computer.increment_counter()  #loser
        elif computer_value > player_value:
            print("The computer win this round. Try again!")
            self._computer.decrement_counter()  # winner
            self._player.increment_counter()  # loser
        else:
            print("It is a tie")

        #Show counters
        print(f"Your counter: {self._player.counter}")
        print(f"Computer counter: {self._computer.counter}")


#Create instances
player_die = Die()
computer_die = Die()


my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

game = DiceGame(my_player, computer_player)

#Start the game
game.play()