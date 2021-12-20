import torch
import inspect
print(inspect.getdoc(torch.zeros))


a = torch.zeros(size=[2,3])
b = a+1

c = a + b