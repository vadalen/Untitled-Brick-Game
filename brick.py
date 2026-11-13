import tkinter # Importăm biblioteca tkinter
import random

biscuiti = []
biscuiti_heal = []
lives = 3
game_over = False

master = tkinter.Tk() # Creăm o fereastră și o asignăm variabilei master
master.title('Cărămidă Veselă') # Stabilim titlul ferestrei

# Creăm canvas-ul pe care vom desena. Îl colorăm în negru.
canvas = tkinter.Canvas(master, width=600, height=600, bg='black')

# Aici trebuie creat algoritmul


brick = canvas.create_rectangle((270, 285),(330, 315), fill='brown', outline = 'black')
line1 = canvas.create_line((280, 285), (280, 315), fill = 'black')
line2 = canvas.create_line((290, 285), (290, 315), fill = 'black')
line3 = canvas.create_line((300, 285), (300, 315), fill = 'black')
line4 = canvas.create_line((310, 285), (310, 315), fill = 'black')
line5 = canvas.create_line((320, 285), (320, 315), fill = 'black')
line6 = canvas.create_line((270, 295), (330, 295), fill = 'black')
line7 = canvas.create_line((270, 305), (330, 305), fill = 'black')
full_brick = [brick, line1, line2, line3, line4, line5, line6, line7]


def key_pressed(event):
    if not game_over:
        key_name = event.keysym
        brick_coords = canvas.coords(brick)

        if brick_coords[1] > 0 and key_name in ['w', 'W']:
            i = 0
            while i < len(full_brick):
                canvas.move(full_brick[i], 0, -10)
                i += 1
        elif brick_coords[3] < 600 and key_name in ['s', 'S']:
            i = 0
            while i < len(full_brick):
                canvas.move(full_brick[i], 0, 10)
                i += 1
        elif brick_coords[2] < 600 and key_name in ['d', 'D']:
            i = 0
            while i < len(full_brick):
                canvas.move(full_brick[i], 10, 0)
                i += 1
        elif brick_coords[0] > 0 and key_name in ['a', 'A']:
            i = 0
            while i < len(full_brick):
                canvas.move(full_brick[i], -10, 0)
                i += 1
        elif brick_coords[1] > 0 and brick_coords[3] < 600 and key_name in ['e', 'E']:
            i = 0
            while i < len(full_brick):
                canvas.move(full_brick[i], 10,-10)
                i += 1
        elif brick_coords[1] > 0 and brick_coords[0] > 0 and key_name in ['q', 'Q']:
            i = 0
            while i < len(full_brick):
                canvas.move(full_brick[i], -10, -10)
                i += 1
        elif brick_coords[3] < 600 and brick_coords[3] < 600 and key_name in ['z', 'Z']:
            i = 0
            while i < len(full_brick):
                canvas.move(full_brick[i], -10, 10)
                i += 1
        elif brick_coords[3] < 600 and brick_coords[2] < 600 and key_name in ['c', 'C']:
            i = 0
            while i < len(full_brick):
                canvas.move(full_brick[i], 10, 10)
                i += 1


def crearea_biscuiti():
    if not game_over:
        directii = ['sus', 'jos', 'stanga', 'dreapta']
        directie_selectata = random.choice(directii)

        if directie_selectata == 'sus':
            x = random.randint(0,590)
            y = 10
        elif directie_selectata == 'jos':
            x = random.randint(0, 590)
            y = 590
        elif directie_selectata == 'stanga':
            x = 10
            y = random.randint(0, 590)
        elif directie_selectata == 'dreapta':
            x = 590
            y = random.randint(0, 590)

        biscuite = canvas.create_oval((x, y), (x + 10, y + 10), fill='white')
        info_biscuite = {'id_biscuite': biscuite, 'pozitie': directie_selectata}
        biscuiti.append(info_biscuite)
        master.after(500, crearea_biscuiti)

