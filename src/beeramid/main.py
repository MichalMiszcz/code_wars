

def beeramid(bonus_value: int, price_of_beer: int) -> int:
    levels_of_pyramid = 1
    beer_number = 1
    cost = price_of_beer

    while True:
        if cost > bonus_value:
            levels_of_pyramid -= 1
            break

        levels_of_pyramid += 1
        new_beer_number = levels_of_pyramid ** 2 + beer_number
        cost = new_beer_number * price_of_beer

        beer_number = new_beer_number

    return levels_of_pyramid



if __name__ == '__main__':
    print(beeramid(1500, 2))
    print(beeramid(5000, 3))
    print(beeramid(3, 4))
    print(beeramid(0, 4))
    print(beeramid(-1, 4))
