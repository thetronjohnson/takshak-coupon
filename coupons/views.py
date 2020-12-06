from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Data
import qrcode
from PIL import Image,ImageFont,ImageDraw 

BASE_DIR = settings.MEDIA_ROOT

def generate_coupon(name,no,amount):

	source = Image.open(BASE_DIR + '/coupon.jpg')
	font = ImageFont.truetype(BASE_DIR + "/OpenSans-Regular.ttf", 65)
	font2 = ImageFont.truetype(BASE_DIR + "/OpenSans-Regular.ttf", 130)



	path = settings.STATIC_URL+ f"reciept/{name}_{no}_coupon.jpg"

	draw = ImageDraw.Draw(source)

	draw.text((589,290), name,font=font,fill =(255, 0, 0))
	draw.text((480,365), no,font=font,fill =(255, 0, 0))
	draw.text((1843,780), amount + "/-",font=font2,fill =(0, 0, 0))


	qr_code = qrcode.make(f"Thank You for contributing Rs.{amount} for Takshak")

	source.paste(qr_code,(900,650))
	source.save(path)

	return ((settings.STATIC_URL + f"reciept/{name}_{no}_coupon.jpg"), f"{name}_{no}_coupon.jpg")
# Create your views here.

@login_required
def dashboard(request):
	if request.method == 'POST':
		name = request.POST['name']
		number = request.POST['number']
		amount = request.POST['amount']
		path, name = generate_coupon(name, number, amount)

		data = Data()
		data.created_by = request.user.username
		data.generated_for = name
		data.coupon_no = number
		data.amount = amount
		data.save()

		return render(request, 'dashboard.html',{'path':path, 'name':name})

	return render(request, 'dashboard.html')

def login_view(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	try:
		if request.POST:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			login(request,user)
			return redirect('dashboard')
	except:
		return HttpResponse('404 Page not found!')

	return render(request, 'login.html')

def auth_logout(request):
	logout(request)
	return redirect('login-view')