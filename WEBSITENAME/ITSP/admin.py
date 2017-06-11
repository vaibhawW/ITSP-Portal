from django.contrib import admin
from .models import passwordList,team
class PasswordListView(admin.ModelAdmin):
    list_display = ['id','password']
class TeamListView(admin.ModelAdmin):
	list_display = ['team_id','team_name','project_name','member1','member2','member3','member4','mentor','club','slot','bill','teamPic','documentation','video','description']

admin.site.register(passwordList,PasswordListView)
admin.site.register(team,TeamListView)

# I have shown the necessary informations only in above list view. If you want to change objects, then comment out the above 2 and uncomment the below.
# admin.site.register(passwordList)
# admin.site.register(team)
