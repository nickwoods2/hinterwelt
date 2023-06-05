# Add to genetics.py file

import tensorflow as tf
import numpy as np


class Brain:
    def __init__(self, genome):
        self.genome = genome
        self.model = tf.keras.models.Sequential(
            [
                tf.keras.layers.Dense(10, activation="relu"),  # hidden layer 1
                tf.keras.layers.Dense(10, activation="relu"),  # hidden layer 2
                tf.keras.layers.Dense(4, activation="softmax"),  # output layer
            ]
        )

        # Explicitly build the model
        self.model.build((None, 8))  # input_shape: batch_size x number_of_input_neurons

        # Convert the genome to weights and biases
        weights, biases = self.genome_to_weights_and_biases()

        # Set the weights and biases
        self.model.set_weights(
            [weights[0], biases[0], weights[1], biases[1], weights[2], biases[2]]
        )

    def genome_to_weights_and_biases(self):
        # Convert genome into a list of weights and biases
        weights = []
        biases = []

        # Weights and biases for first layer
        weights.append(np.array(self.genome[:80]).reshape((8, 10)))
        biases.append(np.array(self.genome[80:90]))

        # Weights and biases for second layer
        weights.append(np.array(self.genome[90:190]).reshape((10, 10)))
        biases.append(np.array(self.genome[190:200]))

        # Weights and biases for output layer
        weights.append(np.array(self.genome[200:240]).reshape((10, 4)))
        biases.append(np.array(self.genome[240:]))

        return weights, biases

    def decide(self, inputs):
        inputs = np.array(inputs)[np.newaxis, ...]  # add batch dimension
        outputs = self.model.predict(inputs)[0]  # remove batch dimension
        return np.argmax(outputs)