def crearea_biscuiti_heal():
    if not game_over:
        directii = ['sus', 'jos', 'stanga', 'dreapta']
        directie_selectata = random.choice(directii)

        if directie_selectata == 'sus':
            x = random.randint(0,590)
            y = 10
        elif directie_selectata == 'jos':
            x = random.randint(0, 590)
            y = 590
        elif directie_selectata == 'stanga':
            x = 10
            y = random.randint(0, 590)
        elif directie_selectata == 'dreapta':
            x = 590
            y = random.randint(0, 590)

        biscuite = canvas.create_oval((x, y), (x + 10, y + 10), fill='yellow')
        info_biscuite = {'id_biscuite': biscuite, 'pozitie': directie_selectata}
        biscuiti_heal.append(info_biscuite)
        master.after(3000, crearea_biscuiti_heal)

def verificare_contact(biscuite):
    if not game_over:
        coordonate_biscuite = canvas.coords(biscuite)

        coordonate_contact_caramida = canvas.find_overlapping(coordonate_biscuite[0], coordonate_biscuite[1],coordonate_biscuite[2], coordonate_biscuite[3])


        if brick in coordonate_contact_caramida:
            return True
        else:
            return False

def verificare_contact_heal(biscuite):
    if not game_over:
        coordonate_biscuite = canvas.coords(biscuite)

        coordonate_contact_caramida = canvas.find_overlapping(coordonate_biscuite[0], coordonate_biscuite[1],coordonate_biscuite[2], coordonate_biscuite[3])


        if brick in coordonate_contact_caramida:
            return True
        else:
            return False


def miscare_biscuiti_heal():
    global lives, game_over
    if not game_over:
        for info_biscuite in biscuiti_heal:
            if info_biscuite['pozitie'] == 'sus':
                canvas.move(info_biscuite['id_biscuite'], 0, 3)

            elif info_biscuite['pozitie'] == 'jos':
                canvas.move(info_biscuite['id_biscuite'], 0, -3)

            elif info_biscuite['pozitie'] == 'stanga':
                canvas.move(info_biscuite['id_biscuite'], 3, 0)

            elif info_biscuite['pozitie'] == 'dreapta':
                canvas.move(info_biscuite['id_biscuite'], -3, 0)

            if verificare_contact_heal(info_biscuite['id_biscuite']) == True:
                lives += 1
                master.title('Vietile curente:' + str(lives) + '/20')
                canvas.delete(info_biscuite['id_biscuite'])
                biscuiti_heal.remove(info_biscuite)
            if lives == 20:
                game_over = True
                master.title('Ai castigat!!')

        master.after(50, miscare_biscuiti_heal)

def miscare_biscuiti():
    global lives, game_over
    if not game_over:
        for info_biscuite in biscuiti:
            if info_biscuite['pozitie'] == 'sus':
                canvas.move(info_biscuite['id_biscuite'], 0, 3)

            elif info_biscuite['pozitie'] == 'jos':
                canvas.move(info_biscuite['id_biscuite'], 0, -3)

            elif info_biscuite['pozitie'] == 'stanga':
                canvas.move(info_biscuite['id_biscuite'], 3, 0)

            elif info_biscuite['pozitie'] == 'dreapta':
                canvas.move(info_biscuite['id_biscuite'], -3, 0)

            if verificare_contact(info_biscuite['id_biscuite']) == True:
                lives -= 1
                master.title('Vietile curente:'+str(lives)+'/20')
                canvas.delete(info_biscuite['id_biscuite'])
                biscuiti.remove(info_biscuite)
            if lives == 0:
                game_over = True


        master.after(50, miscare_biscuiti)


crearea_biscuiti()
miscare_biscuiti()
crearea_biscuiti_heal()
miscare_biscuiti_heal()
master.bind('<Key>',key_pressed)

canvas.pack() # Facem canvas-ul vizibil
master.mainloop() # Afișăm fereastra
