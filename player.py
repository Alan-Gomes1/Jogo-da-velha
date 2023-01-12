import math
import random

class Player:
  def __init__(self, letter): # letter é X ou O
    self.letter = letter
    
  def get_move(self, game):
    pass
  
  
class RandomComputerPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)
    
  def get_move(self, game):
    square = random.choice(game.available_moves())
    return square
  

class HumanPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)
    
  def get_move(self, game):
    valid_square = False
    val = None
    while not valid_square:
      # Verifica se o valor inserido é válido ou se o campo no tabuleira está disponível, senão retorna inválido
      square = input(self.letter + ' Insira um movimento de (0-8):')
      try:
        val = int(square)
        if val not in game.available_moves():
          raise ValueError
        valid_square = True
      except ValueError:
        print('Campo invalido. Tente novamente')
        
    return val