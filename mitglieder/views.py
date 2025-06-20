from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
def mitglieder(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def allMembers(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('member_detail.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))