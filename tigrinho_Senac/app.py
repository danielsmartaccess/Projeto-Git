from abc import ABC, abstractmethod
import itertools
import random

@abstractmethod


class  CassaNiquel:
    def __init__(self, level=1):
        self.SIMBOLOS = {
            'money_mouth_face': '1F911',
            'money_bag': '1F4B0',
            'money_with_wings': '1F4B8',
            'dollar_banknote': '1F4B5',
            'coin': '1FA99'
        }
        self.level = level
        self.permutations = self._gen_permutations()

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






maquina1 = CassaNiquel()
maquina1._get_final_result()
