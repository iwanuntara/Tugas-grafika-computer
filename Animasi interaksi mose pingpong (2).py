import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Sederhana")

# Warna
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Posisi dan ukuran objek
blade1_pos = [50, HEIGHT // 2 - 50]
blade2_pos = [WIDTH - 60, HEIGHT // 2 - 50]
blade_size = [10, 100]

ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_radius = 10
ball_speed = [4, 4]  # Kecepatan bola (x, y)

# Kecepatan blade
blade_speed = 5

# Loop utama
clock = pygame.time.Clock()

while True:
    screen.fill(BLUE)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Gerakkan blade 1 (kiri) dengan mouse
    mouse_y = pygame.mouse.get_pos()[1]
    blade1_pos[1] = mouse_y - blade_size[1] // 2

    # Gerakkan blade 2 (kanan) otomatis mengikuti bola
    if ball_pos[1] > blade2_pos[1] + blade_size[1] // 2:
        blade2_pos[1] += blade_speed
    elif ball_pos[1] < blade2_pos[1] + blade_size[1] // 2:
        blade2_pos[1] -= blade_speed

    # Batasi gerakan blade agar tidak keluar layar
    blade1_pos[1] = max(0, min(HEIGHT - blade_size[1], blade1_pos[1]))
    blade2_pos[1] = max(0, min(HEIGHT - blade_size[1], blade2_pos[1]))

    # Pergerakan bola
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Pantulan bola di atas dan bawah layar
    if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Pantulan bola di blade 1
    if (
        ball_pos[0] - ball_radius <= blade1_pos[0] + blade_size[0]
        and blade1_pos[1] < ball_pos[1] < blade1_pos[1] + blade_size[1]
    ):
        ball_speed[0] = -ball_speed[0]

    # Pantulan bola di blade 2
    if (
        ball_pos[0] + ball_radius >= blade2_pos[0]
        and blade2_pos[1] < ball_pos[1] < blade2_pos[1] + blade_size[1]
    ):
        ball_speed[0] = -ball_speed[0]

    # Reset bola jika keluar layar
    if ball_pos[0] - ball_radius <= 0 or ball_pos[0] + ball_radius >= WIDTH:
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [4, 4]

    # Gambar net
    pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)

    # Gambar blade dan bola
    pygame.draw.rect(screen, RED, (*blade1_pos, *blade_size))
    pygame.draw.rect(screen, YELLOW, (*blade2_pos, *blade_size))
    pygame.draw.circle(screen, WHITE, ball_pos, ball_radius)

    # Perbarui layar
    pygame.display.flip()
    clock.tick(60)
