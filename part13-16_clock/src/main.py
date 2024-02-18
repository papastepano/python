# WRITE YOUR SOLUTION HERE:
import pygame
import datetime
import math

pygame.init()

# Constants for clock size and colors
CLOCK_RADIUS = 100  # Make the clock bigger
HOUR_HAND_LENGTH = CLOCK_RADIUS * 0.5
MIN_HAND_LENGTH = CLOCK_RADIUS * 0.7
SEC_HAND_LENGTH = CLOCK_RADIUS * 0.9
CENTER = (320, 240)  # Center of the screen
HAND_TAIL_LENGTH = 15  # Length of the tail of the hand

# Set up the display
display = pygame.display.set_mode((640, 480))
pygame.display.set_caption("System Clock")

def draw_hand(center, length, tail_length, angle, color, width=2):
    end_x = center[0] + length * math.cos(angle)
    end_y = center[1] - length * math.sin(angle)
    tail_x = center[0] - tail_length * math.cos(angle)
    tail_y = center[1] + tail_length * math.sin(angle)
    pygame.draw.line(display, color, (tail_x, tail_y), (end_x, end_y), width)

def draw_clock_face():
    for i in range(12):
        angle = -((i / 12) * 2 * math.pi - math.pi / 2)
        x = CENTER[0] + CLOCK_RADIUS * math.cos(angle)
        y = CENTER[1] - CLOCK_RADIUS * math.sin(angle)
        pygame.draw.circle(display, (255, 255, 255), (int(x), int(y)), 4 if i % 3 == 0 else 2)

def update_clock():
    display.fill((0, 0, 0))
    
    draw_clock_face()

    current_time = datetime.datetime.now()
    hours = current_time.hour % 12 + current_time.minute / 60
    minutes = current_time.minute
    seconds = current_time.second

    # Calculate hand angles
    hour_angle = -((hours / 12) * 2 * math.pi - math.pi / 2)
    min_angle = -((minutes / 60) * 2 * math.pi - math.pi / 2)
    sec_angle = -((seconds / 60) * 2 * math.pi - math.pi / 2)

    # Draw the hands with tails
    draw_hand(CENTER, HOUR_HAND_LENGTH, HAND_TAIL_LENGTH, hour_angle, (255, 255, 255), 6)
    draw_hand(CENTER, MIN_HAND_LENGTH, HAND_TAIL_LENGTH, min_angle, (255, 255, 255), 4)
    draw_hand(CENTER, SEC_HAND_LENGTH, HAND_TAIL_LENGTH, sec_angle, (255, 0, 0), 2)

    # Draw center circle
    pygame.draw.circle(display, (255, 255, 255), CENTER, 5)

    # Optionally, display the current time as text
    font = pygame.font.SysFont(None, 36)
    time_text = font.render(current_time.strftime('%H:%M:%S'), True, (0, 255, 0))
    display.blit(time_text, (10, 10))

    pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update_clock()
    pygame.time.delay(1000)  # Update the clock every second

pygame.quit()
