# VEGA Aries V3 Project Notes

## Serial

| Parameter | Value |
|---|---|
| Board | VEGA Aries V3 |
| Interface | USB Serial |
| Baud rate | 115200 |
| Feature count | 42 |

## TinyML data path

Laptop webcam → MediaPipe hand landmarks → 21 landmarks → X/Y coordinates → 42 features → Serial → VEGA Aries V3

## HW-125 image-transfer experiment

The separate SD experiment used:

- MOSI → MOSI-0
- MISO → MISO-1
- SCK → SCLK-1
- CS → GPIO-10
- VCC → 5V
- GND → GND

The SD image-transfer experiment is separate from the TinyML inference pipeline.
