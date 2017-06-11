from django.forms import ModelForm,PasswordInput,CharField,IntegerField
from .models import team

class projectForm(ModelForm):
	password = CharField(widget=PasswordInput())
	team_id = IntegerField(min_value=1)
	class Meta:
		model=team
		fields = [
			"team_name",
			"team_id",
			"password",
			"project_name",
			"description",
			"member1",
			"member2",
			"member3",
			"member4",
			"mentor",
			"club",
			"slot",
			"teamPic",
			"documentation",
			"video",
			"bill"
		] 
		labels = {
			"team_name":"Team Name",
			"password":"Team Password",
			"project_name":"Project Name",
			"discription":"Project Description",
			"mem1":"Member 1 Name (leader)", 
			"mem2":"Member 2 Name", 
			"mem3":"Member 3 Name", 
			"mem4":"Member 4 Name", 
			"mentor":"Mentor's Name",
			"club":"Club",
			"team_id":"Team Id",
			"slot":"Slot",
			"teamPic":"Team Picture (image files)",
			"documentation":"Documents (only PDF files)",
			"video":"Project Video (youtube link)",
			"bill":"Bill Submitted" ,
		}
		error_messages={
			"team_name":{
				"required":"I want your team name, please!",
				"max_length":"What are you trying to do?",
				"min_length":"Hmm, suspecious"
			},
			"project_name":{
				"required":"You worked on some project, right?",
				"max_length":"That's suspecious",
				"min_length":"Please... Stop this"
			},
			"description":{
				"required":"Can you describe your peoject a little bit more please."
			},
			"member1":{
				"required":"Someone should take the responsibility, right?",
				"max_length":"A nick(smaller) name will be appreciated :)",
				"min_length":"I cant speak your name, bro"
			},
			"member2":{
				"max_length":"A nick(shorter) name will be appreciated :)"
			},
			"member3":{
				"max_length":"A nick(shorter) name will be appreciated :)"
			},
			"member4":{
				"max_length":"A nick(shorter) name will be appreciated :)"
			},
			"mentor":{
				"required":"Sir! We all need some guidance, right?",
				"max_length":"Write the name you used to call him by ;P",
				"min_length":"hmmm, how do I call him??"
			},
			"club":{
				"required":"We need to categorize your projects",
				"invalid_choice":"How did you end up with such choice?"
			},
			"team_id":{
				"required":"You can find your id at resouces section.",
				"invalid":"That was definitely a invalid entry, try to enter the true id",
				"min_value":"I don't think that's your teams id."
			},
			"slot":{
				"required":"We need it. Don't ask why, jusk know that we need it.",
				"invalid_choice":"There are only two options T_T"
			},
			"teamPic":{
				"invalid_image":"Our reSources says dats not any image."
			},
			"documentation":{
				"required":"Documentaion is inevitable in this world",
				"invalid":"Sir/Mam, please convert it to PDF, then upload."
			},
			"video":{
				"invalid":"URL is something you find in addressbar."
			},
			"bill":{
				"required":"YES or NO, simple right?"
			},
		}