from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage 

# Create your views here.
def home(request):
    return render (request,"home.html")

def about(request):
    return render (request, "about.html")

def projects(request):
        projects_shows=[
            { 
                 "title":"Exam Portal",
                "path":"images/exam.jpg",
                "github_url":"https://github.com/MahadevprasadDL/Exam-Portal"
            },

            { 
                 "title":"Healthcare Management system",
                "path":"images/health.png",
                "github_url":"https://github.com/MahadevprasadDL/Healthcare_management-CRUD-operation"
            },
            {
                  "title":"Speech to Text",
                "path":"images/text.png",
                "github_url":"https://github.com/MahadevprasadDL/speech-to-text"
            },
            { 
                 "title":"User Greetings",
                "path":"images/user.png",
                "github_url":"https://github.com/MahadevprasadDL/User_Greetings"
            },
            { 
                 "title":"Code Editor Synchronisation",
                "path":"images/code.png",
                "github_url":"https://github.com/MahadevprasadDL/Code-Editor-Synchronisation"
            },
            

        ]
        return render (request, "projects.html", {"projects_shows": projects_shows})

def certificate(request):
     return render (request, "certificate.html")

def contact(request):
     return render (request, "contact.html")

def resume(request):
    resume_path="myapp/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)