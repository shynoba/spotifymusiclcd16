#include <LiquidCrystal.h>

LiquidCrystal lcd(13, 12, 10, 9, 8, 7);     //You must put the value of the data plug in the Arduino UNO"

String ligne = "";
String titreScroll = "";
String temps = "";

unsigned long previousMillis = 0;
int scrollIndex = 0;

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.clear();
}

void loop() {
  if (Serial.available()) {
    ligne = Serial.readStringUntil('\n');

    int sep = ligne.indexOf('|');
    if (sep != -1) {
      titreScroll = ligne.substring(0, sep);
      temps = ligne.substring(sep + 1);
    } else {
      titreScroll = ligne;
      temps = "";
    }
    scrollIndex = 0;
  }

  if (millis() - previousMillis > 300) {
    previousMillis = millis();
    lcd.clear();

    // Line 1 : Scroll
    if (titreScroll.length() <= 16) {
      lcd.setCursor(0, 0);
      lcd.print(titreScroll);
    } else {
      lcd.setCursor(0, 0);
      lcd.print(titreScroll.substring(scrollIndex, scrollIndex + 16));
      scrollIndex++;
      if (scrollIndex + 16 > titreScroll.length()) {
        scrollIndex = 0;
      }
    }

    // Line 2 : Timer
    lcd.setCursor(0, 1);
    lcd.print("Duree: ");
    lcd.print(temps);
  }
}
