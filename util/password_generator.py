import random
import string
import re


class TextGenerator:
    @staticmethod
    def generate_text_for_matching_pattern(pattern: str):
        pass

    @staticmethod
    def generate_text_with_length(length: int):
        letters = list(string.ascii_letters)
        return "".join(random.choices(letters, k=length))


class PasswordGenerator:
    letters = list(string.ascii_letters) # or list(map(chr, range(97, 123)))
    numbers = list({str(num) for num in range(0, 10)})
    symbols = list("!#$%&()*+")

    @staticmethod
    def generate_password() -> str:
        nr_letters = random.randint(8, 10)
        nr_numbers = random.randint(2, 4)
        nr_symbols = random.randint(2, 4)

        # password_list = []
        # password_list.extend(random.choices(population=PasswordGenerator.letters, k=nr_letters))
        # password_list.extend(random.choices(population=PasswordGenerator.numbers, k=nr_numbers))
        # password_list.extend(random.choices(population=PasswordGenerator.symbols, k=nr_symbols))

        # or

        # you can also use .extend instead of +
        password_list = [random.choice(PasswordGenerator.letters) for _ in range(0, nr_letters)] + \
                        [random.choice(PasswordGenerator.numbers) for _ in range(0, nr_numbers)] + \
                        [random.choice(PasswordGenerator.symbols) for _ in range(0, nr_symbols)]

        random.shuffle(password_list)

        return "".join(password_list)
