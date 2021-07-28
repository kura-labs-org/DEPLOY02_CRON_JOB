import sys,subprocess,os,datetime,getpass
uuidgen = subprocess.run(['uuidgen'],stdout= subprocess.PIPE)
a = uuidgen.stdout.decode('utf-8').strip('\n')
log = os.getcwd()
c = os.path.isfile(f'{log}/testing/main')
if a:
	chmod  = subprocess.run(['chmod','700','testing/main'],stdout = subprocess.PIPE,stderr=subprocess.PIPE)
	if chmod.stderr:
		print('[-] Error Changing attributes')
		sys.exit(1)
	else:
		test = subprocess.run(['./testing/main'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		if test.stderr:
			l = test.stderr.decode('utf-8')
			print(f'{l}')
			with open(f'{log}/logs/testingLogs/e_{a}.log','w+') as errorLog:
				errorLog.write(f'{datetime.datetime.now()},1,{l},{getpass.getuser()},{os.getuid()}')
				errorLog.close()
			sys.exit(1)
		else:
			with open(f'{log}/logs/testinglogs/s_{a}.log','x') as successLog:
				successLog.write(f'{datetime.datetime.now()},0,test successful,{getpass.getuser()},{os.getuid()}')
				successLog.close()
			print('[+] Build Complete. file moved To deployment')
			os.system('mv testing/main Deploy/')
			sys.exit(0)
else:
	print('[-] Error can not find main file')
	sys.exit(1)
