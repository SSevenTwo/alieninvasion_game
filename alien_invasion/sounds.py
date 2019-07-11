import pygame.mixer as pm

pm.init()

def play_boom():
    pm.stop()
    boom= pm.Sound("sounds/boom.wav")
    boom.set_volume(0.2)
    boom.play()
    
def play_explode():
    pm.stop()
    boom= pm.Sound("sounds/explode.wav")
    boom.set_volume(0.2)
    boom.play()
    
def play_shoot():
    pm.stop()
    boom= pm.Sound("sounds/shoot.wav")
    boom.set_volume(0.1)
    boom.play()
    
def play_levelup():
    pm.stop()
    boom= pm.Sound("sounds/levelup.wav")
    boom.set_volume(1)
    boom.play()
    

def play_music():
    pm.music.load('sounds/music.mp3')
    pm.music.set_volume(0.5)
    pm.music.play(0)

def stop_music():
    pm.music.stop()
