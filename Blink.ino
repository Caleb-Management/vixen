int Green_LED = 9;
//defining pin number for LED

void setup(){
  pinMode(Green_LED,OUTPUT);
  //determining that LED is considered an output
  
}

void loop(){
  digitalWrite(9, HIGH);
  //LED is turned on
  delay(250);
  digitalWrite(9, LOW);
  //LED is turned off
  delay(250);
}
