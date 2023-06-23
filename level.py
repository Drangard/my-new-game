
import pygame
from tiles import Tile
from tiles import Coin
from settings import tile_size, screen_width
from player import Player

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.coin_counter = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                if cell == 'C':
                    coin = Coin((x, y), tile_size)
                    self.coins.add(coin)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 4
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -4
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 4

    def horizontal_movement_colision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_colision(self):
        player = self.player.sprite
        player.apply_gravity()

        collided_coins = pygame.sprite.spritecollide(player, self.coins, True)
        if collided_coins:
            self.coin_counter += len(collided_coins)
             # Handle coin collision here (e.g., increment score, play sound, etc.)

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
    def run(self):
        #tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.coins.update(self.world_shift)
        self.coins.draw(self.display_surface)
        self.scroll_x()
        #player
        self.player.update()
        self.horizontal_movement_colision()
        self.vertical_movement_colision()
        self.player.draw(self.display_surface)
        #coins
        font = pygame.font.Font(None, 36)
        coin_text = font.render("Coins: " + str(self.coin_counter), True, (255, 255, 255))
        self.display_surface.blit(coin_text, (10, 10))