import time
import numpy as np
from scipy.fft import fft

#defining functions
def get_FF(inputsignal):
  '''
  Returns the focused feature of the signal of 150.2 Hz
  '''

  fourier_coeffs = fft(inputsignal)
  p_alpha = np.mean(np.abs(fourier_coeffs[16:24]))
  focusfeature = 1/p_alpha

  return focusfeature/2.7

#algorithm to compute BFF of 10 second signal

def get_BFF(basesignal):
  '''
  Returns the baseline focused feature of the signal of 150.2 Hz
  '''

  fourier_coeffs = fft(basesignal)
  p_alpha = np.mean(np.abs(fourier_coeffs[80:120]))
  focusfeature = 1/p_alpha

  return focusfeature


def parse_input(focusfeature, baselinefocusfeature):
  '''
  Parses input based on features, 1 denotes upward, 0 denotes downwards
  '''

  a = focusfeature
  b = baselinefocusfeature

  if a > b:
    return 1 #this represents up
  else:
    return 0 #this represents down

#eeg_pong_data is the txt file being written from PySerial in an actual application case

with open("sample_eeg_pong_data.txt", "r") as file: 
    data = file.readlines()
    count = 0;
    signalwindow = []
    baselinewindow = []
    for line in data: 
        if count < 500:
          pass
        elif count < 2003:
          baselinewindow.append(float(line))
        elif count < 2303:
          signalwindow.append(float(line))
        else: 
          signalwindow.pop(0)
          signalwindow.append(float(line))
          print(parse_input(get_FF(signalwindow), get_BFF(baselinewindow)))
        sleep(1/150)
        count += 1

sample_data.close()

