#pragma once
#include <stdint.h>
struct TwoWire { bool begin(int,int,uint32_t=100000); void setTimeOut(uint16_t); void beginTransmission(uint8_t); uint8_t endTransmission(bool=true); size_t write(uint8_t); uint8_t requestFrom(int,int); int read(); };
extern TwoWire Wire;
