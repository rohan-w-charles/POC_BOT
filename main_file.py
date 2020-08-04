import os
import argparse
import platform

if __name__ == "__main__":
    """
    Test Stuff
    """
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input_file", type=str, required=True, help="path\
         to input python file")
    ap.add_argument("-v", "--virtualenv_folder", type=str, required=True, help="path\
         to virtualenv")
    args = ap.parse_args()
    i = args.input_file
    v = args.virtualenv_folder
    if platform.system().lower() == 'linux':
        process = f". ./{v}/bin/activate && python3 {i}"
    else:
        raise "Unknown platfrom"
    os.system(process)
