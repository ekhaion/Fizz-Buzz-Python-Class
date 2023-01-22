from math import ceil
import typer

app = typer.Typer()


@app.command("FizzBuzz")
def main(displayed_word: str = "fizzbuzz", numbers_to_divide: int = 15):
    fb = FizzBuzz(displayed_word, numbers_to_divide)
    fb.loop_on_numbers_to_divide()
    return fb


def _is_modulo_5_equal_0(_: int) -> bool:
    return _ % 5 == 0


def _is_modulo_3_equal_0(_: int) -> bool:
    return _ % 3 == 0


class FizzBuzz:
    def __init__(self, fizzbuzz: str, numbers_to_divide: int):
        self.fizzbuzz = fizzbuzz
        self.numbers_to_divide = numbers_to_divide

    def __str__(self) -> str:
        cut_in_half = ceil(len(self.fizzbuzz) / 2)
        return f" {self.fizzbuzz[:cut_in_half]} {self.fizzbuzz[cut_in_half:]}".title()

    def _display_word(self, _: int):
        fizz_or_buzz = self.__str__().split(" ", 2)
        if _is_modulo_3_equal_0(_) and _is_modulo_5_equal_0(_):
            typer.secho(self.__str__(), fg=typer.colors.MAGENTA)
        elif _is_modulo_3_equal_0(_):
            typer.secho(f" {fizz_or_buzz[1]}", fg=typer.colors.RED)
        elif _is_modulo_5_equal_0(_):
            typer.secho(f" {fizz_or_buzz[2]}", fg=typer.colors.BLUE)
        else:
            typer.secho(f" {_}", fg=typer.colors.WHITE)

    def loop_on_numbers_to_divide(self) -> bool:
        with typer.progressbar(range(1, self.numbers_to_divide + 1)) as progress:
            for _ in progress:
                self._display_word(_)
            return True


if __name__ == '__main__':
    app()

# command line -> python3.10 [file_name.py] [str(fizzbuzz)] [int(iterations)]
