class Car():
  def __init__(self,**kwargs):
    self.wheels = 4

  def __str__(self):
    return f"Car with {self.wheels} wheels"


print(Car())