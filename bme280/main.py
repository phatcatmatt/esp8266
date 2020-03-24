from machine import Pin, I2C
# import bme280_float as bme280
import BME280

i2c = I2C(scl=Pin(5), sda=Pin(4))
# bme = bme280.BME280(i2c=i2c)
# print(bme.values)

bme = BME280.BME280(i2c=i2c)
temp = bme.temperature
hum = bme.humidity
pres = bme.pressure

# uncomment for temperature in Fahrenheit
temp = (bme.read_temperature()/100) * (9/5) + 32
temp = str(round(temp, 2)) + 'F'

sensor_readings = {'value1': temp, 'value2': hum, 'value3': pres}
print(sensor_readings)
