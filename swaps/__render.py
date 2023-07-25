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
    img.save(os.path.join(img_out_folder_path, 'org.png'))

    for size in [
        512,
        256,
        128,
        64,
        32,
        16
    ]:
        img_sized =  img.resize((size, size))
        path_sized = os.path.join(img_out_folder_path, f'{size}.png')
        path_sized_crunch = os.path.join(img_out_folder_path, f'{size}-crunch.png')
        img_sized.save(path_sized)
        os.system(f'crunch \'{path_sized}\'')
        os.remove(path_sized)
        os.rename(path_sized_crunch, path_sized)