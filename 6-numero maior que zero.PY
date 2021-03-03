# 6-Estruturas condicionais dentro de condicionais
from pyfirmata import Arduino
import lcd
import time

board=Arduino ('COM6')
var1 = 0
var2 = int(input(lcd.escrever(board, 0, 0, 'DIGITE UM NUMERO')))

if var2 > var1:
    lcd.escrever(board, 0, 0, 'NUM MAIOR Q ZERO')
    if var2 == 1:
        lcd.escrever(board, 0, 1, 'O NUM DIGITADO 1')
    if var2 == 2:
        lcd.escrever(board, 0, 1, 'O NUM DIGITADO 2')
    if var2 == 3:
        lcd.escrever(board, 0, 1, 'O NUM DIGITADO 3')
    else:
        lcd.escrever(board, 0, 1, 'O NUM INVALIDO')

time.sleep(100.0)
lcd.limpar(board)
board.exit()