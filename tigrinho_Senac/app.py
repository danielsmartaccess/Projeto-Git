from abc import ABC, abstractmethod
import itertools
import random
from time import sleep
import os
from typing import List, Tuple, Dict
from matplotlib import pyplot as plt

class BaseMachine(ABC):
    """Abstract base class for slot machine implementations."""
    
    @abstractmethod
    def _get_final_result(self) -> List[str]:
        """Get the final result of a spin."""
        pass

    @abstractmethod
    def _display(self, amount_bet: float, result: List[str], time: float = 0.3) -> None:
        """Display the spinning animation and result."""
        pass

    @abstractmethod
    def _emojize(self, emojis: List[str]) -> str:
        """Convert emoji codes to actual emojis."""
        pass

    @abstractmethod
    def _check_result_user(self, result: List[str]) -> bool:
        """Check if the result is a winning combination."""
        pass

    @abstractmethod
    def _update_balance(self, amount_bet: float, result: List[str], player: 'Player') -> float:
        """Update machine and player balance based on the result."""
        pass

    @abstractmethod
    def play(self, amount_bet: float, player: 'Player') -> None:
        """Execute a play on the machine."""
        pass


class Player:
    """Represents a player with a balance."""
    
    def __init__(self, balance: float = 0):
        self.balance = balance


class CassaNiquel(BaseMachine):
    """Implementation of a slot machine."""

    def __init__(self, level: int = 1, balance: float = 0):
        self.SIMBOLOS: Dict[str, str] = {
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

    def _gen_permutations(self) -> List[Tuple[str, ...]]:
        permutations = list(itertools.product(self.SIMBOLOS.keys(), repeat=3))
        for _ in range(self.level):
            for symbol in self.SIMBOLOS.keys():
                permutations.append((symbol, symbol, symbol))
        return permutations

    def _get_final_result(self) -> List[str]:
        if not hasattr(self, 'permutations'):
            self.permutations = self._gen_permutations()

        result = list(random.choice(self.permutations))

        if len(set(result)) == 3 and random.randint(0, 5) >= 2:
            result[1] = result[0]

        return result

    def _display(self, amount_bet: float, result: List[str], time: float = 0.3) -> None:
        seconds = 2
        clear_command = 'cls' if os.name == 'nt' else 'clear'
        
        for _ in range(0, int(seconds / time)):
            # print(self._emojize(random.choice(self.permutations)))
            sleep(time)
            os.system(clear_command)
        # print(self._emojize(result))

        # if self._check_result_user(result):
        #     print(f'Parabéns, você ganhou R${amount_bet * 3:.2f}')
        # else:
        #     print('Que pena, tente novamente!')

    def _emojize(self, emojis: List[str]) -> str:
        return ''.join(tuple(chr(int(self.SIMBOLOS[code], 16)) for code in emojis))

    def _check_result_user(self, result: List[str]) -> bool:
        return all(result[0] == x for x in result)

    def _update_balance(self, amount_bet: float, result: List[str], player: Player) -> float:
        if self._check_result_user(result):
            self.balance -= (amount_bet * 3)
            player.balance += (amount_bet * 3)
        else:
            self.balance += amount_bet
            player.balance -= amount_bet
        return self.balance

    def play(self, amount_bet: float, player: Player) -> None:
        if amount_bet <= 0:
            raise ValueError("A aposta deve ser maior que zero")
        if amount_bet > player.balance:
            raise ValueError("Saldo insuficiente para realizar a aposta")
            
        result = self._get_final_result()
        self._display(amount_bet, result)
        self._update_balance(amount_bet, result, player)

    @property
    def gain(self) -> float:
        """Calculate total gain since initialization."""
        return self.initial_balance - self.balance


def plot_results(days: int, balances: List[float]) -> None:
    """Plot the results of multiple days of operation."""
    plt.figure(figsize=(10, 6))
    x = list(range(1, days + 1))
    plt.plot(x, balances, marker='o')
    plt.title('Saldo da Máquina ao Longo dos Dias')
    plt.xlabel('Dias')
    plt.ylabel('Saldo (R$)')
    plt.grid(True)
    
    # Força o matplotlib a exibir o gráfico
    plt.show()

if __name__ == "__main__":
    maquina1 = CassaNiquel(level=1)

    JOGADORES_POR_DIA = 100
    APOSTAS_POR_DIA = 100
    DIAS = 10
    VALOR_MAXIMO = 200
    SALDO_INICIAL_JOGADOR = 1000  # Added constant for initial player balance

    saldo = []
    players = [Player(balance=SALDO_INICIAL_JOGADOR) for _ in range(JOGADORES_POR_DIA)]  # Initialize with balance

    # try:
    for i in range(DIAS):
        for player in players:
            for _ in range(random.randint(1, APOSTAS_POR_DIA)):
                if player.balance >= 5:  # Only play if player has minimum bet amount
                    maquina1.play(min(random.randint(5, VALOR_MAXIMO), player.balance), player)
        saldo.append(maquina1.gain)

    print(f'Saldo final da máquina: R${maquina1.balance:.2f}')
    plot_results(DIAS, saldo)
    plt.show()
        
    # except Exception as e:
    #     print(f"Erro durante a execução: {str(e)}")
