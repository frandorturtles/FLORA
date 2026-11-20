# Revisión de diseño — FLORA v0.2

## Verificaciones automáticas realizadas
| Comprobación | Herramienta | Resultado |
|---|---|---|
| Netlist esquemático vs modelo | `check_netlist.py` (kicad-cli) | ✅ idéntico (55 componentes: 53 + 2 orificios) |
| ERC propio | `erc_light.py` | ✅ 0 errores, 0 avisos (no es el ERC oficial) |
| DRC PCB (archivo entregado) | KiCad 7.0.11, API pcbnew | ✅ 0 errores, 0 pads sin conectar; 1 aviso de serigrafía; avisos "librería no configurada" por ejecutar sin tabla de librerías |
| Contorno y cobre al borde (0,4 mm) | DRC | ✅ |
| Zona de antena (área de exclusión del módulo) | DRC | ✅ sin pistas/vías/relleno |
| Gerbers del mismo archivo | gerbonara + revisión visual | ✅ 9 capas, contorno 56,5 × 53,0 mm |
| Lógica del firmware | g++ en PC | ✅ |
| Sintaxis/tipos de `main.cpp` | g++ `-fsyntax-only -Wall -Wextra` con cabeceras simuladas | ✅ sin avisos |
| Pines contra hoja de datos | búsqueda de datasheets | ✅ ESP32-C3-WROOM-02, TSL25911FN, AP2112K (SOT-25), USBLC6-2SC6; TVS SMF5.0CA (bidireccional, SOD-123FL) |

## Correcciones respecto a la v0.2
- Añadido el PWR_FLAG de VBUS que faltaba en el esquemático (el ERC oficial lo habría marcado).
- TVS definido: **SMF5.0CA** (bidireccional, VRWM 5 V, VBR mín 6,4 V, VC 9,2 V, SOD-123FL), compatible con el símbolo bidireccional.
- Pistas de 3V3, VIN_PROT y SENS_VCC a **0,3 mm** (antes 0,2 mm).
- **Dos orificios de montaje M2** (2,2 mm), con ≥ 1,6 mm de material hasta el borde.
- Comprobación de sintaxis del firmware contra cabeceras simuladas.

## NO realizado
- **ERC oficial de KiCad** (la CLI de KiCad 7 no lo tiene).
- **DRC y ERC en KiCad 10** sobre estos archivos (verificados con KiCad 7.0.11).
- **Compilación real del firmware** para ESP32-C3 (el entorno bloquea el toolchain).
- **Contraste con hoja de datos** de SHT40, AO3401A, 2N7002, USB-C (GCT USB4105) y zumbador (Murata PKMCS0909E).
- **Verificación de stock y precios.**
- **Render 3D de la placa montada** (se entrega el STEP de la placa desnuda).
- **Fabricación y todas las pruebas físicas.**

## Limitaciones y riesgos conocidos
1. **Rutado generado por un router propio** (573 segmentos: 419 a 0,2 mm y 154 a 0,3 mm; 117 vías; 894 mm). Revisarlo visualmente.
2. **VBUS a 0,2 mm:** los pads del USB-C (paso fino) no admiten pistas más anchas con este router; el tramo es corto y la corriente máxima prevista es ≤ 500 mA (PTC), pero es el punto más justo de la placa. Mejora posible: ensanchar a mano en KiCad.
3. **Vía en el pad de GND de C6** (el router no encontró otra salida); mover C6 rompía otras conexiones.
4. **Orificios de montaje solo 2, no simétricos:** usa separadores/patas adicionales si necesitas estabilidad.
5. **OLED sobre el módulo ESP32** y a ~0,8 mm de la zona de antena: posible degradación de RF; v0.2 no usa Wi-Fi/BLE y no se midió nada.
6. **Orden de pines del OLED** variable según fabricante (la placa espera GND-VCC-SCL-SDA).
7. **Detección de sonda desconectada** heurística (pull-down 470 kΩ y rango de tensión).
8. **TSL25911FN:** el firmware usa registros y fórmula de lux del TSL2591: validar en hardware.
9. **Huella del TVS:** se usa `D_SOD-123F` de KiCad para un SOD-123FL; compatible en la envolvente de pads, pero confirma con el fabricante.
10. **LDO/PTC al límite** si se activa Wi-Fi.
11. **Reglas de fabricación supuestas** (0,2/0,2 mm, vía 0,6/0,3 mm, taladro mínimo 0,3 mm): confirmar con tu laboratorio.
12. **SHT40 en DFN:** requiere aire caliente/reflujo. Se eliminó del footprint un área de exclusión interna que ocupaba sus propios pads.
13. **Serigrafía decorativa** colocada automáticamente en zonas libres; revisar el Gerber de serigrafía.
14. Los colores de las imágenes **no** son capas de fabricación.
