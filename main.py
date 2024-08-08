import random
class Die:

    def __init__(self, ):
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
        self.computer = computer
        self.player = player

    def play(self):
      print("==============================================")
      print("🎲🎲Welcome to Roll the Dice!")
      print("===================================")
      while True:
          self.play_round()
          #TODO: implement game over

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
        elif computer_value > player_value:
            print("The computer win this round. Try again!")
        else:
            print("It is a tie")

        print(f"Your counter: {self._player.counter}")
        print(f"Computer counter: {self._computer.counter}")