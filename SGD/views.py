from django.shortcuts import render
from .models import Professor, CheckStudent
from django.contrib import messages
from django.db.models import Q
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from SGD.camera2 import FaceDetect

def index(request):

    return render(request, 'index.html')

def login(request):

    return render(request, 'login.html')

def log(request):
    pro_id = request.POST.get("id")
    professor = Professor.objects.filter(id = pro_id)
    if(professor.exists()):
        name = Professor.objects.get(id = pro_id).name
        context = {"professor": name}
        return render(request, 'index_log.html', context)
    
    messages.info(request, '아이디 다시 확인해주세요!')
    return render(request, 'login.html')

    # <!-- <button onclick="goBack()">로그아웃</button>
    # <script>
    #     function goBack() { window.history.back(-2); }
    # </script>
    # {% else %} -->
def logout(request):

    return render(request, 'index.html')


def attendance(request):
    students = CheckStudent.objects.order_by("-check_in_time")
    
    kw = request.GET.get("kw", '')
    if kw:
        students = students.filter(
            Q(check_name__icontains=kw) |   # 이름 검색
            Q(check_id__icontains=kw)       # 학번 검색
        ).distinct()
    context = {"students": students, 'kw': kw}
    
    # context = {"students": students}


    return render(request, "attendance.html", context)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@gzip.gzip_page
def detectme(request):
    return StreamingHttpResponse(gen(FaceDetect()), content_type="multipart/x-mixed-replace;boundary=frame")

def cam_1(request):

    return render(request, 'cam_1.html')

def cam_2(request):

    return render(request, 'cam_2.html')

def check(request):
    # students = CheckStudent.objects.order_by("-check_in_time")
    # context = {"students": students}

    students = CheckStudent.objects.get(check_name = "양성모")
    context = {"students": students}
    

    return render(request, "check.html", context)

def right(request):

    return render(request, 'right.html')
