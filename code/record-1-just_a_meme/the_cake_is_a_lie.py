"""
The cake is a lie

"The cake is a lie" is a meme from the game Portal.
This example shows to check type matching, how not to use the isinstance function, and how to break the
Liskov Substitution Principle.
Don't get this too seriously.
"""


class Lie:
    pass


class Reward:
    pass


class Cake(Reward, Lie):
    pass


if __name__ == "__main__":
    cake = Cake()
    classes_to_check_wrong_order = [Lie, Reward, Cake]

    for cl in classes_to_check_wrong_order:
        if isinstance(cake, cl):
            print(f"cake instance {cake} is a {cl.__name__}")
            break

    print(type(cake) == Lie)  # False
    print(type(cake) == Cake)  # True
