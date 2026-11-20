#pragma once
#include "Arduino.h"
struct Preferences { bool begin(const char*,bool=false); void end(); float getFloat(const char*,float=0); bool getBool(const char*,bool=false); size_t putFloat(const char*,float); size_t putBool(const char*,bool); };
