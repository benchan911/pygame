import pygame
import random
from time import sleep

WIDTH = 500
HEIGHT = 300
BACKGROUND = (255, 255, 255)


class Scoreboard:

    def __init__(self, p1, p2) :
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font1 = pygame.font.Font('freesansbold.ttf', 120)

        h = 125
        w = 100

        # Scoreboard 1
        self.label = "Scoreboard"
        self.TextLabel = self.font.render(str(self.label), True, (0,0,0), (255,255,255))
        self.TextRect = self.TextLabel.get_rect(center=(WIDTH//2, 45))  

        # Player 1
        self.playerOneLabel = "Player 1"
        self.playerOneTextLabel = self.font.render(str(self.playerOneLabel), True, (0,0,0), (255,255,255))
        self.playerOneTextRect = self.playerOneTextLabel.get_rect(center=(w, h))
        self.playerOneScore = p1
        self.playerOneScoreText = self.font.render(str(self.playerOneScore), True, (0,0,0), (255,255,255))           
        self.playerOneScoreRect = self.playerOneScoreText.get_rect(center=(w, h+100))

        # LINE
        self.l1 = "|"
        self.l1text = self.font1.render(str(self.l1), True, (0,0,0), (255,255,255))
        self.l1rect = self.l1text.get_rect(center=(WIDTH//2, HEIGHT//2))
        
        # Player 2
        self.playerTwoLabel = "Player 2"
        self.playerTwoTextLabel = self.font.render(str(self.playerTwoLabel), True, (0,0,0), (255,255,255))
        self.playerTwoTextRect = self.playerTwoTextLabel.get_rect(center=(WIDTH-w, h))
        self.playerTwoScore = p2
        self.playerTwoScoreText = self.font.render(str(self.playerTwoScore), True, (0,0,0), (255,255,255))   
        self.playerTwoScoreRect = self.playerTwoScoreText.get_rect(center=(WIDTH-w, h+100))


class Result:

   def __init__(self, p1, p2): 
        self.font = pygame.font.Font('freesansbold.ttf', 40)  

        if p1 > p2:
            self.text = "Player 1 win!"
        elif p1 < p2:
            self.text = "Player 2 win!"
        else:
            self.text = "Draw!"

        # Score
        self.textBox = self.font.render(str(self.text), True, (0,0,0), (255,255,255))           
        self.textRect = self.textBox.get_rect(center=(WIDTH//2, HEIGHT//2))


def main():
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Player Scores
    Player1 = 0
    Player2 = 0

    state = 0

    run = True
    while run:

        screen.fill(BACKGROUND)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and state == 0:
                # Check for backspace
                if event.key == pygame.K_z:
                    print("YOU HIT Z")
                    Player1 += 1

                elif event.key == pygame.K_x:
                    print("YOU HIT X")
                    Player2 += 1
                
                elif event.key == pygame.K_f:
                    state = 1
                    count = 10
                    
                elif event.key == pygame.K_SPACE:
                    run = False

        if state == 0:
            screen1 = Scoreboard(Player1, Player2)
            screen.blit(screen1.TextLabel, screen1.TextRect)
            screen.blit(screen1.playerOneTextLabel, screen1.playerOneTextRect)
            screen.blit(screen1.playerOneScoreText, screen1.playerOneScoreRect)
            screen.blit(screen1.l1text, screen1.l1rect)
            screen.blit(screen1.playerTwoTextLabel, screen1.playerTwoTextRect)
            screen.blit(screen1.playerTwoScoreText, screen1.playerTwoScoreRect)

        elif state == 1:
            screen2 = Result(Player1, Player2)
            screen.blit(screen2.textBox, screen2.textRect)
            count -= 1
            if count > 0:
                sleep(0.1)

            else:
                state = 0
                Player1 = 0
                Player2 = 0


        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()