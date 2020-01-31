import shutil
import os

def copy_common(target):
    print("Creating Common:"+ target)
    shutil.rmtree("{}/common".format(target),)
    os.mkdir("{}/common".format(target))
    os.system('cp -v ./particles/particle_engine.py ./{0}/common/.'.format(target))

print('Copy common files to game dirs')

copy_common("lemon_leak")
copy_common("galga")
