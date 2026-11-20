#pragma once
#include <stdint.h>
#define U8G2_R0 0
#define U8X8_PIN_NONE 255
extern const uint8_t u8g2_font_6x12_tf[];
struct U8G2_SSD1306_128X64_NONAME_F_HW_I2C { U8G2_SSD1306_128X64_NONAME_F_HW_I2C(int,int=255,int=255,int=255); bool begin(); void setI2CAddress(uint8_t); void setContrast(uint8_t); void clearBuffer(); void setFont(const uint8_t*); int drawStr(int,int,const char*); void sendBuffer(); };
