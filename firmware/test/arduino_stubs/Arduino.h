#pragma once
#include <stdint.h>
#include <stdio.h>
#include <string>
#include <math.h>
#define ESP_ARDUINO_VERSION_MAJOR 3
#define HIGH 1
#define LOW 0
#define OUTPUT 1
#define INPUT 0
#define ADC_11db 3
class String { std::string s; public: String(){} String(const char*c):s(c){} String(int v):s(std::to_string(v)){} const char* c_str() const {return s.c_str();}
  String operator+(const String&o) const {String r; r.s=s+o.s; return r;} friend String operator+(const char*a,const String&b){String r(a); return r+b;} String operator+(const char*b) const {String r; r.s=s+b; return r;} };
struct SerialT { void begin(int){} template<class...A> void printf(const char*,A...){} } ;
extern SerialT Serial;
void pinMode(int,int); void digitalWrite(int,int); int digitalRead(int); uint32_t millis(); void delay(uint32_t);
uint32_t analogReadMilliVolts(int); void analogSetPinAttenuation(int,int);
bool ledcAttach(int,uint32_t,uint8_t); uint32_t ledcWriteTone(int,uint32_t);
void setup(); void loop();
