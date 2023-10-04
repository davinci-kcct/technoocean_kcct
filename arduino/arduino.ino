#include <SoftwareSerial.h>
#include <ps3btlib.h>

int base = 200, adjust = 0;

void setup() {
  Serial.begin(9600);
  bt_set();
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
  
  if (P_SANKAKU){
      digitalWrite(2, LOW);
      analogWrite(3, base);
      digitalWrite(12, HIGH);
      analogWrite(11, base);
  }
  if (P_MARU){
      digitalWrite(2, HIGH);
      analogWrite(3, base);
      digitalWrite(12, HIGH);
      analogWrite(11, base);
  }
  if (P_BATU){
      digitalWrite(2, HIGH);
      analogWrite(3, base);
      digitalWrite(12, LOW);
      analogWrite(11, base);
  }
  if (P_SIKAKU){
      digitalWrite(2, LOW);
      analogWrite(3, base);
      digitalWrite(12, LOW);
      analogWrite(11, base);
  }
  if (P_MIGI){
      analogWrite(5, 0);
      analogWrite(11, 0);
      analogWrite(3, 0);
      analogWrite(6, 0);
  }
  if (P_UE){
      digitalWrite(7, HIGH);
      analogWrite(5, base);
      digitalWrite(8, HIGH);
      analogWrite(6, base);
  }
  if (P_SITA){
      digitalWrite(7, LOW);
      analogWrite(5, base);
      digitalWrite(8, LOW);
      analogWrite(6, base);
  }

  delay(100);
}
