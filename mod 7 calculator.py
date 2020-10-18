import pygame
import math
from pygame.locals import *
from fractions import Fraction as frac
from decimal import Decimal

pygame.init()
pygame.display.set_caption('Calculator')

FPS = 30
white = (255, 255, 255)
black = (0, 0, 0)
background = (150, 242, 190)
transparent = (0,0,0,0)
red = (255,0,0)
pink = (242, 191, 235)
blue = (142, 228, 245)
clock=pygame.time.Clock()
gameDisplay = pygame.display.set_mode((700,500))
rectpos = (0,0)
font = pygame.font.SysFont(None,40)
equation = ''
y=0
answer=''
text=font.render(str(answer), False, black)


mouse = pygame.draw.rect(gameDisplay,transparent,Rect((rectpos),(10,10)))

def gcd(dividend, divisor):
  if 0 == divisor:
    return 1, 0, dividend
  x2, y2, remainder = gcd(divisor, dividend % divisor)

  temp = x2
  x1 = y2
  y1 = temp - int(math.floor(dividend/divisor)) * y2

  return x1, y1, remainder

def add_space(number):
    number = number.replace("+", " + ")
    number = number.replace("-", " - ")
    number = number.replace("*", " * ")
    number = number.replace("/", " / ")
    number = number.replace("(", " ( ")
    number = number.replace(")", " ) ")
    return number

def precedence(op): 
      
    if op == '+' or op == '-': 
        return 1
    if op == '*' or op == '/': 
        return 2
    return 0
  
def applyOp(a, b, op):   
    if op == '+': return (a + b) % 7
    if op == '-': return (a - b) % 7
    if op == '*': return (a * b) % 7
    if op == '/':
        first, second, third = gcd(b, 7)
        return (a * first) % 7
 
def evaluate(tokens): 
    values = [] 
    ops = [] 
    i = 0
      
    while i < len(tokens): 
        if tokens[i] == ' ': 
            i += 1
            continue
        elif tokens[i] == '(': 
            ops.append(tokens[i]) 
        elif tokens[i].isdigit(): 
            val = 0
            while (i < len(tokens) and
                tokens[i].isdigit()): 
              
                val = (val * 10) + int(tokens[i]) 
                i += 1
              
            values.append(val) 
        elif tokens[i] == ')': 
          
            while len(ops) != 0 and ops[-1] != '(': 
              
                val2 = values.pop() 
                val1 = values.pop() 
                op = ops.pop() 
                  
                values.append(applyOp(val1, val2, op)) 
              
            ops.pop() 
          
        else: 
            while (len(ops) != 0 and
                precedence(ops[-1]) >= precedence(tokens[i])): 
                          
                val2 = values.pop() 
                val1 = values.pop() 
                op = ops.pop() 
                  
                values.append(applyOp(val1, val2, op)) 
              
            ops.append(tokens[i]) 
          
        i += 1

    while len(ops) != 0: 
          
        val2 = values.pop() 
        val1 = values.pop() 
        op = ops.pop() 
                  
        values.append(applyOp(val1, val2, op)) 
      
    return values[-1] 

