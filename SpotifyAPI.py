import spotipy
from spotipy.oauth2 import SpotifyOAuth
import serial
import time

# === CONFIGURATION ===
SERIAL_PORT = 'COM3'  # <- ton port Arduino
CLIENT_ID = 'eaa32e1736c9409f8b1b9bd9cd92150d'
CLIENT_SECRET = '661b4fb0c7c94dfb903b8621baf77528'
REDIRECT_URI = 'http://127.0.0.1:8888/callback'  # doit être ajouté dans le dashboard Spotify

# === Connexion série avec Arduino ===
try:
    arduino = serial.Serial(SERIAL_PORT, 9600, timeout=1)
    time.sleep(2)
except:
    print("❌ Impossible de se connecter à l'Arduino sur", SERIAL_PORT)
    exit()

# === Authentification Spotify ===
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope='user-read-playback-state'
))

# === Boucle principale ===
dernier = ""

while True:
    try:
        lecture = sp.current_playback()
        if lecture and lecture['is_playing']:
            titre = lecture['item']['name']
            artiste = lecture['item']['artists'][0]['name']
           # Durée en minutes:secondes
            duree_ms = lecture['item']['duration_ms']
            duree_s = int(duree_ms / 1000)
            minutes = duree_s // 60
            secondes = duree_s % 60
            temps = f"{minutes}:{secondes:02d}"

            # Chaîne complète avec séparateur |
            ligne = f"{titre} - {artiste}|{temps}"
            if ligne != dernier:
                print("🎵 Envoi :", ligne)
                arduino.write((ligne[:32] + '\n').encode())  # LCD 16x2 = max 32 caractères
                dernier = ligne
        else:
            if dernier != "Pause":
                arduino.write("Pause\n".encode())
                print("⏸️ Pause")
                dernier = "Pause"
    except Exception as e:
        print("⚠️ Erreur :", e)
    time.sleep(5)
