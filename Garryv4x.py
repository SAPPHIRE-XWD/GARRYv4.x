import os, sys, platform

os.system('rm -rf Garry.cpython-311.so')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf Garry.cpython-311.so')
except:
    pass


bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile("Garry.cpython-311.so"):
        os.system('curl -L https://github.com/SAPPHIRE-XWD/GARRYv4.x/executables/blob/main/Garry.cpythonv-311.so') 
        import Garry.main()
    else:
        import Garry.main()

elif bit == '32bit':
    if not os.path.isfile('Garry.cpython-311.so'):
        os.system('curl -L https://github.com/SAPPHIRE-XWD/GARRYv4.x/executables/blob/main/Garry.cpython-311.so')
        import Garry.main()
    else:
        import Garry.main()