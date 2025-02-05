from abc import ABC, abstractmethod
import itertools
import random
from time import sleep
import os

@abstractmethod

class Player:
    def __init__(self, balance = 0):
        self.balance = balance
 
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def _display(self):
        pass

    @abstractmethod
    def _update_balance(self):
        pass
class  CassaNiquel:
    def __init__(self, level=1, balance = 0):
        self.SIMBOLOS = {
            'money_mouth_face': '1F911',
            'money_bag': '1F4B0',
            'money_with_wings': '1F4B8',
            'dollar_banknote': '1F4B5',
            'coin': '1FA99'
        }
        self.level = level
        self.permutations = self._gen_permutations()
        self.balance = balance
        self.initial_balance = self.balance

    def _gen_permutations(self):
        permutations = list(itertools.product(self.SIMBOLOS.keys(), repeat=3))
        for j in range(self.level):
            for i in self.SIMBOLOS.keys():
                permutations.append((i, i, i))
        return permutations
    
    def _get_final_result(self):
        if  not hasattr(self, 'permutations'):
            self.permutations = self._gen_permutations()

        result = list(random.choice(self.permutations))

        if len(set(result)) == 3 and random.randint(0,5) >= 2:
            result[1] = result[0]

        return result
    
    def _display(self, amount_bet, result, time=0.3):
        seconds = 2
        for i in range(0,int(seconds/time)):
            print(self._emojize(random.choice(self.permutations)))
            sleep(time)
            os.system('cls')
        print(self._emojize(result))

        if self._check_result_user(result):
            print(f'Parabéns, você ganhou {amount_bet*3}')
        else:
            print(f'Que pena, tente novamente!')


    def _emojize(self, emojis):
            return ''.join(tuple(chr(int(self.SIMBOLOS[code], 16)) for code in emojis))

    def _check_result_user(self, result):
        x = [result[0] == x for x in result]
        return True if all(x) else False
    
    def _update_balance(self, amount_bet, result, player: Player):
        if self._check_result_user(result):
            self.balance -= (amount_bet*3)
            player.balance += (amount_bet*3)
        else:
            self.balance += amount_bet
            player.balance -= amount_bet
        return self.balance
            
    def play(self, amount_bet, player: Player):
        result = self._get_final_result()
        self._display(amount_bet, result)
        self._update_balance(amount_bet, result, player)




maquina1 = CassaNiquel(level=1)
player1 = Player()
maquina1.play(10, player1)
print(player1.balance)