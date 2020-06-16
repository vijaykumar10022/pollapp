from django.shortcuts import render,redirect
from app.models import POLL,Spoll,Names
from app.forms import Myform
from django.http import HttpResponse
# Create your views here.
def poll_q(req):
	if req.method=="POST":
		que=req.POST['question']
		data=POLL(question=que)
		data.save()
		sp=Spoll.objects.all().delete()
		return redirect('/result')
	return render(req,'app/poll_q.html',{})
def answer(req):
	if req.method =="POST":
		data=Names(name=req.POST['name'])
		data.save()
		return redirect('/submit')
	return render(req,'app/answer.html')
def submit(req):
	if req.method=="POST":
		data=Myform(req.POST)
		data.save()
		return HttpResponse("Done")
	form=Myform()
	data=POLL.objects.last()
	# data={'data':data.question}
	return render(req,'app/submit.html',{'form':form,'data':data.question})
def result(req):
	data=Spoll.objects.all()
	y=0
	n=0
	for i in data:
		if i.opt=="Yes":
			y=y+1
		else:
			n=n+1
	data={'Yes':y,"No":n}
	return render(req,"app/result.html",{'data':data})