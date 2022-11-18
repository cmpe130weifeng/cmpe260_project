import torch
import torch.nn as nn
import torchvision

class RPSCNN(nn.Module):

    def __init__(self):
        super(RPSCNN, self).__init__()

        self.layer1 = nn.Sequential(
            nn.Conv2d(in_channels=4, out_channels=32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        self.layer2 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        self.fc1 = nn.Linear(in_features=64 * 24 * 24, out_features=5000)
        self.fc2 = nn.Linear(in_features=5000, out_features=10)
        self.fc3 = nn.Linear(in_features=10, out_features=3)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = out.view(out.size(0), -1)
        out = self.fc1(out)
        out = self.fc2(out)
        out = self.fc3(out)
        out = nn.functional.log_softmax(out, dim=1)

        return out


