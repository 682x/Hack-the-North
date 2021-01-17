#example use of PySerial to Interface with Arduino
import serial

ser = serial.Serial('COM4', baudrate = 115200, timeout = 1/150.2) #timeout is based on sampling rate
data = open("eeg_pong_data.txt", "w+") #the file that would be read from

while True:
  data.write(ser.readline() + "\n")

data.close()
