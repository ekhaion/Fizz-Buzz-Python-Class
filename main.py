import os
import typer
from class_fizzbuzz import FizzBuzz
from typing import Tuple

user = os.environ["USER"]

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
    fb.progress_bar()
    return fb


if __name__ == '__main__':
    app()
