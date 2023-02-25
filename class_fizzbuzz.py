import typer
from typing import Tuple


class FizzBuzz:
    def __init__(self, fizzbuzz: str, numbers_to_divide: int, numbers_fizzbuzz: Tuple):
        self.fizzbuzz = fizzbuzz
        self.numbers_to_divide = numbers_to_divide
        self.numbers_fizzbuzz = numbers_fizzbuzz
        self.dividers = []
        self.dividend = []
        self.dict_values = {}

    def __str__(self) -> str:
        numbers_to_divide = typer.style(self.numbers_to_divide, fg=typer.colors.CYAN)
        return typer.style(
            f"\t{self.fizzbuzz.capitalize()} -> {numbers_to_divide} is divisible by : ", fg=typer.colors.MAGENTA
        )

    def __try_modulo(self, numbers_to_divide: int):
        for _ in self.numbers_fizzbuzz:
            if numbers_to_divide % _ == 0:
                self.__fill_lists(self.numbers_to_divide)

    def __fill_lists(self, numbers_to_divide: int):
        for _ in self.numbers_fizzbuzz:
            if numbers_to_divide % _ == 0 and _ not in self.dividers:
                self.dividers.append(_)
                self.dividend.append(numbers_to_divide)
                self.dict_values[numbers_to_divide] = self.dividers

    def progress_bar(self):
        with typer.progressbar(range(1, self.numbers_to_divide + 1), length=self.numbers_to_divide) as progress:
            for self.numbers_to_divide in progress:
                self.__display_fizzbuzz()
            print("\tDone !")
            self.__display_dictionary()

    def __display_fizzbuzz(self):
        self.__try_modulo(self.numbers_to_divide)
        if self.numbers_to_divide in self.dividend:
            typer.secho(f"{self.__str__()}{typer.style(self.dividers, fg=typer.colors.CYAN)}")
        self.dividers = []
        if self.numbers_to_divide not in self.dividend:
            typer.secho(f"\t{self.numbers_to_divide}", fg=typer.colors.WHITE)

    def __display_dictionary(self):
        list_values = []
        for cle, valeur in self.dict_values.items():
            list_values.append(cle)
            sorted(list_values)
            if cle in list_values:
                print(f" {cle} is divisible by : {valeur}")
