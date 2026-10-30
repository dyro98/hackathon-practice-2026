def greet(name: str = "Hackathon 2026") -> str:
    return f"Hello, {name}! Welcome to the hackathon practice repo."


def main() -> None:
    print(greet())
    print("This is a sample program created in this repository.")


if __name__ == "__main__":
    main()
