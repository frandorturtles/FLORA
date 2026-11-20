# FLORA — Smart Plant Companion 🌸

🇬🇧 **[Read this in English → README.en.md](README.en.md)**

**Autora:** Francesca Martínez · [@frandorturtles](https://github.com/frandorturtles) · **Web:** https://frandorturtles.github.io/FLORA/ (tras activar GitHub Pages, ver abajo)

Monitor de plantas con **ESP32-C3** en una **PCB con forma de flor** (5 pétalos, 56,5 × 53 mm, 2 capas, 2 orificios de montaje M2, firma «frandorturtles» en la serigrafía).
Mide humedad del suelo (sonda capacitiva), temperatura y humedad del aire (SHT40) y luz (TSL25911), y lo muestra en una pantalla OLED con LEDs de estado y alerta sonora opcional. Alimentación por USB-C (5 V).

![FLORA - cara superior](renders/top_view.png)

> **Estado honesto (v0.2): diseño completo y verificado con herramientas automáticas, pero SIN fabricar y SIN probar en hardware.**
> Los colores de las imágenes son de presentación; el color real de la máscara depende del fabricante.

## Qué hay en este repositorio
| Carpeta | Contenido |
|---|---|
| `hardware/` | Proyecto KiCad (`FLORA.kicad_pro/.kicad_sch/.kicad_pcb`), símbolo propio, BOM, pinout, Gerbers, taladros, posiciones, scripts generadores |
| `firmware/` | Firmware ESP32-C3 (Arduino/PlatformIO), lógica probada en PC y comprobación de sintaxis |
| `documentation/` | Arquitectura, diseño eléctrico, montaje, plan de pruebas, BOM, ERC, revisión de diseño |
| `manufacturing/` | Notas de fabricación, ensamblaje, checklist y el ZIP de Gerbers |
| `renders/` | Vistas superior/inferior (desde los Gerbers), vista de fabricación y modelo STEP de la placa |
| `website/` y `docs/` | Sitio web morado de FLORA (`docs/index.html` lo sirve GitHub Pages) |
| `portfolio/` | Página de caso de estudio (ES/EN) y textos para el portafolio |

## Funciones (v0.2)
Humedad de suelo calibrable (seco/húmedo) · temperatura y HR ambiente · luz · OLED 0,96" · 3 LEDs (seco / OK / exceso) · zumbador desactivable · botón de usuario + reset · umbrales configurables · aviso de sonda desconectada · 10 puntos de prueba · USB-C 5 V (sin PD) · 2 orificios M2 · **sin riego automático, sin batería**.

## Verificaciones
| Comprobación | Estado |
|---|---|
| Netlist del esquemático = modelo de diseño | ✅ automática (`check_netlist.py`) |
| ERC propio sobre el netlist (tipos de pin, alimentaciones, pines vs huellas) | ✅ 0 errores, 0 avisos — **no sustituye al ERC oficial** (`documentation/erc_report.md`) |
| ERC oficial de KiCad | ❌ no ejecutado (la CLI de KiCad 7 no lo incluye): hazlo en KiCad (Inspeccionar → Comprobar reglas eléctricas) o con el CI |
| DRC de la PCB (KiCad 7.0.11, **sobre el mismo archivo entregado**) | ✅ 0 errores, 0 pads sin conectar. Quedan avisos "librería no configurada" (ejecución sin tabla de librerías) y 1 aviso de serigrafía |
| Gerbers del mismo archivo, leídos con un visor independiente (gerbonara) y revisados visualmente | ✅ |
| Lógica del firmware (pruebas en PC, g++) | ✅ |
| Firmware: sintaxis y tipos contra cabeceras simuladas de Arduino | ✅ (`firmware/test/syntax_check.sh`) |
| Firmware: compilación real para ESP32-C3 | ❌ no se pudo (mi entorno bloquea la descarga del toolchain): ejecuta `pio run` o el CI |
| Pines contrastados con hoja de datos | ✅ ESP32-C3-WROOM-02, TSL25911FN, AP2112K, USBLC6-2SC6, SMF5.0CA · ⚠️ SHT40, AO3401A, 2N7002, USB-C, zumbador: solo símbolos oficiales de KiCad |
| Fabricación, ensamblaje, pruebas físicas | ❌ pendientes (`documentation/testing_plan.md`) |

Lista completa de limitaciones: `documentation/design_review.md`.

## Publicar en tu GitHub (@frandorturtles)
```
cd FLORA
git init -b main
git add .
git commit -m "FLORA v0.2: hardware, firmware, documentación y web"
git remote add origin https://github.com/frandorturtles/FLORA.git   # crea antes el repo vacío "FLORA" en github.com/new
git push -u origin main
```
Luego, en GitHub: **Settings → Pages → Deploy from a branch → `main` / carpeta `/docs`**. En **About** pon descripción y topics: `esp32-c3`, `kicad`, `pcb`, `plant-monitor`, `platformio`, `open-hardware`.

## Cómo empezar
1. **Abrir:** `hardware/FLORA.kicad_pro` en KiCad 10 (los archivos están en formato KiCad 7; KiCad 10 los actualiza al guardar). Ejecuta ERC y DRC.
2. **Fabricar:** `manufacturing/fabrication_notes.md` y `manufacturing/FLORA_gerbers_for_fab.zip` (vuelve a trazar desde KiCad 10 si prefieres, ver `gerber_checklist.md`).
3. **Comprar:** `hardware/bom.csv` (verifica stock y números de parte).
4. **Montar:** `documentation/assembly_guide.md`.
5. **Firmware:** `firmware/README.md`.
6. **Probar:** `documentation/testing_plan.md`.

## Regenerar el hardware desde cero
Ver `hardware/scripts/README.md`.

## Licencia
MIT (ver `LICENSE`). Puedes cambiar la licencia del hardware (por ejemplo CERN-OHL-P o CC BY 4.0).
