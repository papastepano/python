# Complete your game here
import pygame

class Frog:
    def __init__(self):
        pygame.init()
        
        self.load_images()
        self.new_game()
        
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.scale = self.images[1].get_height()

        window_height = self.scale * self.height
        window_width = self.scale * self.width
        self.window = pygame.display.set_mode((window_width, window_height + self.scale))

        self.game_font = pygame.font.SysFont("Arial", 24)
        pygame.display.set_caption("Frog")

        self.main_loop()

    def load_images(self):
        self.images = []
        for name in ["coin", "door", "monster", "robot"]:
            self.images.append(pygame.image.load(name + ".png"))

    def new_game(self):
        self.moves = 0
        self.coins = 0

        self.map = [[9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9],
                    [9, 8, 8, 2, 8, 8, 8, 8, 8, 8, 8, 8, 2, 8, 8, 8, 9],
                    [9, 8, 0, 8, 8, 8, 2, 8, 8, 2, 8, 0, 8, 8, 8, 8, 9],
                    [9, 8, 8, 2, 8, 0, 8, 8, 0, 8, 8, 8, 2, 8, 8, 8, 9],
                    [9, 8, 8, 8, 8, 8, 2, 8, 8, 2, 8, 8, 8, 8, 8, 8, 9],
                    [9, 8, 8, 8, 8, 8, 8, 8, 3, 8, 8, 8, 8, 8, 8, 8, 9],
                    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]

    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()

    
    def move(self, move_y, move_x):
        if self.game_solved():
            return

        self.moves += 1
        robot_old_y, robot_old_x = self.find_robot() 
        # print(robot_old_y, robot_old_x, self.map[robot_old_y][robot_old_x])
        robot_new_y = robot_old_y + move_y
        robot_new_x = robot_old_x + move_x
        # print(robot_new_y, robot_new_x, self.map[robot_new_y][robot_new_x])

        # Did the robot hit a wall?
        if self.map[robot_new_y][robot_new_x] == 9:
            return

        # collect a coin
        if self.map[robot_new_y][robot_new_x] == 0:
            self.map[robot_new_y][robot_new_x] = 8
            self.coins += 1

        self.map[robot_old_y][robot_old_x] += 5
        self.map[robot_new_y][robot_new_x] = abs(self.map[robot_new_y][robot_new_x] - 5)
        print('latest', self.map[robot_new_y][robot_new_x])

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
                print("Quitting")
                exit()

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
                elif square == 4:  # If the tile is a wall
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
            game_text = self.game_font.render("Congratulations, you solved the game!", True, (255, 0, 0))
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
