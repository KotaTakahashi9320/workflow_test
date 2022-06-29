import subprocess
import sys
path = sys.argv[1]
print(path)
subprocess.run(
    ['python', '-m', 'nuitka', '--module', path+'/op.py', '--follow-imports'],
    cwd=f"{path}")
subprocess.call(
    'rm -r *.build *.pyi',
    cwd=f"{path}", shell=True)