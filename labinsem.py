import torch
import torch.nn as nn

# --------------------------
# 1. Dataset (Sequence Data)
# --------------------------
# Example: sequences (like time steps)
# Shape: (batch_size, seq_len, input_size)

X = torch.tensor([
    [[0.0], [1.0], [0.0]],
    [[1.0], [0.0], [1.0]],
    [[0.0], [0.0], [1.0]],
    [[1.0], [1.0], [0.0]]
])

y = torch.tensor([[0.0], [1.0], [0.0], [1.0]])

# --------------------------
# 2. RNN Model
# --------------------------
class RNNModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.rnn = nn.RNN(input_size=1, hidden_size=4, batch_first=True)
        self.fc = nn.Linear(4, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        out, _ = self.rnn(x)
        out = out[:, -1, :]   # take last time step
        out = self.fc(out)
        out = self.sigmoid(out)
        return out

model = RNNModel()

# --------------------------
# 3. Loss & Optimizer
# --------------------------
loss_fn = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# --------------------------
# 4. Training
# --------------------------
for epoch in range(200):
    y_pred = model(X)
    loss = loss_fn(y_pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 20 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item()}")

# --------------------------
# 5. Testing
# --------------------------
test = torch.tensor([[[1.0], [0.0], [1.0]]])
output = model(test)

print("\nTest Output:", output)

if output.item() > 0.5:
    print("Class 1")
else:
    print("Class 0")