# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is for space aliens game

import ugame
import stage

import constants


def game_scene():
    # this function is the main game scene
    
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [ship] + [background]
    game.render_block()

        # repeat forever, or you turn it off
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            #if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
        #else:
           # ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)

        if keys & ugame.K_LEFT:
            #if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            #else:
                #ship.move(0, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
        
        # update game logic
        
        # redraw Sprites
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()
