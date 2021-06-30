# -*- coding: utf-8 -*-
# file: lcf_pooler.py
# time: 2021/6/29
# author: yangheng <yangheng@m.scnu.edu.cn>
# github: https://github.com/yangheng95
# Copyright (C) 2021. All Rights Reserved.
import numpy
import torch
import torch.nn as nn


class LCF_Pooler(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.dense = nn.Linear(config.hidden_size, config.hidden_size)
        self.activation = nn.Tanh()

    def forward(self, hidden_states, asp_pos):
        # We "pool" the model by simply taking the hidden state corresponding
        # to the first token.
        device = hidden_states.device
        asp_pos = asp_pos.detach().cpu().numpy()
        pooled_output = numpy.zeros((hidden_states.shape[0], hidden_states.shape[2]), dtype=numpy.float32)
        hidden_states = hidden_states.detach().cpu().numpy()
        for i, pos in enumerate(asp_pos):
            pooled_output[i] = hidden_states[i][pos]

        pooled_output = torch.Tensor(pooled_output).to(device)
        pooled_output = self.dense(pooled_output)
        pooled_output = self.activation(pooled_output)
        return pooled_output