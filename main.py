import sys, random, os,time 
import pygame
import matplotlib.pyplot as plt

#mapplotlib de ve do thi
MAP_WIDTH, MAP_HEIGHT = 10,18
TILE_SIZE = 40 #40 pixel 1 can ho 
SC_WIDTH, SC_HEIGHT = 450,770
PAUSE_LENGTH = 0.25
FIRE_SPREAD_CHANCE = 0.25
FIRE_CHANCE = 0.0001
SIM_LENGTH = 18 #so lan lap lai


#khoi tao pygame
pygame.init()
screen = pygame.display.set_mode((SC_WIDTH,SC_HEIGHT))

#convert: load anh cay vao window

TREE_IMG = pygame.image.load(os.path.join("BuildingFire","Graphics","apartment1.jpg")).convert_alpha()
FIRE_IMG = pygame.image.load(os.path.join("BuildingFire","Graphics","Fire_Small.png")).convert_alpha()
FIRE_GIF = pygame.image.load(os.path.join("BuildingFire","Graphics","fire-gif.gif")).convert_alpha()
FIRE_APARTMENT_IMG = pygame.image.load(os.path.join("BuildingFire","Graphics","fire-apartment.jpg")).convert_alpha()
STAIR_IMG = pygame.image.load(os.path.join("BuildingFire","Graphics","stair4.jpg")).convert_alpha()
LINE_IMG = pygame.image.load(os.path.join("BuildingFire","Graphics","line.png")).convert_alpha()
MOTORBIKE_IMG = pygame.image.load(os.path.join("BuildingFire","Graphics","motorbike3.png")).convert_alpha()


trees = []
fires = []

#hàm main chạy chương trình chính, pop-up dùng thư viện pygame
def main():
    apartment = createNewForest()

    # for _ in range(SIM_LENGTH):
    for _ in range(SIM_LENGTH):
        random_num = random.random()
        for event in pygame.event.get():

        #dieu kien thoat
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #ve do thi so cay va so nha bi chay: dem so cay va ngon lua
        tree_count = sum(row.count("T") for row in apartment)
        tree_land_percentage = (tree_count/(MAP_HEIGHT*MAP_WIDTH))*100
        trees.append(tree_land_percentage)

        fire_count = sum(row.count("F") for row in apartment)
        fire_land_percentage = (fire_count/(MAP_HEIGHT*MAP_WIDTH))*100
        fires.append(fire_land_percentage)

        #khai bao
        next_apartment = [["Empty" for x in range (MAP_WIDTH)] for y in range (MAP_HEIGHT)]
        screen.fill((255,255,255)) #lightgreen

#toa do can ho bi chay
        apartment[15][4] = "F"

        # apartment[3][5] = "F"

        # apartment[6][7] = "F"

        # apartment[17][6] = "F"

        #hien thi
        displayForest(apartment)

        #Thuat toan chinh: 
        i = 0
        for x in range (MAP_WIDTH):
            for y in range(MAP_HEIGHT):
                if next_apartment[y][x] != "Empty":
                    continue
                elif apartment[y][x] == "F":
                    for ix in range (-1,2): 
                        for iy in range(-1,2):
                            if (x + ix) >= 0 and (y + iy) >= 0:
                                if (x + ix) <= (MAP_WIDTH - 1) and (y + iy) <= (MAP_HEIGHT-1):
                                    #check neighboor
                                    if (apartment[y+iy][x+ix] == "T"):
                                        if ((x+1) <= (MAP_WIDTH-1) and y-1 >= 0):    
                                            next_apartment[y-1][x] ="F"
                                            if(random.random() < 0.05):
                                                next_apartment[y][x+1] ="F"
                                            if(random.random() < 0.05):
                                                next_apartment[y][x-1] ="F"        
                    #thay can ho = can ho chay
                    next_apartment[y][x] = "F"
                    i = i+1
                else:
                    next_apartment[y][x] = apartment[y][x]
        #Thay doi
        apartment = next_apartment

        #Thoi gian chay
        time.sleep(PAUSE_LENGTH)

        #update the screen
        pygame.display.update() 
    
    #ve do thi 
    fig, ax = plt.subplots()
    ax.plot(trees, color = 'green', label = 'Apartment')
    ax.plot(fires, color ='red', label ='Fired Apartment')
    ax.legend(loc = 'upper right')
    ax.set_xlabel = ("Time")
    ax.set_ylabel = ("%")    
    plt.show()

#Khoi tao 1 map hien thi cây random 
def createNewForest():
    #Tao ban do hien thi mang 2 chieu
    map = [["T"
        for x in range(MAP_WIDTH) ]
        for y in range(MAP_HEIGHT)]
    return map

#Hien thi cay
def displayForest(apartment):
    for x in range(0, MAP_WIDTH):
        for y in range(0, MAP_HEIGHT):
            if apartment[y][x] == "T":
                screen.blit(TREE_IMG, (x*TILE_SIZE, y*TILE_SIZE))
            elif apartment[y][x] == "F":
                screen.blit(FIRE_IMG, (x*TILE_SIZE, y*TILE_SIZE))
            elif apartment[y][x] == "F-A":
                screen.blit(FIRE_APARTMENT_IMG, (x*TILE_SIZE, y*TILE_SIZE))
    for y in range(0, MAP_HEIGHT+1):
        screen.blit(STAIR_IMG, (10*TILE_SIZE, y*TILE_SIZE))

    screen.blit(LINE_IMG, (0*TILE_SIZE, 18*TILE_SIZE))
    
    for x in range(0, MAP_WIDTH):
        screen.blit(MOTORBIKE_IMG, (x*TILE_SIZE, 18.25*TILE_SIZE))

    
if __name__ =='__main__':
    main()