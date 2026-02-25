"""主程序入口"""

from utils import add, subtract


def main():
    print(f"1 + 2 = {add(1, 2)}")
    print(f"5 - 3 = {subtract(5, 3)}")


if __name__ == "__main__":
    main()
