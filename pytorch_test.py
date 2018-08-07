# -*- coding: utf-8 -*-

#  pytorch_test.py

import torch



x = torch.Tensor(5, 3)
y = torch.rand(5,3)
print(x+y)
print(torch.add(x, y))



result = torch.Tensor(5, 3)
torch.add(x, y, out=result)
print(result)
y.add_(x)
print(y)



