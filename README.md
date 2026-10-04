# VEGA Aries V3 TinyML Gesture Recognition

TinyML-based hand gesture recognition on the VEGA Aries V3 RISC-V board using a lightweight neural network.

## Overview

This project demonstrates on-device TinyML inference on the VEGA Aries V3. A laptop webcam captures a hand, 21 hand landmarks are converted into 42 X/Y features, and the feature vector is sent to VEGA over USB serial.

**Pipeline:** Laptop webcam → hand landmarks → 42 features → Serial → VEGA Aries V3 → TinyML inference → gesture prediction.

## Model

- Input: 42 features
- Hidden layer 1: 16 neurons
- Hidden layer 2: 8 neurons
- Output: 3 classes
- Hidden activation: ReLU
- Output activation: Softmax

### Gesture classes

| Class | Gesture |
|---|---|
| 0 | REST |
| 1 | TWO |
| 2 | THREE |

## Hardware

- VEGA Aries V3 RISC-V development board
- Laptop/USB webcam
- USB connection for serial communication
- Optional HW-125 MicroSD module for the separate image-transfer experiment

## Software

- Arduino IDE
- VEGA RISC-V Arduino core
- Python
- OpenCV
- MediaPipe Hands
- TensorFlow/TensorFlow Lite for model development

## Serial interface

- Baud rate: **115200**
- Feature vector: **42 values**
- Packet: comma-separated values followed by a newline

## Repository structure

```
VEGA-Aries-V3-TinyML-Gesture-Recognition/
├── README.md
├── firmware/
│   └── VEGA_TinyML_Gesture.ino
├── model/
│   ├── README.md
│   └── gesture_model.h        # add final trained weights here
├── python/
│   └── webcam_gesture_capture.py
├── docs/
│   └── pinout.md
└── LICENSE
```

## Development status

- VEGA Aries V3 TinyML firmware: developed
- 42-feature serial transfer: tested
- Laptop webcam feature pipeline: tested
- 42 → 16 → 8 → 3 neural-network architecture: established
- REST / TWO / THREE classes: established
- HW-125 image transfer to VEGA SD: tested separately

## Future work

- Finalize and deploy the trained `gesture_model.h`
- Improve feature normalization
- Add confidence reporting
- Optimize inference speed and memory usage
- Add more gesture classes

## Author

**Drishant Das**

## License

MIT
