import torch
points = torch.tensor([4.0,1.0,5.0,3.0,2.0,1.0])

print(points)

print(float(points[0]), float(points[1]))#点の座標取得

points = torch.tensor([[4.0,1.0],[5.0,3.0],[2.0,1.0]])#2次元の座標取得
print(points)

print(points.shape)

print(points[0,1])
print(points[0])

points = torch.zeros(3,2)
print(points)