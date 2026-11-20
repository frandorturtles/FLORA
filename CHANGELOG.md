# Changelog

## v0.2.1 — 2026-11-19
- Serigrafía: firma «frandorturtles» en las caras superior e inferior.
- Sitio web con modo ES/EN; README en inglés (`README.en.md`).

## v0.2 — 2026-11-19
- PWR_FLAG de VBUS añadido; TVS definido (SMF5.0CA); pistas de 3V3/VIN_PROT/SENS_VCC a 0,3 mm; 2 orificios de montaje M2.
- Esquemático y PCB regenerados y verificados juntos (DRC sin errores en KiCad 7.0.11); Gerbers, taladros, BOM, renders y STEP regenerados.
- Serigrafía: «frandorturtles» en la cara superior (bajo el logotipo) y en la inferior; Gerbers e imágenes regenerados (DRC sin errores nuevos).
- Comprobación de sintaxis del firmware contra cabeceras simuladas; datasheets contrastadas (AP2112K, USBLC6, SMF5.0CA).

## v0.1.1 — 2026-11-18
- Rutado guardado en KiCad 10 (zonas GND rellenas).
- Añadido el PWR_FLAG de VBUS que faltaba en el esquemático.
- Sitio web publicado en `docs/` para GitHub Pages.
- Sin repetir DRC en KiCad 10; Gerbers por re-trazar desde KiCad 10.

## v0.1 — 2026-10-26
- Primer diseño completo: esquemático, PCB en forma de flor, firmware, Gerbers, documentación.
- Sin fabricar ni probar. Ver `documentation/design_review.md` para pendientes.
