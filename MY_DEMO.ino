const int dataFrame = 22;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() >= dataFrame){
    for (int i = 0; i < dataFrame; i++){
      Serial.print(Serial.read(), HEX);
      Serial.print(",");
    }
    Serial.println();
  }
}
