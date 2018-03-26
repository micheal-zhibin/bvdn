from django.shortcuts import render
import json

from users.models import User
from tool_03.models import Blog, Comment

# Create your views here.
def index(request):
	a = Blog.objects.all().order_by('-id')[:5]
	return render(request, 'main/base.html', {'blogs': a})

def account_profile(request):
	if request.method == 'POST':
		a = json.loads(request.body)
		print(a)
		b = User.objects.get(email=request.user.email)
		b.name = a['name']
		b.sex = a['sex']
		b.birthday = a['birthday']
		b.job_number = a['job_number']
		b.zhengzhi_mianmao = a['zhengzhi_mianmao']
		b.zhengzhi_time = a['zhengzhi_time']
		b.job = a['job']
		b.job_time = a['job_time']
		b.job_2 = a['job_2']
		b.id_number = a['id_number']
		b.xue_li = a['xue_li']
		b.school = a['school']
		b.graduate_time = a['graduate_time']
		b.job_join_time = a['job_join_time']
		b.team_belong = a['team_belong']
		b.phone = a['phone']
		b.save()
	return render(request, 'main/accounts_profile.html')