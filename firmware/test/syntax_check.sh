#!/bin/sh
# Comprobación de sintaxis y tipos de src/main.cpp contra cabeceras SIMULADAS de Arduino/Wire/Preferences/U8g2.
# NO es la compilación real para ESP32-C3 (eso requiere PlatformIO); detecta errores de C++ y de tipos.
cd "$(dirname "$0")/.." && g++ -std=gnu++17 -fsyntax-only -Wall -Wextra -Itest/arduino_stubs -Ilib/flora_logic src/main.cpp && echo "sintaxis OK (contra stubs)"
