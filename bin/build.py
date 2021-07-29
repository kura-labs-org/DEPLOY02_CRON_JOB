import sys,subprocess,os,getpass,datetime
pwd = os.getcwd()
a = subprocess.run(['uuidgen'],stdout=subprocess.PIPE)
b = a.stdout.decode('utf-8').strip('\n')
i = os.getcwd()
example = os.path.isfile(f'{i}/software/Example.cpp')
if example:
	print('[+] Building Example File')
	p = subprocess.run(['g++',f'{pwd}/software/Example.cpp','-o','main'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	if p.stderr:
		l = p.stderr.decode('utf-8').strip('\n')
		with open(f'{pwd}/logs/buildlogs/e_{b}.log','w') as fe:
			fe.write(f'{datetime.datetime.now()},1,{l},{getpass.getuser()},{os.getuid()}')
			fe.close()
			print(f'[-] Error: Log Written to e_{b}.log')
	else:
		print('[+] Moving file to testing')
		c  = subprocess.run(['mv','main','testing'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		if c.stderr:
			print('[-] Error: Moving file to testing folder')
			sys.exit(1)
		else:
			with open(f'{pwd}/logs/buildlogs/s_{a}.log','w') as succesLog:
				succesLog.write(f'{datetime.datetime.now()},0,deploy successful,{getpass.getuser()},{os.getuid()}')
				succesLog.close()
			print('[+] File waiting to be tested')
			sys.exit(0)
else:
	print('[-] Error: Cant Find Example File')
	sys.exit(1)