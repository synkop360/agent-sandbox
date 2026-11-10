"""Petit script qui dit bonjour."""


def bonjour(name: str = "monde") -> str:
    """Retourne le message de salutation."""
    return f"Bonjour {name} !"


def main() -> None:
    print(bonjour())


if __name__ == "__main__":
    main()
