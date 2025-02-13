from __future__ import annotations

import argparse
from typing import Any

import numpy as np
import torch
import torch.nn.functional as F
from torch import nn

FC1_DIM = 1024
FC2_DIM = 128
FC_DROPOUT = 0.5


class MLP(nn.Module):
    """Simple MLP suitable for recognizing single characters.

    Example:
        data_config = {
            'input_dims': (784,),
            'mapping': {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                        5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        }
    """

    def __init__(
        self,
        data_config: dict[str, Any],
        args: argparse.Namespace = None,
    ) -> None:

        super().__init__()
        self.args = vars(args) if args is not None else {}
        self.data_config = data_config

        input_dim = np.prod(self.data_config["input_dims"])
        num_classes = len(self.data_config["mapping"])

        fc1_dim = self.args.get("fc1", FC1_DIM)
        fc2_dim = self.args.get("fc2", FC2_DIM)
        dropout_p = self.args.get("fc_dropout", FC_DROPOUT)

        self.fc1 = nn.Linear(input_dim, fc1_dim)
        self.dropout = nn.Dropout(dropout_p)
        self.fc2 = nn.Linear(fc1_dim, fc2_dim)
        self.fc3 = nn.Linear(fc2_dim, num_classes)

    def forward(self, x):
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.dropout(x)
        x = self.fc3(x)
        return x

    @staticmethod
    def add_to_argparse(parser):
        parser.add_argument("--fc1", type=int, default=FC1_DIM)
        parser.add_argument("--fc2", type=int, default=FC2_DIM)
        parser.add_argument("--fc_dropout", type=float, default=FC_DROPOUT)
        return parser
