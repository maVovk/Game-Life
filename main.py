from Game import Game


def main():
    game = Game(map_size=300, seed=1, possibility=0.2)

    game.start(delay=300)


if __name__ == '__main__':
    main()

