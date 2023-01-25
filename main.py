import os
from typing import Tuple

import typer

user = os.environ["USER"]
NUMBERS_FIZZ_BUZZ = [3, 5, 6, 7]

app = typer.Typer()
typer.secho(f"\t Hello {user} ! ", bg=typer.colors.WHITE, fg=typer.colors.RED)


@app.command("FizzBuzz")
def main(displayed_word: str = typer.Argument("fizzbuzz", help="String to display"),
         numbers_to_divide: int = typer.Argument(60, help="number to loop in."),
         numbers_fizzbuzz: Tuple[int, int, int] = typer.Argument((3, 5, 7), help="3 dividers.")):
    """
    Found dividers of a number with three arguments
    :param displayed_word: str
    :param numbers_to_divide: int
    :param numbers_fizzbuzz: Tuple
    :return: FizzBuzz()
    :version : python 3.10
    """
    fb = FizzBuzz(displayed_word, numbers_to_divide, numbers_fizzbuzz)
    fb.display_fizzbuzz()
    return fb


class FizzBuzz:
    def __init__(self, fizzbuzz: str, numbers_to_divide: int, numbers_fizzbuzz: Tuple):
        self.fizzbuzz = fizzbuzz
        self.numbers_to_divide = numbers_to_divide
        self.numbers_fizzbuzz = numbers_fizzbuzz
        self.dividers = []
        self.dividend = []

    def __str__(self) -> str:
        numbers_to_divide = typer.style(self.numbers_to_divide, fg=typer.colors.CYAN)
        return typer.style(
            f"\t{self.fizzbuzz.capitalize()} -> {numbers_to_divide} is divisible by : ", fg=typer.colors.MAGENTA
        )

    def _try_modulo(self, numbers_to_divide: int):
        for _ in self.numbers_fizzbuzz:
            if numbers_to_divide % _ == 0:
                self._fill_lists(self.numbers_to_divide)

    def _fill_lists(self, numbers_to_divide: int):
        for _ in self.numbers_fizzbuzz:
            if numbers_to_divide % _ == 0 and _ not in self.dividers:
                self.dividers.append(_)
                self.dividend.append(numbers_to_divide)

    def display_fizzbuzz(self):
        with typer.progressbar(range(1, self.numbers_to_divide + 1), length=self.numbers_to_divide) as progress:
            for self.numbers_to_divide in progress:
                self._try_modulo(self.numbers_to_divide)
                if self.numbers_to_divide in self.dividend:
                    typer.secho(f"{self.__str__()}{typer.style(self.dividers, fg=typer.colors.CYAN)}")
                self.dividers = []
                if self.numbers_to_divide not in self.dividend:
                    typer.secho(f"\t{self.numbers_to_divide}", fg=typer.colors.WHITE)
            print("\tDone !", end="")


if __name__ == '__main__':
    app()
