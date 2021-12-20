import torch
import inspect
print(inspect.getdoc(torch.zeros))


a = torch.zeros(size=[2,3])
b = torch.ones(size=[4,5])

c = a.transpose(0,1)
d = torch.transpose(0,1)