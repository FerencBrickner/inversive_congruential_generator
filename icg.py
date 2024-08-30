from typing import Generator


def inversive_congruential_generator(
    *, seed: int = 1, multiplier: int = 2, increment: int = 3, modulus: int = 5
) -> Generator[int, None, None]:
    """
    Generates a sequence of numbers using an Inversive Congruential Generator (ICG).
    "https://en.wikipedia.org/wiki/Inversive_congruential_generator"
    """

    def modular_multiplicative_inverse(num):
        return next(x for x in range(1, modulus) if (num * x) % modulus == 1)

    while True:
        yield seed
        if seed == 0:
            seed = increment
            continue
        seed = modular_multiplicative_inverse(seed)
        seed *= multiplier
        seed += increment
        seed %= modulus


def main(*args, **kwargs) -> None:
    # sample usage with default arguments
    g = inversive_congruential_generator()
    for _ in range(10):
        print(next(g))


if __name__ == "__main__":
    main()
