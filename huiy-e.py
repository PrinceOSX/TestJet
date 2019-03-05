from lxml import html
import requests, re
import time, schedule
try:
	from linepy import *
except:
	print('You must install linepy')
	exit()
#Default linepy from python package installer
client = LINE(appName="CHROMEOS\t1.4.17\tChrome_OS\t1")

def seek(nub):
	# url web edit
	url = 'https://www.jetsadabet.com/login'
	page = requests.get(url)
	tree = html.fromstring(page.content)

	yiki_1 = tree.xpath('//*[@id="app"]/div[1]/div[5]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[{}]/td[1]/text()'.format(nub))
	yiki_2 = tree.xpath('//*[@id="app"]/div[1]/div[5]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[{}]/td[2]/text()'.format(nub))
	yiki_1 = re.findall('\d\d\d',str(yiki_1[0]))
	yiki_2 = re.findall('\d\d',str(yiki_2[0]))
	for group in client.getGroupIdsJoined():
		client.sendMessage(group,'รอบที่ {}\n หวยสามตัวบน {}\n หวยสองตัวล่าง {}'.format(nub,yiki_1[0],yiki_2[0]))
	#print('---------'*10)
	time.sleep(0)
	

def job():
	for i in range(1,88+1):
		try:
			seek(i)
		except Exception as e:
			print(e)
			try:
				seek(i)
			except Exception as e:
				print(e)
			
		

schedule.every().day.at("23:05").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
