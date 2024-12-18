from django.shortcuts import render

from Examapp.models import Question
# Create your views here.

def starttest(request):
    
    subjectname=request.GET["subject"]
    request.session["subject"]=subjectname
    
    queryobj=Question.objects.filter(subject=subjectname)
    questionobj=queryobj[0]
    return render (request,'Examapp/questions.html', {"question": questionobj})

def nextQuestion(request):
    questionlist=Question.objects.filter(subject=request.session['subject'])
    if (request.session['qindex']<len(questionlist)-1):
        request.session['qindex']+=1
        questionobj=questionlist[request.session['qindex']]
        return render(request,'Examapp/questions.html',{'question':questionobj})
    else:
        return render(request,'Examapp/questions.html',{'question':questionlist[len(questionlist)-1]})


def prevQuestion(request):
    questionlist=Question.objects.filter(subject=request.session['subject'])
    if (request.session['qindex']>0):
        request.session['qindex']= request.session['qindex'] - 1
        questionobj=questionlist[request.session['qindex']]
        return render(request,'Examapp/questions.html',{'question':questionobj})
    else:
        return render(request,'Examapp/questions.html',{'question':questionlist[len(questionlist)-1]})

    