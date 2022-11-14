import os, shutil
from PIL import Image

# install crunch => https://github.com/chrissimpkins/Crunch/blob/master/docs/EXECUTABLE.md#install

cwd = os.path.dirname(__file__)
fp_inputs = os.path.join(cwd, '__inputs')

for img_name_with_ext in [img_name_with_ext for img_name_with_ext in os.listdir(fp_inputs) if img_name_with_ext.endswith('.png')]:
  img_name = img_name_with_ext.split('.', 1)[0]
  img_in_path = os.path.join(fp_inputs, img_name_with_ext)
  img_out_folder_path = os.path.join(cwd, img_name)

  shutil.rmtree(img_out_folder_path, ignore_errors=True)
  os.makedirs(img_out_folder_path)

  img = Image.open(img_in_path)

  img_128 = img.resize((128, 128))
  img_64 = img.resize((64, 64))
  img_32 = img.resize((32, 32))

  path_128 = os.path.join(img_out_folder_path, '128.png')
  path_128_crunch = os.path.join(img_out_folder_path, '128-crunch.png')
  img_128.save(path_128)
  os.system(f'crunch \'{path_128}\'')
  os.remove(path_128)
  os.rename(path_128_crunch, path_128)

  path_64 = os.path.join(img_out_folder_path, '64.png')
  path_64_crunch = os.path.join(img_out_folder_path, '64-crunch.png')
  img_64.save(path_64)
  os.system(f'crunch \'{path_64}\'')
  os.remove(path_64)
  os.rename(path_64_crunch, path_64)

  path_32 = os.path.join(img_out_folder_path, '32.png')
  path_32_crunch = os.path.join(img_out_folder_path, '32-crunch.png')
  img_32.save(path_32)
  os.system(f'crunch \'{path_32}\'')
  os.remove(path_32)
  os.rename(path_32_crunch, path_32)