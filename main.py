import pygame
import random
import sys
import asyncio

import requests
import io

import threading

s_r = requests.session()

def get_image(url : str, target : list):
    data = io.BytesIO()
    response = s_r.get(url, stream=True)      
    if not response.ok:
        print(response)

    for block in response.iter_content(1024):
        if not block:
            break
        data.write(block)

    data.seek(0)
    target.append(pygame.image.load(data))

RUN_URLS = [
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run1.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run2.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run3.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run4.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run5.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run6.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run7.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run8.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run9.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run10.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run11.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run12.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run13.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run14.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run15.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run16.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run17.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run18.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run19.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Run20.png"
]
RUN = []
JUMP_URLS = [
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump1.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump2.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump3.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump4.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump5.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump6.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump7.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump8.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump9.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump10.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump11.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump12.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump13.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump14.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump15.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump16.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump17.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump18.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump19.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump20.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump21.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump22.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump23.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump24.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump25.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump26.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump27.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump28.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump29.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Jump30.png"
]
JUMP = []
OBSTACLES_URLS = [
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/H.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/A1.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/P1.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/P2.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Y1.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/V.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/E.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/R.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/A2.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/D.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/A3.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/Y2.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/cake.png"
]
OBSTACLES = []
BUTTON_URLS = [
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/easy.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/again.png"
]
BUTTON = []
SCENE_URLS = [
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/start.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/end.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/lose.png",
    "https://raw.githubusercontent.com/Charleywang246/HBD/main/awww.png"
]
SCENE_RAW = []

run_thread = [threading.Thread(target=get_image(url, RUN)) for url in RUN_URLS]
jump_thread = [threading.Thread(target=get_image(url, JUMP)) for url in JUMP_URLS]
obstacle_thread = [threading.Thread(target=get_image(url, OBSTACLES)) for url in OBSTACLES_URLS]
button_thread = [threading.Thread(target=get_image(url, BUTTON)) for url in BUTTON_URLS]
scene_thread = [threading.Thread(target=get_image(url, SCENE_RAW)) for url in SCENE_URLS]
for thread in run_thread:
    thread.start()
for thread in jump_thread:
    thread.start()

for thread in button_thread:
    thread.start()

for thread in obstacle_thread:
    thread.start()
    thread.join()
OBSTACLES_AD = [
    pygame.transform.scale(OBSTACLES[0], (160,220)),
    pygame.transform.scale(OBSTACLES[1], (180,220)),
    pygame.transform.scale(OBSTACLES[2], (180,220)),
    pygame.transform.scale(OBSTACLES[3], (180,220)),
    pygame.transform.scale(OBSTACLES[4], (180,220)),
    pygame.transform.scale(OBSTACLES[5], (180,220)),
    pygame.transform.scale(OBSTACLES[6], (180,220)),
    pygame.transform.scale(OBSTACLES[7], (180,220)),
    pygame.transform.scale(OBSTACLES[8], (180,220)),
    pygame.transform.scale(OBSTACLES[9], (180,220)),
    pygame.transform.scale(OBSTACLES[10], (180,200)),
    pygame.transform.scale(OBSTACLES[11], (180,200)),
    OBSTACLES[12]
]

for thread in scene_thread:
    thread.start()
    thread.join()

SCENE = [
    pygame.transform.scale(SCENE_RAW[0], (1200,700)),
    pygame.transform.scale(SCENE_RAW[1], (1200,700)),
    pygame.transform.scale(SCENE_RAW[2], (1200,700)),
    pygame.transform.scale(SCENE_RAW[3], (1200,700))
]

B = []
BACKGROUND = get_image("https://raw.githubusercontent.com/Charleywang246/HBD/main/BG.png", B)
BG = pygame.transform.scale(B[0], (1200,700))

pygame.init()

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1200
GAMESPEED = 17
pygame.display.set_caption("For Vera")
pygame.display.set_icon(pygame.image.load("icon.png"))
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class girl:
    X_POS = 80
    Y_POS = 400
    JUMP_V = 25
    IMAGE_X = 192.5
    IMAGE_Y = 224.5
    
    def __init__(self):
        self.run_img = RUN
        self.jump_img = JUMP
        
        self.girl_run = True
        self.girl_jump = False
        
        self.step_index_RUN = 0
        self.step_index_JUMP = 0
        self.image_size = (self.IMAGE_X, self.IMAGE_Y)
        self.image = pygame.transform.scale(self.run_img[0], self.image_size) 
        self.girl_rect = self.image.get_rect()
        self.jump_v = self.JUMP_V
        self.girl_rect.x = self.X_POS
        self.girl_rect.y = self.Y_POS
            
    def running(self):
        self.image = pygame.transform.scale(self.run_img[self.step_index_RUN], self.image_size) 
        self.girl_rect = self.image.get_rect()
        self.girl_rect.x = self.X_POS
        self.girl_rect.y = self.Y_POS 
        
        if self.step_index_RUN >= 19:
            self.step_index_RUN = 0
        
        self.step_index_RUN += 1 
        
    def jumping(self):  
        self.image = pygame.transform.scale(self.jump_img[self.step_index_JUMP], self.image_size) 
        
        self.girl_rect.y -= self.jump_v
        self.jump_v -= 1
        self.step_index_JUMP +=1
        
        if self.step_index_JUMP >=29:
            self.step_index_JUMP = 29
        
        if self.girl_rect.y >= self.Y_POS:
            self.step_index_JUMP = 0
            self.girl_jump = False
            self.girl_run = True
            self.jump_v = self.JUMP_V


    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.girl_rect.x, self.girl_rect.y))
        
    def update(self, userinput):
        if self.girl_run:
            self.running()
            
        if self.girl_jump:
            self.jumping()
            
        if userinput[pygame.K_SPACE] and not self.girl_jump:
            self.girl_jump = True
            self.girl_run = False
        
            
        # self.image = pygame.transform.scale(self.image, (self.image_size[0]*0.5, self.image_size[1]*0.5))
    

