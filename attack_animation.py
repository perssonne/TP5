import arcade
from enum import Enum

class AttackType(Enum):
    def __init__(self):

        """
        Simple énumération pour représenter les différents types d'attaques.
        """
        ROCK = 0,
        PAPER = 1,
        SCISSORS = 2
        self.rock = AttackAnimation(AttackType.ROCK)
        self.paper = AttackAnimation(AttackType.PAPER)
        self.scissors = AttackAnimation(AttackType.SCISSORS)


class AttackAnimation(arcade.Sprite):
   ATTACK_SCALE = 0.50
   ANIMATION_SPEED = 5.0