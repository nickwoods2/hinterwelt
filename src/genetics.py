# genetics.py


class Gene:
    def __init__(self, input_neuron, output_neuron, weight):
        self.input_neuron = input_neuron
        self.output_neuron = output_neuron
        self.weight = weight


class Genes:
    def __init__(self, input_neurons, intermediary_neurons, output_neurons, genes):
        self.input_neurons = input_neurons
        self.intermediary_neurons = intermediary_neurons
        self.output_neurons = output_neurons
        self.genes = genes


class Neuron:
    def __init__(self):
        self.value = 0.0
        self.synapses = []


class Synapse:
    def __init__(self, input_neuron, output_neuron, weight):
        self.input_neuron = input_neuron
        self.output_neuron = output_neuron
        self.weight = weight
