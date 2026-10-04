#include <Arduino.h>

static const int NUM_FEATURES = 42;
static const int NUM_CLASSES = 3;

float features[NUM_FEATURES];

const char* className(int cls) {
  switch (cls) {
    case 0: return "REST";
    case 1: return "TWO";
    case 2: return "THREE";
    default: return "UNKNOWN";
  }
}

bool readFeatures() {
  static char buffer[2000];
  size_t n = 0;
  unsigned long start = millis();

  while (millis() - start < 3000) {
    while (Serial.available()) {
      char c = Serial.read();

      if (c == '\n' || c == '\r') {
        if (n == 0) continue;

        buffer[n] = '\0';
        int count = 0;
        char* token = strtok(buffer, ",");

        while (token != nullptr && count < NUM_FEATURES) {
          features[count++] = atof(token);
          token = strtok(nullptr, ",");
        }

        return count == NUM_FEATURES;
      }

      if (n < sizeof(buffer) - 1) buffer[n++] = c;
    }
  }
  return false;
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  Serial.println("FLASHER");
  Serial.println("VEGA TINYML READY");
  Serial.println("WAITING FOR 42 FEATURES");
}

void loop() {
  if (!readFeatures()) return;

  Serial.println("FEATURES RECEIVED: 42");

  // Include gesture_model.h here when the final trained weights are deployed.
  // The serial interface is kept independent from the trained model.

  Serial.println("RESULT");
  Serial.println("MODEL_HEADER_REQUIRED");
  Serial.println("PREDICTED: -1");
  Serial.println("WAITING FOR 42 FEATURES");
}
