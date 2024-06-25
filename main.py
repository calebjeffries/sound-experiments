#!/bin/python3

import struct
import math

# Change these values to suit your needs
SAMPLE_RATE = 48000
OUTPUT_FILE = "out.wav"

# Your function to make a sound
def generatesound():
  """
  This is your space to create the sound and put the samples in an array.
  Make sure the amplitude stays within -32767 and 32767, or there will be an error.
  Also, the array should be integers only.

  A simple example to generate a sine wave at 440Hz for one second would be:
  """
  outarray = []
  frequency = 440
  for x in range(0, SAMPLE_RATE):
    amplitude = 30000 * math.sin(2 * math.pi * x / (SAMPLE_RATE / frequency))
    outarray.append(int(amplitude))
  return outarray

# Function to write a wav file for output
def writeoutput(wavdata):
  outfile = open(OUTPUT_FILE, "wb")
  outfile.write(b'RIFF')
  outfile.write(struct.pack("<I", len(wavdata) * 2 + 44))
  outfile.write(b'WAVEfmt ')
  outfile.write(struct.pack("<I", 16))
  outfile.write(struct.pack("<H", 1))
  outfile.write(struct.pack("<H", 1))
  outfile.write(struct.pack("<I", SAMPLE_RATE))
  outfile.write(struct.pack("<I", int(SAMPLE_RATE * 2)))
  outfile.write(struct.pack("<H", 2))
  outfile.write(struct.pack("<H", 16))
  outfile.write(b'data')
  for sample in wavdata:
    outfile.write(struct.pack("@h", sample))
  outfile.close()

# Generate the file
writeoutput(generatesound())

