from Game import Game


def main():
    game = Game(map_size=400, seed=115, possibility=0.25)

    game.start(delay=300)


if __name__ == '__main__':
    main()

