import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

user_input = input("Enter two binary inputs for XOR (e.g., '1 0'): ")
x1, x2 = map(int, user_input.split())
X = np.array([[x1, x2]])
y = np.array([[x1 ^ x2]])  # XOR output: 1 if inputs differ, 0 otherwise

wh = np.array([[0.4, 0.2],
               [0.3, 0.7]])
bh = np.array([[0.1, 0.1]])

wo = np.array([[0.6],
               [0.9]])
bo = np.array([[0.05]])

hidden_input = np.dot(X, wh) + bh
hidden_output = sigmoid(hidden_input)

output_input = np.dot(hidden_output, wo) + bo
predicted_output = sigmoid(output_input)

print("🔄 Forward Propagation Results:")
print("Hidden layer input:", hidden_input)
print("Hidden layer output:", hidden_output)
print("Output layer input:", output_input)
print("Predicted output:", predicted_output)

error = y - predicted_output
print("\n❌ Error:", error)

d_output = error * sigmoid_derivative(predicted_output)

error_hidden = d_output.dot(wo.T)
d_hidden = error_hidden * sigmoid_derivative(hidden_output)

learning_rate = 0.1

wo += hidden_output.T.dot(d_output) * learning_rate
bo += d_output * learning_rate

wh += X.T.dot(d_hidden) * learning_rate
bh += d_hidden * learning_rate

print("\n✅ Updated Weights and Biases After Backpropagation:")
print("Updated input → hidden weights:\n", wh)
print("Updated hidden biases:\n", bh)
print("Updated hidden → output weights:\n", wo)
print("Updated output bias:\n", bo)