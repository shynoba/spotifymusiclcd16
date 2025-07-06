# 🎵 Spotify Music Display on LCD1602 (Arduino UNO)

Affiche en temps réel le **titre de la musique en cours sur Spotify** sur un écran **LCD1602** connecté à un **Arduino UNO**. Le script Python utilise l’API Spotify pour extraire les infos et les transmet via **port série USB**.

---

## 📷 Aperçu

![schemaarduinospotify](https://github.com/user-attachments/assets/bcc0139b-5323-429a-8d9c-05beb40d40eb)


---

## 🧰 Matériel nécessaire

| Matériel               | Description                          |
|------------------------|--------------------------------------|
| Arduino UNO            | Carte microcontrôleur principale     |
| Écran LCD 1602         | Affichage 16 colonnes × 2 lignes     |
| Module I2C (optionnel) | Pour simplifier les connexions LCD  |
| Câbles                 | Pour relier l'écran à l'Arduino      |
| Ordinateur             | Avec Python + API Spotify            |

---

## 🔌 Schéma de branchement LCD1602 (sans I2C)

| LCD Pin | Arduino UNO Pin |
|---------|------------------|
| RS      | 13               |
| E       | 12               |
| D4      | 10               |
| D5      | 9                |
| D6      | 8                |
| D7      | 7                |

> 💡 Pense à connecter VSS à GND, VDD à 5V, RW à GND. Un potentiomètre est recommandé pour régler le contraste du LCD.

---

## 💻 Fonctionnement

1. Le **script Python** se connecte à Spotify via l’API (`spotipy`) et récupère les infos de lecture.
2. Il envoie le **titre**, **artiste** et **durée** via le port série.
3. L'**Arduino** lit la chaîne et affiche le tout sur le **LCD1602**, avec un **défilement automatique** si le texte est long.

---

## 📂 Fichiers

| Fichier                      | Description                                 |
|-----------------------------|---------------------------------------------|
| `arduino_lcd_scroll.ino`       | Code Arduino : lecture série + affichage LCD |
| `spotifyAPI.py`         | Script Python : API Spotify + port série     |
| `images/schema.jpeg`        | Capture du projet                            |

---

