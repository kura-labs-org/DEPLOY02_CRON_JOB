import sys,subprocess,os,getpass,datetime
pwd = os.getcwd()
uuidgen = subprocess.run(['uuidgen'],stdout = subprocess.PIPE)
f = uuidgen.stdout.decode('utf-8').strip('\n')
a = os.path.isfile(f'{pwd}/Deploy/main')
if a:
	print('[+] Found Deployable File')
	deploy = subprocess.run(['./Deploy/main'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	if deploy.stderr:
		l = deploy.stderr.decode('utf-8').strip('\n')
		print(f'[-] Error: Deploying File {l}')
		with open(f'{pwd}/logs/deploylogs/e_{a}.log','w') as errorLog:
				errorLog.write(f'{datetime.datetime.now()},1,{l},{getpass.getuser()},{os.getuid()}')
				errorLog.close()
		sys.exit(1)
	else:
		with open(f'{pwd}/logs/deploylogs/s_{a}.log','w') as succesLog:
				succesLog.write(f'{datetime.datetime.now()},0,deploy successful,{getpass.getuser()},{os.getuid()}')
				succesLog.close()
		print('[+] File Deployed')
		print('[*] Deleted file to test cron job')
		os.system('rm Deploy/main')
		sys.exit(0)
else:
	print('[-] Error: Can Not Find File')
	sys.exit(1)
