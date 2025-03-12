import pygame
import neat
import os
import pickle  # For loading the best genome
from pong_game import Game


class PongGame:
    def __init__(self, window, width, height):
        self.game = Game(window, width, height)
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle
        self.ball = self.game.ball

    def test_ai(self, best_genome, config):
        net = neat.nn.FeedForwardNetwork.create(best_genome, config)

        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.game.move_paddle(left=True, up=True)
            if keys[pygame.K_s]:
                self.game.move_paddle(left=True, up=False)

            output = net.activate((self.right_paddle.y, self.ball.y, abs(self.right_paddle.x - self.ball.x)))
            decision = output.index(max(output))

            if decision == 0:
                pass
            elif decision == 1:
                self.game.move_paddle(left=False, up=True)
            else:
                self.game.move_paddle(left=False, up=False)

            self.game.loop()
            self.game.draw()
            pygame.display.update()

        pygame.quit()


def load_best_genome(file_path):
    try:
        with open(file_path, "rb") as f:
            best_genome = pickle.load(f)
            print("Best genome loaded successfully from 'best_genome.pickle'.")
            return best_genome
    except FileNotFoundError:
        print(f"No file found at '{file_path}'. Make sure to save the best genome first.")
        return None
    except Exception as e:
        print(f"Error loading the best genome: {e}")
        return None


def run_neat(config):
    # Load the best genome from the pickle file
    best_genome_file = 'best_genome.pickle'
    best_genome = load_best_genome(best_genome_file)

    if best_genome is None:
        print("Best genome not found. Exiting...")
        return

    # Initialize the game window
    width, height = 700, 500
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("AI vs Human Pong")

    # Create a PongGame instance and let the best genome play
    game = PongGame(window, width, height)
    game.test_ai(best_genome, config)


# Load NEAT configuration
local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'config.txt')

config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet,
                     neat.DefaultStagnation, config_path)
run_neat(config)
