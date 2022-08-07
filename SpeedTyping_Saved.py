# SPEED TYPING TEST
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


class Ready:

    def __init__(self, seconds, word, n, l):
        
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font1 = pygame.font.Font('freesansbold.ttf', 24)

        x = 30
        # Player Turn
        self.nLabel = f"P{n}"
        
        if n == 1:
            self.nLabel = self.font1.render(str(self.nLabel), True, (255,0,0), (255, 255, 255))
            self.nRect = self.nLabel.get_rect(center=(WIDTH-x, x))  
        elif n == 2:
            self.nLabel = self.font1.render(str(self.nLabel), True, (0,0,255), (255, 255, 255))
            self.nRect = self.nLabel.get_rect(center=(WIDTH-x, x))  

        # Level
        self.nLabel1 = f"Level {l}"
        self.nLabel1 = self.font1.render(str(self.nLabel1), True, (0,0,0), (255, 255, 255))
        self.nRect1 = self.nLabel1.get_rect(center=(x*2, x))

        # Memorise
        self.label = f"Ready in {seconds}"
        self.TextLabel = self.font.render(str(self.label), True, (0,0,0), (255,255,255))
        self.TextRect = self.TextLabel.get_rect(center=(WIDTH//2, 125))  

        # Memorise
        self.label1 = f"{word}"
        self.TextLabel1 = self.font.render(str(self.label1), True, (0,0,0), (255,255,255))
        self.TextRect1 = self.TextLabel1.get_rect(center=(WIDTH//2, 225))  


class Answer:

    def __init__(self, word, w, n):
        
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font1 = pygame.font.Font('freesansbold.ttf', 24)

        x = 30

        # Memorise
        self.label = f"{w}"
        self.TextLabel = self.font.render(str(self.label), True, (0,0,0), (255,255,255))
        self.TextRect = self.TextLabel.get_rect(center=(WIDTH//2, 45))  

        # Memorise
        self.label1 = f"{word}"
        self.TextLabel1 = self.font.render(str(self.label1), True, (0,0,0), (255,255,255))
        self.TextRect1 = self.TextLabel1.get_rect(center=(WIDTH//2, 225))  

        # COUNT TOP RIGHT
        self.nLabel = f"{n}"
        self.nLabel = self.font1.render(str(self.nLabel), True, (0,0,0), (255, 255, 255))
        self.nRect = self.nLabel.get_rect(center=(WIDTH-x-100, x))

class Result:

    def __init__(self, s1, s2):
        self.font0 = pygame.font.Font('freesansbold.ttf', 60)  
        self.font = pygame.font.Font('freesansbold.ttf', 120)  

        h = HEIGHT // 2

        # Score
        self.playerOneScore = "You scored"
        self.playerOneScoreText = self.font0.render(str(self.playerOneScore), True, (0,0,0), (255,255,255))           
        self.playerOneScoreRect = self.playerOneScoreText.get_rect(center=(WIDTH//2, HEIGHT//2-110))

        # Total
        self.playerTwoScore = f'{s1} / {s2}'
        self.playerTwoScoreText = self.font.render(str(self.playerTwoScore), True, (0,0,0), (255,255,255))   
        self.playerTwoScoreRect = self.playerTwoScoreText.get_rect(center=(WIDTH//2, HEIGHT//2+50))



def main():
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    state = 0
    count = 5

    countdown = {
        1: 3,
        2: 3,
        3: 3,
    }

    length_of_words = {
        1: 5,
        2: 8,
        3: 12
    }

    user_text = ''
    # Player Scores
    Player1 = 0
    Player2 = 0

    # Current Player Turn 
    # 0 - Player 1
    # 1 - Player 2 
    player_turn = 0

    # Current Level 
    level = 1

    while True:

        digits = length_of_words[level]

        screen.fill(BACKGROUND)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and state == 2:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                # Unicode standard is used for string
                # formation
                elif event.key == pygame.K_SPACE:
                    if state == 2:
                        state = 3
                else:
                    user_text += event.unicode
                print(user_text)

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if state == 0:
                # state = (state + 1) % 2
                state = 1
                count = countdown[level]
                # word = wordList[1]
        
        elif pygame.key.get_pressed()[pygame.K_q]:
            if state == 0:
                break

        if state == 0: # SCOREBOARD
            screen1 = Scoreboard(Player1, Player2)
            screen.blit(screen1.TextLabel, screen1.TextRect)
            screen.blit(screen1.playerOneTextLabel, screen1.playerOneTextRect)
            screen.blit(screen1.playerOneScoreText, screen1.playerOneScoreRect)
            screen.blit(screen1.l1text, screen1.l1rect)
            screen.blit(screen1.playerTwoTextLabel, screen1.playerTwoTextRect)
            screen.blit(screen1.playerTwoScoreText, screen1.playerTwoScoreRect)
            word = ''
            for i in range(digits):
                word+=str(chr(random.randint(1,26)+64))

        elif state == 1: # MEMORISE
            screen2 = Ready( "{}".format(count), word, player_turn+1, level)
            screen.blit(screen2.nLabel, screen2.nRect)
            screen.blit(screen2.nLabel1, screen2.nRect1)
            screen.blit(screen2.TextLabel, screen2.TextRect)
            screen.blit(screen2.TextLabel1, screen2.TextRect1)
            count -= 1 #0.01
            sleep(1) #0.01)
            if count <= 0: 
                state = 2
                user_text = ''
                count0 = 5
                step_counter = 10
        
        elif state == 2:  # ANSWER 
            screen3 = Answer(user_text, word, count0)
            screen.blit(screen3.TextLabel, screen3.TextRect)
            screen.blit(screen3.TextLabel1, screen3.TextRect1)
            screen.blit(screen3.nLabel, screen2.nRect)

            if count0 > 0:
                sleep(0.1)
                step_counter -= 1
                if step_counter < 0:
                    count0 -= 1
                    step_counter = 10

            elif count0 <= 0:
                state = 3
                user_text = ''

        elif state == 3: # RESULT
            s = 0 
            for i in range(len(word)):
                try:
                    if word[i].lower() == user_text[i].lower():
                        s += 1
                except:
                    break
            print(f'{s} / {len(word)}')
            screen4 = Result(s, digits)
            screen.blit(screen4.playerOneScoreText, screen4.playerOneScoreRect)
            screen.blit(screen4.playerTwoScoreText, screen4.playerTwoScoreRect)
            pygame.display.flip()

            # HOLD
            for i in range(5):
                sleep(1)
            
            # Update the player turn
            if player_turn == 0:
                Player1 += s
                player_turn = 1
            
            elif player_turn == 1:
                Player2 += s
                player_turn = 0
                level += 1
            state = 0

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()