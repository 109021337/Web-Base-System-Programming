from email import message
import re
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from chaapp import forms, models
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from chaapp import models
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from .models import book


message = ''
cartlist = []  #購買商品串列
customname = ''  #購買者姓名
customphone = ''  #購買者電話
customaddress = ''  #購買者地址
customemail = ''  #購買者電子郵件


def login(request):
	if request.method == "POST":
		postform = forms.PostForm(request.POST)
		if postform.is_valid():  #forms驗證通過
			username = postform.cleaned_data['username']
			pd =  postform.cleaned_data['pd']
			user1 = authenticate(username=username, password=pd)  #管理者驗證
			if user1 is not None:  #驗證通過
				auth.login(request, user1)  #登入
				postform = forms.PostForm()
				return redirect('/index/')
			else:  #驗證未通過
				messages.info(request, '密碼錯誤!')
		else:
			messages.info(request, '驗證碼錯誤!')
	else:
		postform = forms.PostForm()
	return render(request, "login.html", locals())

def register(request):
	if request.method == "POST":
		#Data
		FName = request.POST['FName']
		LName = request.POST['LName']
		cName = request.POST['username']
		cEmail = request.POST['email']
		cPassword = request.POST['password']
		try:
			user=User.objects.get(username=cName)
		except:
			user=None
		if user!=None:
			message = user.username + " 帳號已建立!"
			return render(request, "createsuccess.html", locals())
		else:	# 建立 test 帳號			
			user=User.objects.create_user(cName,cEmail,cPassword)
			user.first_name=LName
			user.last_name=FName
			user.is_staff=False	# 工作人員狀態
			user.save()
			return redirect('/createsucces/')
	else:
		return render(request, "add.html", locals())

def edit(request, name=None, mode=None):
	if(name != None):
		if(mode == "load"):
			unit = User.objects.get(username = name)
			urlname = name
			return render(request, "edit.html", locals())
		elif(mode == "save"):
			unit = User.objects.get(username = name)
			unit.first_name = request.POST['FName']
			unit.last_name = request.POST['LName']
			unit.email = request.POST['email']
			newpassword = request.POST['password']
			unit.set_password(newpassword)
			unit.save()
			message = '已修改資料'
	return redirect('/news/')

def bookview(request, isbn=None):
	try:
		unit = book.objects.get(ISBN = isbn)
		cover = "'/images/"+ unit.Cover+"'"
		return render(request, "book.html", locals())
	except:
		return redirect('/news/')

def adduser(request):
	return render(request, "add.html", locals())

def createsucces(request):
	return render(request, "createsuccess.html", locals())

def manage(request):
    return render(request, "manage.html", locals())

def news(request):
	mydata = book.objects.all().order_by('-Purchased').values()
	popular = mydata[:4]
	popular2 = mydata[4:8]
	popular3 = mydata[8:12]
	mydata2 = book.objects.all().order_by('Purchased').values()
	recommend = mydata2[:4]
	recommend2 = mydata2[4:8]
	return render(request, "news.html", locals())

def aboutus(request):
	title = "關於我們"
	return render(request, "about.html", locals())

def service(request):
	return render(request, "service.html", locals())

def index(request):
	return render(request, "index.html", locals())

# 文學小說
def literature1(request):
    return render(request, "literature1.html", locals())

def literature2(request):
    return render(request, "literature2.html", locals())

def literature3(request):
    return render(request, "literature3.html", locals())

# 財經企管
def finance1(request):
    return render(request, "finance1.html", locals())

def finance2(request):
    return render(request, "finance2.html", locals())

def finance3(request):
    return render(request, "finance3.html", locals())

# 語言
def language1(request):
    return render(request, "language1.html", locals())

def language2(request):
    return render(request, "language2.html", locals())

def language3(request):
    return render(request, "language3.html", locals())

# 飲食料理 cooking
def cooking1(request):
    return render(request, "cooking1.html", locals())

def cooking2(request):
    return render(request, "cooking2.html", locals())

def cooking3(request):
    return render(request, "cooking3.html", locals())

# 日本輕小說
def light_novel1(request):
    return render(request, "light_novel1.html", locals())

def light_novel2(request):
    return render(request, "light_novel2.html", locals())

def light_novel3(request):
    return render(request, "light_novel3.html", locals())

def light_novel4(request):
    return render(request, "light_novel4.html", locals())

# 電腦資訊
def computer1(request):
    return render(request, "computer1.html", locals())

def computer2(request):
    return render(request, "computer2.html", locals())

def computer3(request):
    return render(request, "computer3.html", locals())

def computer4(request):
    return render(request, "computer4.html", locals())

def computer5(request):
    return render(request, "computer5.html", locals())

def question(request):
	return render(request, "question.html", locals())

def logout(request):
	auth.logout(request)
	return redirect('/login/')

def cart(request):  #顯示購物車
	global cartlist
	cartlist1 = cartlist  #以區域變數傳給模版
	total = 0
	for unit in cartlist:  #計算商品總金額
		total += int(unit[3])
	grandtotal = total + 10  #加入運費總額
	return render(request, "cart.html", locals())

