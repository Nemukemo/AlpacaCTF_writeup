from subprocess import run, DEVNULL

run('cat flag.txt > ' + input('cat flag.txt > ')[:10], shell=True, stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL)
