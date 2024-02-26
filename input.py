import sys
def prints(s:str):
       sys.stdout.write(s)
         
def inputs(s:str)->str:
       prints(s)
       return sys.stdin.readline()
prints("\x1bc\x1b[41;37m\n")
s=inputs("give me a number?\n")
prints(s+"\n")