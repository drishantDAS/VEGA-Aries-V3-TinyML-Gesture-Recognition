# Gesture Model

The intended deployed classifier is:

- 42 input features
- 16-neuron hidden layer
- 8-neuron hidden layer
- 3-neuron output layer
- ReLU hidden activation
- Softmax output

Classes:

0. REST
1. TWO
2. THREE

The final trained `gesture_model.h` should contain the trained weights, biases, and any required normalization parameters.

Keep the trained header separate from the firmware so the model can be updated without changing the serial transport code.
