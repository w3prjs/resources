import os, subprocess

for root, subdirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
    for file in files:
        if file.endswith('-min.svg') or not file.endswith('.svg'):
            continue

        p_in  = os.path.join(root, file)
        p_out = p_in.replace('.svg', '-min.svg')

        subprocess.getoutput(f'svgo {p_in} -o {p_out}')