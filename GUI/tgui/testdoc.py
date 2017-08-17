import subprocess

def RunCmd(curCmd):
    pipe = subprocess.Popen(curCmd,shell = True,stdout =subprocess.PIPE).stdout
    printStr = pipe.read()
    return printStr