def addtocart(request, ctype=None, bookid=None):
	global cartlist
	if ctype == 'add':  #加入購物車
		books = book.objects.get(id=bookid)
		flag = True  #設檢查旗標為True
		for unit in cartlist:  #逐筆檢查商品是否已存在
			if books.Name == unit[0]:  #商品已存在
				unit[2] = str(int(unit[2])+ 1)  #數量加1
				unit[3] = str(int(unit[3]) + books.Price)  #計算價錢
				flag = False  #設檢查旗標為False
				break
		if flag:  #商品不存在
			temlist = []  #暫時串列
			temlist.append(books.Name)  #將商品資料加入暫時串列
			temlist.append(str(books.Price))  #商品價格
			temlist.append('1')  #先暫訂數量為1
			temlist.append(str(books.Price))  #總價
			temlist.append(int(books.id))  #總價
			cartlist.append(temlist)  #將暫時串列加入購物車
		request.session['cartlist'] = cartlist  #購物車寫入session
		return redirect('/cart/')
	elif ctype == 'update':  #更新購物車
		n = 0
		for unit in cartlist:
			unit[2] = request.POST.get('qty' + str(n), '1')  #取得數量
			unit[3] = str(int(unit[1]) * int(unit[2]))  #取得總價
			n += 1
		request.session['cartlist'] = cartlist
		return redirect('/cart/')
	elif ctype == 'empty':  #清空購物車
		cartlist = []  #設購物車為空串列
		request.session['cartlist'] = cartlist
		return redirect('/cart/')
	elif ctype == 'remove':  #刪除購物車中商品
		del cartlist[int(bookid)]  #從購物車串列中移除商品
		request.session['cartlist'] = cartlist
		return redirect('/cart/')

def cartorder(request):  #按我要結帳鈕
	global cartlist, message, customname, customphone, customaddress, customemail
	cartlist1 = cartlist
	total = 0
	for unit in cartlist1:  #計算商品總金額
		total += int(unit[3])
	grandtotal = total + 10
	customname1 = customname  ##以區域變數傳給模版
	customphone1 = customphone
	customaddress1 = customaddress
	customemail1 = customemail
	message1 = message
	return render(request, "cartorder.html", locals())

def cartok(request):  #按確認購買鈕
	global cartlist, message, customname, customphone, customaddress, customemail
	total = 0
	for unit in cartlist:
		total += int(unit[3])
		books = book.objects.get(id=unit[4])
		if books.Purchased == None:
			books.Purchased == 0
		else:
			books.Purchased += int(unit[2])
		books.save()
	grandtotal = total + 10
	message = ''
	customname = request.POST.get('CustomerName', '')
	customphone = request.POST.get('CustomerPhone', '')
	customaddress = request.POST.get('CustomerAddress', '')
	customemail = request.POST.get('CustomerEmail', '')
	paytype = request.POST.get('paytype', '')
	customname1 = customname
	if customname=='' or customphone=='' or customaddress=='' or customemail=='':
		message = '姓名、電話、住址及電子郵件皆需輸入'
		return redirect('/cartorder/')
	else:
		unitorder = models.order.objects.create(subtotal=total, shipping=10, grandtotal=grandtotal, customname=customname, customphone=customphone, customaddress=customaddress, customemail=customemail, paytype=paytype) #建立訂單
		for unit in cartlist:  #將購買商品寫入資料庫
			total = int(unit[1]) * int(unit[2])
			unitdetail = models.detail.objects.create(dorder=unitorder, pname=unit[0], unitprice=unit[1], quantity=unit[2], dtotal=total)
		orderid = unitorder.id  #取得訂單id
		mailfrom="gmail帳號"  #帳號
		mailpw="gmail密碼"  #密碼
		mailto=customemail  #收件者
		mailsubject="織夢數位購物網-訂單通知";  #郵件標題
		mailcontent = "感謝您的光臨，您已經成功的完成訂購程序。\n我們將儘快把您選購的商品郵寄給您！ 再次感謝您支持\n您的訂單編號為：" + str(orderid) + "，您可以使用這個編號回到網站中查詢訂單的詳細內容。\n織夢數位購物網" #郵件內容
		send_simple_message(mailfrom, mailpw, mailto, mailsubject, mailcontent)  #寄信
		cartlist = []
		request.session['cartlist'] = cartlist
		return render(request, "cartok.html", locals())

def cartordercheck(request):  #查詢訂單
	orderid = request.GET.get('orderid', '')  #取得輸入id
	customemail = request.GET.get('customemail', '')  #取得輸email
	if orderid == '' and customemail == '':  #按查詢訂單鈕
		firstsearch = 1
	else:
		order = models.order.objects.filter(id=orderid).first()
		if order == None or order.customemail != customemail:  #查不到資料
			notfound = 1
		else:  #找到符合的資料
			details = models.detail.objects.filter(dorder=order)
	return render(request, "cartordercheck.html", locals())

def send_simple_message(mailfrom, mailpw, mailto, mailsubject, mailcontent): #寄信
	global message
	strSmtp = "smtp.gmail.com:587"  #主機
	strAccount = mailfrom  #帳號
	strPassword = mailpw  #密碼
	msg = MIMEText(mailcontent)
	msg["Subject"] = mailsubject  #郵件標題
	mailto1 = mailto  #收件者
	server = SMTP(strSmtp)  #建立SMTP連線
	server.ehlo()  #跟主機溝通
	server.starttls()  #TTLS安全認證
	try:
		server.login(strAccount, strPassword)  #登入
		server.sendmail(strAccount, mailto1, msg.as_string())  #寄信
	except SMTPAuthenticationError:
		message = "無法登入！"
	except:
		message = "郵件發送產生錯誤！"
	server.quit() #關閉連線
