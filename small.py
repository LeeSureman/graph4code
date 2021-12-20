import torch

a = torch.zeros(size=[2,3])
b = a.transpose(0,1)

c = a + b