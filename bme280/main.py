from machine import Pin, I2C
import bme280_float as bme280

i2c = I2C(scl=Pin(5), sda=Pin(4))
bme = bme280.BME280(i2c=i2c)

print(bme.values)
