
from django.db import models

class Calculation(models.Model):
    Q = models.FloatField()  # Q 값 (축 방향 외력)
    Z = models.IntegerField()  # Z 값 (볼트 개수)
    shouli1 = models.FloatField()  # 계산된 F 값
    μ = models.FloatField()
    m = models.IntegerField()
    Z1 = models.IntegerField()
    kf = models.FloatField()
    R = models.FloatField()
    shouli2 = models.FloatField()
    Z3 = models.IntegerField()  # Z 값 (볼트 개수)
    shouli3 = models.FloatField()  # 계산된 F 값
    T = models.FloatField() 
    shouli4 = models.FloatField()
    r_values = models.JSONField()

    def __str__(self):
        return f"Q: {self.Q}, Z: {self.Z}, shouli1: {self.shouli1} N, shouli2={self.shouli2} N, kf={self.kf}, R={self.R} N, μ={self.μ}, m={self.m}, Z1={self.Z1}, R={self.R}, Z3={self.Z3}, shouli3={self.shouli3}, T={self.T}, shouli4={self.shouli4}"
    