from Logic import Logic
from rectangel_creator import RectangleCreator
from view import View


def main():
    size = 9

    ls = RectangleCreator.get_rectangles(size)
    total_square = Logic.calculate_total_square(ls)
    total_perimetr = Logic.calculate_total_perimetr(ls)

    msg = (f"Total square = {total_square}\n" \
           f"total perimetr = {total_perimetr}")
    print(View.convert(ls))
    print(msg)


if __name__ == "__main__":
    main()