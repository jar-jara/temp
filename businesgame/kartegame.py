from random import *
def kartegame():
    def draw_text(screen, text, x, y):
    text_surface = font.render(text, False, (0, 0, 0))
    screen.blit(text_surface, (x, y))

    class Karta():
        def __init__(self, credits, man, reputation):
            self.credits = credits
            self.man = man
            self.reputation = reputation
    def cards():
        kards = [
        karta1 = Karta(5000, 2, 10),
        karta2 = Karta(1000, 5, 20),
        karta3 = Karta(10000, 10, -50)
        ]
        draw_text(screen, f"Возмёшь карточку? {randint[kards(0, 3)]}", 10, 10)