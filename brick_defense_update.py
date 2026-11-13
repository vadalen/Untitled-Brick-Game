import tkinter # Importăm biblioteca tkinter
import random

biscuiti = []
biscuiti_heal = []
biscuiti_def = []
def_up = 0
lives = 3
game_over = False

master = tkinter.Tk() # Creăm o fereastră și o asignăm variabilei master
master.title('Cărămidă Veselă') # Stabilim titlul ferestrei

# Creăm canvas-ul pe care vom desena. Îl colorăm în negru.
canvas = tkinter.Canvas(master, width=600, height=600, bg='black')

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
            for b in full_brick:
                canvas.move(b, 0, -10)
        elif brick_coords[3] < 600 and key_name in ['s', 'S']:
            for b in full_brick:
                canvas.move(b, 0, 10)
        elif brick_coords[2] < 600 and key_name in ['d', 'D']:
            for b in full_brick:
                canvas.move(b, 10, 0)
        elif brick_coords[0] > 0 and key_name in ['a', 'A']:
            for b in full_brick:
                canvas.move(b, -10, 0)
        elif brick_coords[1] > 0 and brick_coords[2] < 600 and key_name in ['e', 'E']:
            for b in full_brick:
                canvas.move(b, 10, -10)
        elif brick_coords[1] > 0 and brick_coords[0] > 0 and key_name in ['q', 'Q']:
            for b in full_brick:
                canvas.move(b, -10, -10)
        elif brick_coords[3] < 600 and brick_coords[0] > 0 and key_name in ['z', 'Z']:
            for b in full_brick:
                canvas.move(b, -10, 10)
        elif brick_coords[3] < 600 and brick_coords[2] < 600 and key_name in ['c', 'C']:
            for b in full_brick:
                canvas.move(b, 10, 10)


def crearea_biscuiti():
    if not game_over:
        directii = ['sus', 'jos', 'stanga', 'dreapta']
        directie_selectata = random.choice(directii)

        if directie_selectata == 'sus':
            x, y = random.randint(0, 590), 10
        elif directie_selectata == 'jos':
            x, y = random.randint(0, 590), 590
        elif directie_selectata == 'stanga':
            x, y = 10, random.randint(0, 590)
        elif directie_selectata == 'dreapta':
            x, y = 590, random.randint(0, 590)

        biscuite = canvas.create_oval((x, y), (x + 10, y + 10), fill='white')
        info_biscuite = {'id_biscuite': biscuite, 'pozitie': directie_selectata}
        biscuiti.append(info_biscuite)
        master.after(500, crearea_biscuiti)

def crearea_biscuiti_heal():
    if not game_over:
        directii = ['sus', 'jos', 'stanga', 'dreapta']
        directie_selectata = random.choice(directii)

        if directie_selectata == 'sus':
            x, y = random.randint(0, 590), 10
        elif directie_selectata == 'jos':
            x, y = random.randint(0, 590), 590
        elif directie_selectata == 'stanga':
            x, y = 10, random.randint(0, 590)
        elif directie_selectata == 'dreapta':
            x, y = 590, random.randint(0, 590)

        biscuite = canvas.create_oval((x, y), (x + 10, y + 10), fill='yellow')
        info_biscuite = {'id_biscuite': biscuite, 'pozitie': directie_selectata}
        biscuiti_heal.append(info_biscuite)
        master.after(3000, crearea_biscuiti_heal)


def crearea_biscuiti_defense():
    if not game_over:
        directii = ['sus', 'jos', 'stanga', 'dreapta']
        directie_selectata = random.choice(directii)

        if directie_selectata == 'sus':
            x, y = random.randint(0, 590), 10
        elif directie_selectata == 'jos':
            x, y = random.randint(0, 590), 590
        elif directie_selectata == 'stanga':
            x, y = 10, random.randint(0, 590)
        elif directie_selectata == 'dreapta':
            x, y = 590, random.randint(0, 590)

        biscuite = canvas.create_oval((x, y), (x + 10, y + 10), fill='green')
        info_biscuite = {'id_biscuite': biscuite, 'pozitie': directie_selectata}
        biscuiti_def.append(info_biscuite)
        master.after(5000, crearea_biscuiti_defense)


