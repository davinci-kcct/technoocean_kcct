#include <Servo.h>

Servo sv1;

int base = 200, adjust = 0;

void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  // myservo.attach(4);
}

void loop() {
  char input = NULL;
  if (Serial.available() > 0) {
    input = Serial.read();
  }
  switch (input) {
    case 'k':
      digitalWrite(2, LOW);
      digitalWrite(12, LOW);
      analogWrite(3, base + adjust);
      analogWrite(11, base);
      break;
    case 'i':
      digitalWrite(2, HIGH);
      digitalWrite(12, HIGH);
      analogWrite(3, base + adjust);
      analogWrite(11, base);
      break;
    case 'j':
      digitalWrite(2, HIGH);
      digitalWrite(12, LOW);
      analogWrite(3, base + adjust);
      analogWrite(11, base);
      break;
    case 'l':
      digitalWrite(2, LOW);
      digitalWrite(12, HIGH);
      analogWrite(3, base + adjust);
      analogWrite(11, base);
      break;
    default:
      analogWrite(3, 0);
      analogWrite(11, 0);
      break;
  }
  switch (input) {
    case 'a':
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);
      analogWrite(6, base + adjust);
      analogWrite(5, base);
      break;
    case 'z':
      digitalWrite(7, LOW);
      digitalWrite(8, LOW);
      analogWrite(6, base + adjust);
      analogWrite(5, base);
      break;
    case 'o':
      sv1.write(130);
      break;
    case 'c':
      sv1.write(30);
      break;
    default:
      analogWrite(6, 0);
      analogWrite(5, 0);
      break;
  }
  switch (input) {
    case '1':
      adjust++;
      break;
    case '2':
      adjust--;
      break;
    case ' ':
      adjust = 0;
      break;
    case 'o':
      break;
    case 'c':
      break;
  }

  delay(100);
}
