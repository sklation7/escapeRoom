# Escape Room – Informatikprojekt der 11d

Willkommen zum Escape Room Spiel der Klasse 11d am Maria-Theresia-Gymnasium!

## Projektbeschreibung

Im Rahmen des Informatikunterrichts haben wir ein digitales Escape Room Spiel entwickelt. Ziel ist es, verschiedene Rätsel zu lösen, Hinweise zu kombinieren und so Schritt für Schritt den Ausgang zu finden.

## Features

- Spannende Rätsel und Aufgaben
- Logisches Denken und Teamarbeit gefragt
- Spielerische Einführung in Programmierung und Problemlösung

## Mitwirkende

Klasse 11d, Maria-Theresia-Gymnasium  
Fach: Informatik

---

## Einrichtung und Kompilierung (Setup and Compilation)

Um dieses Projekt zu kompilieren und auf einem Picoboy auszuführen, befolge diese Schritte:

1.  **Pico SDK einrichten:**
    Stelle sicher, dass du das Raspberry Pi Pico C/C++ SDK installiert hast und die Umgebungsvariable `PICO_SDK_PATH` korrekt auf das SDK-Verzeichnis zeigt. Anleitungen findest du hier: [Getting started with Raspberry Pi Pico](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf) (Kapitel für C/C++ SDK).

2.  **Repository klonen:**
    ```bash
    git clone https://github.com/your-username/escape_room_pico.git
    cd escape_room_pico
    ```
    (Ersetze `https://github.com/your-username/escape_room_pico.git` mit der tatsächlichen URL des Repositories)

3.  **Projekt bauen:**
    ```bash
    mkdir build
    cd build
    cmake ..
    make -j$(nproc)  # Kompiliert mit allen verfügbaren Prozessorkernen
    ```

4.  **Auf Picoboy laden:**
    Nach erfolgreichem Kompilieren findest du eine `.uf2`-Datei im `build`-Verzeichnis (z.B. `build/escape_room_pico.uf2`). Du kannst diese Datei auf deinen Picoboy laden, indem du ihn im BOOTSEL-Modus startest (BOOTSEL-Knopf gedrückt halten und dann mit USB verbinden) und die `.uf2`-Datei dorthin kopierst.

---

Viel Spaß beim Knobeln und Entkommen!
