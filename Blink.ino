int G_LED = 9;
//defining pin number for green LED

int B_LED = 6;
//defining pin number for blue LED

void setup(){
  pinMode(G_LED,OUTPUT);
  pinMode(B_LED, OUTPUT);
  //determining that both LEDs are considered as outputs
  
  
}

void loop(){
  digitalWrite(G_LED, HIGH);
  digitalWrite(B_LED, LOW);
  //Green LED turned on, blue LED turned off
  delay(500);
  digitalWrite(G_LED, LOW);
  digitalWrite(B_LED, HIGH);
  //Green LED turned off, blue LED turned on
  delay(500);
}
