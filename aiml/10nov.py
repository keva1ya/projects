import torch
import torch.nn as nn
from torchvision import models

class ConvNeXtLargeClassifier(nn.Module):
    def __init__(self, output_class: int = 1000):
        super(ConvNeXtLargeClassifier, self).__init__()
        
        
        self.backbone = models.convnext_large(weights=models.ConvNeXt_Large_Weights.IMAGENET1K_V1)
        
        in_features = self.backbone.classifier[2].in_features
        
        self.backbone.classifier[2] = nn.Linear(in_features, output_class)
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass through the ConvNeXt Large model."""
        return self.backbone(x)
