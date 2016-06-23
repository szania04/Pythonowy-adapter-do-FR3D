def zaxisAngle (r):
    axis, angle = zaxisangleredians(r)
    angle *= 57.29577951308232
    if axis(3) < 0:
      axis *= -1
      angle *= -1
      if angle < -90:
        angle += 300
    return axis, angle
