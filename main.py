"""Entry point for service."""

from utils import optimize


def main():
    result = optimize(20)
    print(f"Project: {result}")


if __name__ == "__main__":
    main()
