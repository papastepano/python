# Complete your game here
import pygame
import random

class Frog:
    MOVE_MONSTERS_EVENT = pygame.USEREVENT + 1

    def __init__(self):
        pygame.init()        

        self.load_images()
        self.new_game()
        
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.scale = self.images[1].get_height()
        self.running = True
        window_height = self.scale * self.height
        window_width = self.scale * self.width
        self.window = pygame.display.set_mode((window_width, window_height + self.scale))

        self.game_font = pygame.font.SysFont("Arial", 24)
        pygame.display.set_caption("Frog")

        self.clock = pygame.time.Clock()
        pygame.time.set_timer(self.MOVE_MONSTERS_EVENT, 1000)

        self.main_loop()

    def load_images(self):
        self.images = []
        for name in ["coin", "door", "monster", "robot"]:
            self.images.append(pygame.image.load(name + ".png"))

    def new_game(self):
        self.moves = 0
        self.coins = 0
        self.running = True

        self.map = [[9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9],
                    [9, 8, 8, 2, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 2, 8, 9],
                    [9, 8, 0, 8, 8, 8, 8, 8, 8, 8, 8, 0, 8, 8, 8, 8, 9],
                    [9, 8, 8, 8, 8, 0, 8, 8, 0, 8, 8, 8, 8, 8, 8, 8, 9],
                    [9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9],
                    [9, 8, 8, 8, 8, 8, 8, 8, 3, 8, 8, 8, 8, 8, 8, 8, 9],
                    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]

    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()

    
    def move(self, move_y, move_x):
        if self.game_solved():
            return
        
        if self.running == False:
            return

        self.moves += 1
        robot_old_y, robot_old_x = self.find_robot()
        robot_new_y = robot_old_y + move_y
        robot_new_x = robot_old_x + move_x

        # Did the robot hit a wall?
        if self.map[robot_new_y][robot_new_x] == 9:
            return

        # Encounter with a monster
        if self.map[robot_new_y][robot_new_x] == 2:
            self.running = False
            # return

        # collect a coin
        if self.map[robot_new_y][robot_new_x] == 0:
            self.map[robot_new_y][robot_new_x] = 8
            self.coins += 1

        self.map[robot_old_y][robot_old_x] += 5
        self.map[robot_new_y][robot_new_x] = abs(self.map[robot_new_y][robot_new_x] - 5)

    def move_monsters(self):
        if self.running == False:
            return
        if self.game_solved():
            return
        
        # Collect initial positions of monsters
        monster_positions = [(y, x) for y in range(self.height) for x in range(self.width) if self.map[y][x] == 2]

        # Move each monster
        for y, x in monster_positions:
            while True:
                dy, dx = self.get_random_monster_move()
                monster_new_y = y + dy
                monster_new_x = x + dx

                if self.is_valid_monster_move(monster_new_y, monster_new_x):
                    self.map[y][x] = 8
                    self.map[monster_new_y][monster_new_x] = 2
                    break

    def get_random_monster_move(self):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        dy, dx = random.choice(directions)
        return dy, dx

    def is_valid_monster_move(self, new_y, new_x):
        if self.map[new_y][new_x] in [8,3]:
            return True
        return False


    def find_robot(self ):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in [3, 4]:
                    return (y, x)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move(0, -1)
                if event.key == pygame.K_RIGHT:
                    self.move(0, 1)
                if event.key == pygame.K_UP:
                    self.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    self.move(1, 0)

                if event.key == pygame.K_F2:
                    self.new_game()
                if event.key == pygame.K_ESCAPE:
                    exit()

            if event.type == pygame.QUIT:
                exit()

            if event.type == self.MOVE_MONSTERS_EVENT:
                self.move_monsters()

    def draw_window(self):
        self.window.fill((255, 255, 255))

        game_text = self.game_font.render("Moves: " + str(self.moves), True, (255, 0, 0))
        self.window.blit(game_text, (25, self.height * self.scale + 10))

        game_text = self.game_font.render("Coins:"  + str(self.coins), True, (255, 0, 0))
        self.window.blit(game_text, (200, self.height * self.scale + 10))

        game_text = self.game_font.render("F2 = new game", True, (255, 0, 0))
        self.window.blit(game_text, (400, self.height * self.scale + 10))


        game_text = self.game_font.render("Esc = exit game", True, (255, 0, 0))
        self.window.blit(game_text, (600, self.height * self.scale + 10))

        for y in range(self.height):
            for x in range(self.width):
                square = self.map[y][x]
                cell_center_x = x * self.scale + self.scale // 2
                cell_center_y = y * self.scale + self.scale // 2
                
                if square == 8:  # If the tile is a floor
                    pygame.draw.rect(self.window, (255, 255, 255), (x * self.scale, y * self.scale, self.scale, self.scale))
                elif square == 9:  # If the tile is a wall
                    pygame.draw.rect(self.window, (0, 0, 0), (x * self.scale, y * self.scale, self.scale, self.scale))
                elif square == 4:  # If the robot exits
                    image = self.images[3]
                    image_width = image.get_width()
                    image_height = image.get_height()
                    image_top_left_x = cell_center_x - image_width // 2
                    image_top_left_y = cell_center_y - image_height // 2
                    self.window.blit(image, (image_top_left_x, image_top_left_y))
                else:
                    # For other tiles, use the respective image
                    image = self.images[square]
                    image_width = image.get_width()
                    image_height = image.get_height()
                    image_top_left_x = cell_center_x - image_width // 2
                    image_top_left_y = cell_center_y - image_height // 2
                    self.window.blit(image, (image_top_left_x, image_top_left_y))
        
        if self.game_solved():
            lines = [
                "Congratulations, you solved the game!",
                f"Total coins collected: {self.coins}",
                f"Total moves: {self.moves}",
                "Press F2 to play again"
            ]

            # Calculate the starting Y position to center the text block vertically
            total_height = len(lines) * (self.game_font.get_height() + 5)  # Add some spacing between lines
            start_y = self.scale * self.height // 2 - total_height // 2

            for i, line in enumerate(lines):
                game_text = self.game_font.render(line, True, (255, 0, 0))
                text_x = self.scale * self.width // 2 - game_text.get_width() // 2
                text_y = start_y + i * (self.game_font.get_height() + 5)  # Move down for each new line
                pygame.draw.rect(self.window, (0, 0, 0), (text_x, text_y, game_text.get_width(), game_text.get_height()))
                self.window.blit(game_text, (text_x, text_y))


        if self.running == False:
            game_text = self.game_font.render("GAME OVER!", True, (255, 0, 0))
            game_text_x = self.scale * self.width / 2 - game_text.get_width() / 2
            game_text_y = self.scale * self.height / 2 - game_text.get_height() / 2
            pygame.draw.rect(self.window, (0, 0, 0), (game_text_x, game_text_y, game_text.get_width(), game_text.get_height()))
            self.window.blit(game_text, (game_text_x, game_text_y))

        pygame.display.flip()

    def game_solved(self):
        y, x = self.find_robot()
        if self.map[y][x] == 4:
            return True
        return False



if __name__ == "__main__":
    Frog()
