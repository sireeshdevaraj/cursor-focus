import pygame
import ctypes
import pyautogui

pyautogui.screenshot('foo.png')
pygame.init()
flags = pygame.NOFRAME | pygame.FULLSCREEN
screen = pygame.display.set_mode(flags= flags)
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
clock = pygame.time.Clock()
running = True
bg = pygame.image.load("foo.png")
overlay_flags = pygame.FULLSCREEN | pygame.SRCALPHA
dt = 0.5
INTIAL_RADIUS = 500
prev = INTIAL_RADIUS

def zoom_in(bg,w,h):
    # Here you need to scale and crop it.
    original_w, original_h = bg.get_size()

    new_c_x = original_w // 2
    new_c_y = original_h // 2

    crop_x = new_c_x - (w // 2)
    crop_y = new_c_y - (h // 2)

    
    cropped_image = bg.subsurface((crop_x, crop_y, w, h))

    return cropped_image,


def focus(overlay,r):
    pygame.draw.circle(overlay, (0,0,0,0), pygame.mouse.get_pos(), r)
    screen.blit(overlay,(0,0))


while running:
    screen.blit(bg,(0,0))
    overlay = pygame.Surface((WIDTH,HEIGHT),flags = overlay_flags)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            # [ToDo]
            # Idea was to scale and crop the image.
            w = bg.get_size()[0]
            h = bg.get_size()[1]
            #INTIAL_RADIUS-=20
            #bg = pygame.transform.scale_by(bg,factor=1.5)
            #x,y = pygame.mouse.get_pos()
            #n_w = bg.get_size()[0]
            #n_h = bg.get_size()[1]
            #bg = zoom_in(bg, w = w, h = h)
            #pygame.mouse.set_pos((n_w - x*1.5, n_h - y*1.5))
        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                INTIAL_RADIUS += 40
            else:
                INTIAL_RADIUS -= 40

    dr = (INTIAL_RADIUS - prev)*dt
    prev += dr
    overlay.fill((0, 0, 0, 200)) 
    focus(overlay=overlay,r = prev)
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()