# Informe de ERC propio — FLORA v0.2

**Esto NO es el ERC oficial de KiCad.** La CLI de KiCad 7.0.11 no incluye `sch erc`. Se escribió `hardware/scripts/erc_light.py`, que analiza el netlist exportado del esquemático.

## Qué comprueba
- Referencias únicas; valor y huella presentes en todos los componentes.
- Cada pin del símbolo tiene pad en la huella (y viceversa).
- Redes con un solo pin; pines sin conectar con marca NC.
- Entradas de alimentación sin fuente (`power_out`) ni PWR_FLAG; varias salidas en una misma red.
- Entradas sin ningún pin que las maneje; GPIO del U1 repetidos; existencia de las redes de alimentación.

## Resultado (tras añadir un PWR_FLAG que faltaba en VBUS)
- **0 errores, 0 avisos.**
- 3 PWR_FLAG (VIN_PROT, GND, VBUS).
- Pines sin conectar, todos con marca de "no conectar": J1.A8 y J1.B8 (SBU), U3.2 (INT), U3.4 (NC), U4.4 (NC).

## Hallazgo corregido
Los símbolos de alimentación (power:VBUS) tienen un pin de entrada de alimentación; sin un PWR_FLAG en VBUS el ERC oficial habría marcado "pin de alimentación no conectado a ninguna fuente". Se añadió el PWR_FLAG.

## Resultado final (v0.2)
Tras regenerar el esquemático (con PWR_FLAG en VBUS, TVS SMF5.0CA y 2 orificios de montaje): **0 errores, 0 avisos**, 3 PWR_FLAG. El esquemático se regeneró en formato KiCad 7 para que coincida exactamente con la placa; ábrelo en KiCad 10 y ejecuta el ERC oficial.

## Qué NO cubre
Matriz completa de tipos de pin de KiCad, etiquetas globales/jerárquicas, hilos sin terminar, texto fuera de la hoja, simbología duplicada y otras reglas del ERC oficial. **Ejecuta el ERC oficial en KiCad (Inspeccionar → Comprobar reglas eléctricas)** y corrige lo que muestre.