def verificare_contact(biscuite):
    coordonate_biscuite = canvas.coords(biscuite)
    if not coordonate_biscuite:
        return False
    coordonate_contact_caramida = canvas.find_overlapping(
        coordonate_biscuite[0], coordonate_biscuite[1],
        coordonate_biscuite[2], coordonate_biscuite[3]
    )
    return brick in coordonate_contact_caramida


def miscare_biscuiti_heal():
    global lives, game_over
    if not game_over:
        for info_biscuite in biscuiti_heal[:]:
            if info_biscuite['pozitie'] == 'sus':
                canvas.move(info_biscuite['id_biscuite'], 0, 3)
            elif info_biscuite['pozitie'] == 'jos':
                canvas.move(info_biscuite['id_biscuite'], 0, -3)
            elif info_biscuite['pozitie'] == 'stanga':
                canvas.move(info_biscuite['id_biscuite'], 3, 0)
            elif info_biscuite['pozitie'] == 'dreapta':
                canvas.move(info_biscuite['id_biscuite'], -3, 0)

            if verificare_contact(info_biscuite['id_biscuite']):
                lives = min(20, lives + 1)
                master.title(f'Vietile curente: {lives}/20')
                canvas.delete(info_biscuite['id_biscuite'])
                biscuiti_heal.remove(info_biscuite)
                if lives >= 20:
                    game_over = True
                    master.title('Ai castigat!!')

        master.after(50, miscare_biscuiti_heal)

def miscare_biscuiti_defense():
    global def_up, lives, game_over
    if not game_over:
        for info_biscuite in biscuiti_def[:]:
            if info_biscuite['pozitie'] == 'sus':
                canvas.move(info_biscuite['id_biscuite'], 0, 3)
            elif info_biscuite['pozitie'] == 'jos':
                canvas.move(info_biscuite['id_biscuite'], 0, -3)
            elif info_biscuite['pozitie'] == 'stanga':
                canvas.move(info_biscuite['id_biscuite'], 3, 0)
            elif info_biscuite['pozitie'] == 'dreapta':
                canvas.move(info_biscuite['id_biscuite'], -3, 0)

            if verificare_contact(info_biscuite['id_biscuite']):
                def_up = 1
                master.title(f'Vietile curente: {lives}/20 - Defense UP!')
                canvas.delete(info_biscuite['id_biscuite'])
                biscuiti_def.remove(info_biscuite)

        master.after(50, miscare_biscuiti_defense)

def miscare_biscuiti():
    global lives, game_over, def_up
    if not game_over:
        for info_biscuite in biscuiti[:]:
            if info_biscuite['pozitie'] == 'sus':
                canvas.move(info_biscuite['id_biscuite'], 0, 3)
            elif info_biscuite['pozitie'] == 'jos':
                canvas.move(info_biscuite['id_biscuite'], 0, -3)
            elif info_biscuite['pozitie'] == 'stanga':
                canvas.move(info_biscuite['id_biscuite'], 3, 0)
            elif info_biscuite['pozitie'] == 'dreapta':
                canvas.move(info_biscuite['id_biscuite'], -3, 0)

            if verificare_contact(info_biscuite['id_biscuite']):
                if def_up == 1:
                    def_up = 0  # consumăm scutul
                    master.title(f'Vietile curente: {lives}/20 - Scutul te-a salvat!')
                else:
                    lives -= 1
                    master.title(f'Vietile curente: {lives}/20')

                canvas.delete(info_biscuite['id_biscuite'])
                biscuiti.remove(info_biscuite)

                if lives <= 0:
                    game_over = True
                    master.title('Game Over! Ai pierdut.')

        master.after(50, miscare_biscuiti)


# Pornirea buclelor jocului
crearea_biscuiti()
miscare_biscuiti()
crearea_biscuiti_heal()
miscare_biscuiti_heal()
crearea_biscuiti_defense()
miscare_biscuiti_defense()

master.bind('<Key>', key_pressed)
canvas.pack()
master.mainloop()