class obstacles:
    
    def __init__(self, index, y_pos):
        self.obstacle_image = OBSTACLES_AD[index]
        self.obstacle_rect = self.obstacle_image.get_rect()
        self.obstacle_rect.x = SCREEN_WIDTH*(index + 1) + random.randint(SCREEN_WIDTH*0.6, SCREEN_WIDTH)
        self.obstacle_rect.y = y_pos
        
    def update(self):
        self.obstacle_rect.x -= game_speed
        
        
    def draw(self, SCREEN):
        SCREEN.blit(self.obstacle_image, (self.obstacle_rect.x, self.obstacle_rect.y))

class button:
    
    def __init__(self, index, button_pos, button_size):
        self.button_image = pygame.transform.scale(BUTTON[index], button_size) 
        self.button_rect = self.button_image.get_rect()
        self.button_rect.x = button_pos[0]
        self.button_rect.y = button_pos[1]
    
    def draw(self, SCREEN):
        SCREEN.blit(self.button_image, (self.button_rect.x, self.button_rect.y))
    
async def main(mode):
    global game_speed, BG_X_POS, BG_Y_POS, OBS, start, run, lose, end
    end = False
    run = True
    lose = False
    clock = pygame.time.Clock()
    player = girl()
    OBS = [obstacles(0,400), obstacles(1,400), obstacles(2,400), obstacles(3, 400), obstacles(4, 420), obstacles(5, 400), obstacles(6, 400), obstacles(7, 400), obstacles(8, 400), obstacles(9, 400),obstacles(10, 420), obstacles(11, 420), obstacles(12, 200)]
    game_speed = GAMESPEED
    BG_X_POS = 0
    BG_Y_POS = 0

    
    def background():
        global game_speed, BG_X_POS, BG_Y_POS
        BG_WIDTH = BG.get_width()
        SCREEN.blit(BG, (BG_X_POS, BG_Y_POS))
        SCREEN.blit(BG, (BG_WIDTH + BG_X_POS, BG_Y_POS))
        
        if BG_X_POS <= -BG_WIDTH:
            BG_X_POS = 0
        BG_X_POS -=game_speed
        
    async def lose_menu():
        global lose, run, start
        
        button_easy_pos = (275, 400)
        button_again_pos = (900, 600)
        button_easy_size = (650, 100)
        button_again_size = (250, 48)
        button_easy = button(0, button_easy_pos, button_easy_size)
        button_again = button(1, button_again_pos, button_again_size)
                
        SCREEN.blit(SCENE[1], (0,0))
        button_easy.draw(SCREEN)
        button_again.draw(SCREEN)
        pygame.display.update()
        
        while lose:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_again.button_rect.collidepoint(pygame.mouse.get_pos()):
                        await main("NORMAL")
                    elif button_easy.button_rect.collidepoint(pygame.mouse.get_pos()):
                        await main("EASY")
                        
            await asyncio.sleep(0)
        
    async def end_menu():
        global end, run, start, game_speed
        SCREEN.blit(SCENE[2], (0,0))
        pygame.display.update()
        game_speed = 0
        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                    
            asyncio.sleep(0)

        
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        
        SCREEN.fill((0, 0, 0))
        userinput = pygame.key.get_pressed()
        background()
        player.update(userinput)
        player.draw(SCREEN)
        
        if mode == "NORMAL":
            for obs in OBS:
                obs.draw(SCREEN)
                obs.update()

                if player.girl_rect.colliderect(OBS[12].obstacle_rect):
                    end = True
                    await end_menu()
                    run = False

                elif player.girl_rect.colliderect(obs.obstacle_rect):

                    lose = True
                    await lose_menu()
                
        elif mode == "EASY":
             for obs in OBS:
                obs.draw(SCREEN)
                obs.update()

                if player.girl_rect.colliderect(OBS[12].obstacle_rect):
                    await end_menu()
                
                elif player.girl_rect.colliderect(obs.obstacle_rect):
                    obs.obstacle_rect.x -= 400
                    SCREEN.blit(SCENE[3], (0,0))
                    pygame.display.update()
                    pygame.time.wait(900)
                
        clock.tick(35)
        pygame.display.update()
        await asyncio.sleep(0)
 

           
async def start_menu():
    global start, SCENE
    start = True
    clock = pygame.time.Clock()

    SCREEN.blit(SCENE[0], (0,0))
    pygame.display.update()

    while start:
        
                
        clock.tick(30)
        pygame.display.update()    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            elif event.type == pygame.KEYDOWN:
                await main("NORMAL")
                
        await asyncio.sleep(0)
                
       
asyncio.run(start_menu())