#include <Keyboard.h>


int base = 200, adjust = 0;

void setup() {
  Keyboard.begin();
  Serial.begin(9600);
  
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
}

void loop() {
  char input = NULL;
  if (Serial.available() > 0) {
    input = Serial.read();
  }
  switch (input) {
    case 'w':
      digitalWrite(7, HIGH);
      analogWrite(5, base);
      digitalWrite(12, LOW);
      analogWrite(11, base);
      break;
    case 's':
      digitalWrite(7, LOW);
      analogWrite(5, base);
      digitalWrite(12, HIGH);
      analogWrite(11, base);
      break;
    case 'a':
      digitalWrite(7, LOW);
      analogWrite(5, base);
      digitalWrite(12, LOW);
      analogWrite(11, base);
      break;
    case 'd':
      digitalWrite(7, HIGH);
      analogWrite(5, base);
      digitalWrite(12, HIGH);
      analogWrite(11, base);
      break;
    default:
      analogWrite(5, 0);
      analogWrite(11, 0);
      break;
  }
  switch (input) {
    case 'q':
      digitalWrite(2, LOW);
      analogWrite(3, base);
      digitalWrite(8, HIGH);
      analogWrite(6, base);
      break;
    case 'e':
      digitalWrite(2, HIGH);
      analogWrite(3, base);
      digitalWrite(8, LOW);
      analogWrite(6, base);
      break;
    default:
      analogWrite(3, 0);
      analogWrite(6, 0);
      break;
  }

  delay(100);
}
