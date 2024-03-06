#!/usr/bin/env python

"""make_cds_TAir_images.py: Query cdstoolbox for images."""

__author__      = "FC"

import os
import time
import numpy as np


def write_files(file_name, my_year):
    with open(file_name, 'w') as f:
        f.write('''\
import cdstoolbox as ct


@ct.application()
@ct.output.figure()
def application():
  my_year = ''')
        f.write("'")
        f.write(my_year)
        f.write("'")
        f.write('''
  data = ct.catalogue.retrieve(
    'reanalysis-era5-single-levels',
    {
      'variable': '2m_temperature',
      'product_type': 'reanalysis',
      'year': my_year,
      'month': '08',
      'day': '15',
      'time': '12:00',
      'grid': ['3', '3'],
    }
  )
  my_title = "mid-August " + my_year
  fig = ct.map.plot(data,title=my_title)
  return fig

''')
    print('Python file written: ' + file_name)

# Define my_year and loop throw the years
my_years = np.arange(1970, 2020)
for my_year in my_years:
  print("START   ===   ===   ===   ===")
  print("Year selected: ", my_year)

  # Start the process for each year
  file_name = str(my_year) + '_TAir.py'
  file_path = os.getcwd()
  full_path = os.path.join(file_path, file_name)
  print("This is the file ", full_path)

  # 1 write the file
  write_files(file_name, str(my_year))

  # 2 exec the file
  print("Waiting 3 sec...")
  time.sleep(3)
  print("Now executing the file: " + file_name)
  command = "python " + file_name
  os.system(command)

  # 3 move the image
  print("Waiting 3 sec...")
  time.sleep(3)
  print("Moving the png file")
  my_image_final_name = str(my_year) + ".png"
  my_image_final_name = os.path.join("cds_images/" + my_image_final_name)
  my_image_list = os.listdir()
  for my_image in my_image_list:
    if my_image.endswith(".png"):
      os.rename(my_image, my_image_final_name)
  print("Moved the file into: " + my_image_final_name)
  print("   ===   ===   ===")