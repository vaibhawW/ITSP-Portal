from django.shortcuts import render
# from django.http import HttpResponseRedirect
from .form import projectForm
from .models import passwordList,team

def index(request):
	allEntries = team.objects.all();
	bio=[]
	aero = []
	erc = []
	wncc = []
	for x in allEntries:
		char = x.club
		if "Biotech" in str(char):
			bio.append(x)
		if "Aero" in str(char):
			aero.append(x)
		if "Electro" in str(char):
			erc.append(x)
		if "Web" in str(char):
			wncc.append(x)
	return render(request,"index.html",{"all":allEntries,"biotech":bio,"aero":aero,"erc":erc,"wncc":wncc});

def submitProject(request):
	if request.method == "POST":
		form = projectForm(request.POST,request.FILES)
		if form.is_valid():
			if request.FILES['documentation'].name[-4:]==".pdf":
				if passwordList.objects.filter(id=request.POST['team_id']).get().password==request.POST['password']:
					if team.objects.filter(team_id=request.POST['team_id']).exists():
						team.objects.filter(team_id=request.POST['team_id']).delete()
					instance = form.save(commit=False)
					instance.save()
					return render(request,"submitted.html",{'URL':"/ITSP/project/%s" %request.POST['team_id']})
				else: return render(request,"wrongPassword.html",{'URL':"/ITSP/submitProject"})
	else :
		form =projectForm();
	return render(request,"form.html",{"form":form})

def showCase(request,id):
	k = list(team.objects.filter(team_id=id));
	return render(request,"projectShowCase.html",{"data":k[0]});

# def makePassword(request):
# 	k=''
# 	for x in range(150):
# 		k = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
# 		password.objects.create(password = k);
# 	return HttpResponse("Done! Creating Password")