while True:
    try:
        pygame.display.set_caption('Calculator')
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                rectpos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse.colliderect(button1):
                    equation = equation + '1'
                if mouse.colliderect(button2):
                    equation = equation + '2'
                if mouse.colliderect(button3):
                    equation = equation + '3'
                if mouse.colliderect(button4):
                    equation = equation + '4'
                if mouse.colliderect(button5):
                    equation = equation + '5'
                if mouse.colliderect(button6):
                    equation = equation + '6'
                if mouse.colliderect(button0):
                    equation = equation + '0'
                if mouse.colliderect(buttonAdd):
                    equation = equation + '+'
                if mouse.colliderect(buttonSubtract):
                    equation = equation + '-'
                if mouse.colliderect(buttonMultiply):
                    equation = equation + '*'
                if mouse.colliderect(buttonDivide):
                    equation = equation + '/'
                if mouse.colliderect(buttonLeftBracket):
                    equation = equation + '('
                if mouse.colliderect(buttonRightBracket):
                    equation = equation + ')'
                if mouse.colliderect(buttonEquals):
                    if equation[0] != '+' or equation[0] != '-' or equation[0] != '*' or equation[0] != '/':
                        '''
                        answer = eval(equation)
                        answer = str(answer)
                        #print(answer)
                        answer = frac(Decimal(answer))
                        #print(answer)
                        answer_gcd = math.gcd(answer.numerator,answer.denominator)
                        numerator = (answer.numerator)/answer_gcd
                        #print(numerator)
                        denominator = (answer.denominator)/answer_gcd
                        #print(denominator)                     
                        inv, b, c = gcd(denominator, 7)
                        answer = int((numerator * inv) % 7)
                        '''
                        equation = add_space(equation)
                        answer = evaluate(equation)
                        text = font.render('='+str(answer), False, black)
                        gameDisplay.blit(text, (0,40))
                    else:
                        answer = '=Error'
                if mouse.colliderect(buttonClear):
                    equation = ''

            if event.type == QUIT:
                pygame.quit()

        gameDisplay.fill(background)
        mouse = pygame.draw.rect(gameDisplay,white,Rect((rectpos),(10,10)))

        button1 = pygame.draw.rect(gameDisplay,white,Rect(10, 210, 100, 100))
        gameDisplay.blit(font.render('1',True,black), (60,260))

        button2 = pygame.draw.rect(gameDisplay,white,Rect(120, 210, 100, 100))
        gameDisplay.blit(font.render('2',True,black), (170,260))

        button3 = pygame.draw.rect(gameDisplay,white,Rect(230,210,100,100))
        gameDisplay.blit(font.render('3',True,black), (280,260))

        button4 = pygame.draw.rect(gameDisplay,white,Rect(10,100,100,100))
        gameDisplay.blit(font.render('4',True,black), (60,150))

        button5 = pygame.draw.rect(gameDisplay,white,Rect(120,100,100,100))
        gameDisplay.blit(font.render('5',True,black), (170,150))

        button6 = pygame.draw.rect(gameDisplay,white,Rect(230,100,100,100))
        gameDisplay.blit(font.render('6',True,black), (280,150))

        button0 = pygame.draw.rect(gameDisplay,white,Rect(10,320,100,100))
        gameDisplay.blit(font.render('0',True,black), (60,370))

        buttonAdd = pygame.draw.rect(gameDisplay,white,Rect(340, 210, 100, 100))
        gameDisplay.blit(font.render('+',True,black), (390,260))

        buttonSubtract = pygame.draw.rect(gameDisplay,white,Rect(450, 210, 100, 100))
        gameDisplay.blit(font.render('-',True,black), (500,260))

        buttonMultiply = pygame.draw.rect(gameDisplay,white,Rect(340, 320, 100, 100))
        gameDisplay.blit(font.render('*',True,black), (390,370))

        buttonDivide = pygame.draw.rect(gameDisplay,white,Rect(450, 320, 100, 100))
        gameDisplay.blit(font.render('/',True,black), (500,370))

        buttonEquals = pygame.draw.rect(gameDisplay,white,Rect(450, 100, 100, 100))
        gameDisplay.blit(font.render('=',True,black), (500,150))

        buttonClear = pygame.draw.rect(gameDisplay,white,Rect(340, 100, 100, 100))
        gameDisplay.blit(font.render('C',True,black), (390,150))

        buttonLeftBracket = pygame.draw.rect(gameDisplay,white,Rect(120, 320, 100, 100))
        gameDisplay.blit(font.render('(',True,black), (170,370))

        buttonRightBracket = pygame.draw.rect(gameDisplay,white,Rect(230, 320, 100, 100))
        gameDisplay.blit(font.render(')',True,black), (280,370))

        gameDisplay.blit(font.render(equation,True,black), (250,y))
        gameDisplay.blit(text, (250,40))

        clock.tick(FPS)
        pygame.display.update()
    except SyntaxError:
        answer = 'ERROR'