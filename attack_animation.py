import arcade
from enum import Enum

class AttackType(Enum):
    def __init__(self):

        """
        Simple énumération pour représenter les différents types d'attaques.
        """

        self.rock = AttackAnimation(AttackType.ROCK)
        self.paper = AttackAnimation(AttackType.PAPER)
        self.scissors = AttackAnimation(AttackType.SCISSORS)

class AttackAnimation(arcade.Sprite):
   ATTACK_SCALE = 0.50
   ANIMATION_SPEED = 5.0

   def __init__(self):
       self.ROCK = ("(assets/srock.png)")
       self.PAPER = ("(assets/spaper.png)")
       self.SCISSORS = ("(assets/scissors.png)")

   def on_update(self, delta_time: float = 1 / 60):

       # Update the animation.
       self.current_texture += 1
       if self.current_texture < len(self.textures):
           self.set_texture(self.current_texture)
       else:
           self.current_texture = 0
           self.set_texture(self.current_texture)