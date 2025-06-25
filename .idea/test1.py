from picoboy import PicoBoy
import time

pb = PicoBoy()

# Den Teil oberhalb dieser Zeile bitte nicht ändern!

# PicoBoy Displaygröße
display_width = 128
display_height = 64

# Anzahl der Reihen und Spalten
num_rows = 4 # 1-2-3, 4-5-6, 7-8-9, *-0-#
num_cols = 3

# Abstandsberechnung für gleichmäßige Verteilung
horizontal_spacing = 2 # Kleiner Abstand zwischen den Tasten
vertical_spacing = 2

# Berechne die Tastenbreite und -höhe
button_width = (display_width - (num_cols + 1) * horizontal_spacing) // num_cols
button_height = (display_height - (num_rows + 1) * vertical_spacing) // num_rows

# Startposition für das Gitter (nach dem ersten Abstand)
start_x = horizontal_spacing
start_y = vertical_spacing

# Definition der Tastenwerte in einem 2D-Array für einfache Navigation
keypad_values = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["*", "0", "#"]
]

# Aktuelle Auswahlposition (Reihe, Spalte)
selected_row = 0
selected_col = 0

# Liste zum Speichern der ausgewählten Nummern
entered_numbers = []

def draw_keypad(selected_row, selected_col):
    """Zeichnet das gesamte Nummernfeld und hebt die ausgewählte Taste hervor."""
    pb.fill(0) # Display schwarz füllen

    for r in range(num_rows):
        for c in range(num_cols):
            x = start_x + c * (button_width + horizontal_spacing)
            y = start_y + r * (button_height + vertical_spacing)
            value = keypad_values[r][c]

            # Wenn diese Taste ausgewählt ist, fülle sie (oder zeichne einen gefüllten Rahmen)
            if r == selected_row and c == selected_col:
                pb.fill_rect(x, y, button_width, button_height, 1) # Weiße, gefüllte Taste
                # Textfarbe Schwarz für die ausgewählte Taste
                pb.text(value, x + (button_width // 2) - (len(value) * 4), y + (button_height // 2) - 4, 0)
            else:
                pb.rect(x, y, button_width, button_height, 1) # Nur den Rahmen zeichnen
                # Textfarbe Weiß für die nicht ausgewählten Tasten
                pb.text(value, x + (button_width // 2) - (len(value) * 4), y + (button_height // 2) - 4, 1)

    # Zeige die bisher eingegebenen Zahlen an (z.B. am unteren Rand)
    entered_text = "".join(entered_numbers)
    # Begrenze die angezeigte Länge, falls zu viele Nummern eingegeben werden
    display_entered_text = "Eingabe: " + entered_text[-10:] # Zeigt nur die letzten 10 Zeichen
    pb.text(display_entered_text, 0, display_height - 8, 1) # Unterster Rand

    pb.show() # Alles auf dem Display anzeigen


# Initiales Zeichnen des Nummernfeldes
draw_keypad(selected_row, selected_col)

# Hauptschleife für die Interaktion
while True:
    # Überprüfe jede Joystick-Richtung separat
    # WICHTIG: Verwenden der spezifischen pb.pressedX() Methoden

    moved = False # Flag, um zu prüfen, ob sich etwas bewegt hat

    if pb.pressedUp(): # HIER GEÄNDERT
        selected_row = max(0, selected_row - 1)
        moved = True
    elif pb.pressedDown(): # HIER GEÄNDERT
        selected_row = min(num_rows - 1, selected_row + 1)
        moved = True
    elif pb.pressedLeft(): # HIER GEÄNDERT
        selected_col = max(0, selected_col - 1)
        moved = True
    elif pb.pressedRight(): # HIER GEÄNDERT
        selected_col = min(num_cols - 1, selected_col + 1)
        moved = True

    if moved:
        draw_keypad(selected_row, selected_col)
        # Warte, bis der Joystick losgelassen wird ODER eine Mindestzeit vergeht
        time.sleep(0.15) # Kurze Pause, um die Bewegung zu sehen und Prellen zu reduzieren
        # Warte auf Freigabe der Taste(n)
        while pb.pressedUp() or pb.pressedDown() or \
                pb.pressedLeft() or pb.pressedRight():
            time.sleep(0.01) # Kleine Verzögerung während des Wartens

    # Joystick-Klick (Bestätigung)
    if pb.pressedCenter(): # HIER GEÄNDERT
        selected_value = keypad_values[selected_row][selected_col]
        entered_numbers.append(selected_value) # Wert zur Liste hinzufügen
        draw_keypad(selected_row, selected_col) # Nummernfeld neu zeichnen (mit aktualisierter Eingabezeile)

        print("Nummer ausgewählt:", selected_value) # Optional: Ausgabe auf der Konsole (wenn PicoBoy mit PC verbunden)

        # Warte, bis der CENTER-Button losgelassen wird
        time.sleep(0.2) # Eine kurze Pause nach dem Klick
        while pb.pressedCenter():
            time.sleep(0.01) # Warten, bis der Button freigegeben wird


    time.sleep(0.02) # Kurze globale Pause, um die CPU nicht zu überlasten
