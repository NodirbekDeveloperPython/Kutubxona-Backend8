from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.
def sinashga(request):
    return  HttpResponse('Hello Wowrld!')

def bosh_sahifa(request):
    if request.user.is_authenticated:
        data = {
            'plans': Record.objects.all()
        }
    else:
        redirect('/bosh_sahifa/')
    return  render(request, 'index.html', data)

def salomlash(request):
    soz = request.GET.get('q_sozi')
    if soz is None:
        s = Student.objects.all()
    else:
            s = Student.objects.filter(ism__contains=soz)
    data = {
        'Studentlar': s,
        'ism': 'Nodirbek',
    }
    return render(request, 'mashq.html', data)

def mashqlar(request):
    data = {
        'talabalar' : Student.objects.filter(bitiruvchi=True)
    }
    return render(request, 'mashq/mashq2.html', data)

def mashqlar3(request):
    data = {
        'kitoblar': Student.objects.filter(kitob_soni__gt=0)
    }
    return render(request, 'mashq/mashq2.html', data)

def talaba(request, son):
    data = {
        "student": Student.objects.get(id=son)
    }
    return render(request, "mashq/student.html", data )

#Уйга вазифалар 1-вазифа
def mualliflar(request):
    data = {
        'mualliflar': Muallif.objects.all()
    }
    return render(request, 'homework/muallif_1.html', data)


# vazifa 2
def muallif(request, son):
    data = {
        'muallif': Muallif.objects.get(id=son)
    }
    return render(request, 'homework/muallif_2.html',data)

# vazifa 3
def kitoblar_3(request):
    data = {
        'kitobla': Kitob.objects.all()
    }
    return render(request, 'homework/kitob_3.html', data)

# Vazifa 4
def kitob_haqida(request,son):
    data = {
        'kitob': Kitob.objects.get(id=son)
    }
    return render(request, 'homework/kitob_4.html', data)

#Vazifa 5
def recordlar(request):
    data = {
        'recordlar': Record.objects.all()
    }
    return render(request, 'homework/record5.html', data)

#vazifa 6
def Tmualliflar(request):
    data = {
        'mualliflar': Muallif.objects.filter(tirik=True)
    }
    return render(request, 'homework/muallif_6.html', data)


#vazifa 7
def hamma_kitoblar(request):
    data = {
        'kitoblar' : Kitob.objects.order_by('-sahifa')[:3]
    }
    return render(request, 'homework/kitob7.html', data)


#Vazifa 8
def kitobi_kop_muallif(request):
    data = {
        'mualliflar': Muallif.objects.order_by('-kitob_soni')[:3]
    }
    return  render(request, 'homework/muallif8.html', data)


# Vazifa 9
def oxirgi_recordlar(request):
    data = {
        'recordlar': Record.objects.order_by('-olingan_sana')[:3]
    }
    return render(request, 'homework/record9.html', data)

# Vazifa 10
def tirik_muallif_kitobi(request):
    data = {
        'Kitoblar': Kitob.objects.filter(muallif__tirik=True)
    }
    return render(request, 'homework/muallif10.html', data)

#Vazifa 11
def badiiy_kitoblar(request):
    data = {
        'kitoblar': Kitob.objects.filter(janr="Badiiy")
    }
    return render(request, 'homework/kitob11.html',data)

# Vazifa 12
def Astudent(request):
    data = {
        'studentlar': Student.objects.filter(ism__contains="a")
    }
    return render(request, 'homework/student12.html',data)

# Vazifa 13
def yoshi_katta_mualliflar(request):
    data = {
        'mualliflar': Muallif.objects.order_by('tugilgan_yil')[:3]
    }
    return render(request, 'homework/muallif13.html', data)


#Vazifa 14
def kop_kitobli_mualliflar(request):
    data = {
        'kitoblar': Kitob.objects.filter(muallif__kitob_soni__lt=10)
    }
    return render(request, 'homework/muallif14.html', data)

#Vazifa 15
def Erkak_studentlar(request):
    data = {
        'studentlar': Student.objects.filter(jins="Erkak")
    }
    return render(request, 'homework/student15.html', data)

# Vazifa 16
def batafsil_record(request,son):
    data = {
        'record': Record.objects.get(id=son),
        'bool': Record.objects.get(id=son).qaytardi
    }
    return render(request, 'homework/record16.html', data)

# Vazifa 17
def bitiruvchi_studentlar_recordlari(request):
    data = {
        'recordlar':  Record.objects.filter(student__bitiruvchi=True)
    }
    return render(request, 'homework/student17.html', data)







#2-dars
# def barcha_talabalar(request):
#     soz = request.GET.get('q_sozi')
#     if soz is None:
#         s = Student.objects.all()
#     else:
#         s = Student.objects.filter(ism__contains=soz)
#     data = {
#         "students": s
#     }
#     return render(request, '2Dars/students.html', data)




def barcha_talabalar(request):
    if request.method == "POST":
        if request.POST.get('bt') == "on":
            natija = True
        else:
            natija = False
        Student.objects.create(
            ism = request.POST.get('name'),
            jins = request.POST.get('gender'),
            kitob_soni = request.POST.get('books'),
            bitiruvchi = natija
        )
        return redirect('/talabalar/')
    soz = request.GET.get('q_sozi')
    if soz is None:
        s = Student.objects.all()
    else:
        s = Student.objects.filter(ism__contains=soz)
    data = {
        "students": s
    }
    return render(request, '2Dars/students.html', data)


def talaba_ochir(request,son):
    Student.objects.get(id=son).delete()
    return redirect('/talabalar/')

def talaba_qidirish(request):
    Student.objects.filter(ism__contains="harf")
    return redirect('/talabalar/')

def kitoblar(request):
    if request.method == "POST":
        Kitob.objects.create(
            nom = request.POST.get('nomi'),
            sahifa = request.POST.get('sahifasi'),
            janr = request.POST.get('janri'),
            muallif = Muallif.objects.get(id = request.POST.get('muallifi')),
        )
        return  redirect('/kitoblar/')
    data = {
        'mualliflar': Muallif.objects.all(),
        'kitoblar': Kitob.objects.all()
    }
    return render(request, 'kitoblar.html', data)

def kitob_ochir(request,son):
    Kitob.objects.get(id=son).delete()
    return redirect('/kitoblar/')

#2 dars Homework
# 1-mashq
def barcha_recordlar(request):
    ism = request.GET.get('ism')
    if ism is None:
        s = Record.objects.all()
    else:
        s = Record.objects.filter(student__ism__contains=ism)
    data = {
        'recordlar': s
    }
    return render(request, '2Dars/record1.html/', data)

#2-mash1
def barcha_mualliflar2(request):
    data = {
        'mualliflar': Muallif.objects.all()
    }
    return render(request, '2Dars/mualliflar2.html',data)


# 2-Mashq
def muallif_ochir(request,son):
    Muallif.objects.get(id=son).delete()
    return redirect('/mualliflar2/')

#3-mashq
def hamma_recordlar3(request):
    data = {
        'recordlar': Record.objects.all()
    }
    return render(request, '2Dars/record3.html', data)


def record_ochir3(request,son):
    Record.objects.get(id=son).delete()
    return redirect('/recordlar3/')

#4 - Mashq
def hamma_mualliflar4(request):
    ism = request.GET.get('soz')
    if ism is None:
        s = Muallif.objects.all()
    else:
        s = Muallif.objects.filter(ism__contains=ism)
    data = {
        'mualliflar': s
    }
    return render(request, '2Dars/muallif4.html', data)




#3-Dars  mashqlar

def all_students(request):
    if request.method == "POST":
        if request.POST.get('bt') == "on":
            natija = True
        else:
            natija = False
        Student.objects.create(
            ism = request.POST.get('name'),
            jins = request.POST.get('gender'),
            kitob_soni = request.POST.get('books'),
            bitiruvchi = natija
        )
        return redirect('/students/')
    soz = request.GET.get('q_sozi')
    if soz is None:
        s = Student.objects.all()
    else:
        s = Student.objects.filter(ism__contains=soz)
    data = {
        'students': s
    }
    return render(request, '3Dars/students4.html', data)

def talaba_haqida(request,son):
    data = {
        "student": Student.objects.get(id=son)
    }
    return render(request, '3Dars/batafsil_student4.html', data)

def student_ochir(request,son):
    Student.objects.get(id=son).delete()
    return redirect('/students/')


#kitoblar haqida

def kitoblar4(request):
    if request.method == "POST":
        Kitob.objects.create(
            nom = request.POST.get('nom'),
            sahifa = request.POST.get('sahifa'),
            janr = request.POST.get('nom'),
            muallif = Muallif.objects.get(id = request.POST.get('muallif'))
        )
        return redirect("/kitoblar4/")
    data = {
        'mualliflar': Muallif.objects.all(),
        'kitoblar': Kitob.objects.all()
    }
    return render(request, '3Dars/kitoblar4.html', data)

def kitob_h4(reuqest,son):
    data = {
        'kitob': Kitob.objects.get(id=son)
    }
    return render(request, '3Dars/batafsil_kitob4.html', data)

#3dars Vazifa 1
def mualliflar4(request):
    if request.method == "POST":
        if request.POST.get('tirik') == "on":
            natija =True
        else:
            natija = False
        Muallif.objects.create(
            ism = request.POST.get('ismi'),
            tirik = natija,
            kitob_soni = request.POST.get('kitobi'),
            tugilgan_yil = request.POST.get('t_yil'),
        )
        return redirect('/mualliflar4_1/')
    data = {
        'mualliflar': Muallif.objects.all()
    }
    return  render(request,'3Dars/mualliflar4.html',data)

def mualliflar41(request, son):
    Muallif.objects.get(id=son).delete()
    return redirect('/mualliflar4_1/')



#Vazifa 2
def recordlar2(request):
    if request.method == "POST":
        if request.POST.get("bt") == "on":
            natija = True
        else:
            natija = False
        Record.objects.create(
            student = Student.objects.get(id = request.POST.get('students')),
            kitob = Kitob.objects.get(id= request.POST.get('books')),
            olingan_sana = request.POST.get("o_sana"),
            qaytardi = natija,
        )
    data = {
        "kitoblar": Kitob.objects.all(),
        "studentlar": Student.objects.all(),
        "recordlar": Record.objects.all(),
    }
    return render(request, '3Dars/recordlar5.html',data)


def batafsil_record2(request,son):
    data = {
        "record": Record.objects.get(id=son)
    }
    return render(request, '3Dars/b_record.html', data)



# 4-DARS MASHQ 1
def studentlar4(request):
    if request.method == "POST":

        f = StudentForm(request.POST)

        if f.is_valid():
            Student.objects.create(
                ism = f.cleaned_data.get('i'),
                jins = f.cleaned_data.get('j'),
                kitob_soni = f.cleaned_data.get('kitoblari_soni'),
                bitiruvchi = f.cleaned_data.get('bitiruvchi'),
            )
        return redirect('/studentlar4/')

    data = {
        "students": Student.objects.all(),
        "forma": StudentForm
    }
    return render(request, '4Dars/students.html', data)

def talaba4_ochir(request,son):
    data = {
        "student": Student.objects.get(id=son).delete()
    }
    return redirect('/studentlar4/')

def student_tahrirlash(request, son):
    if request.method == "POST":
        if request.POST.get('bitiradi') == "on":
            natija = True
        else:
            natija = False
        Student.objects.filter(id=son).update(
            ism = request.POST.get('ismi'),
            bitiruvchi = natija,
            kitob_soni = request.POST.get('k_soni')
        )
        return redirect('/studentlar4/')
    data = {
        "student": Student.objects.get(id=son)
    }
    return render(request,'4Dars/student_edit.html', data)


def talaba_tasdiqlash(reuqest, son):
    data = {
        "talaba": Student.objects.get(id=son)
    }
    return render(reuqest, '4Dars/talaba_ochir.html',data)


#2-mashq
def mualliflar44(request):
    data = {
        'mualliflar': Muallif.objects.all()
    }
    return render(request, '4Dars/mualliflar44.html', data)

def mualliflar_edit(request, son):
    data = {
        'muallif':Muallif.objects.get(id=son)
    }
    return render(request, '4Dars/muallif_edit.html', data)



# 4-Dars homework

def mualliflar_home1(request):
    soz = request.GET.get('q_soz')
    if soz is None:
        m = Muallif.objects.all()
    else:
        m = Muallif.objects.filter(ism__contains=soz)
    data = {
        'mualliflar': m
        }
    return render(request, '4Dars/muallif/mualliflar.html', data)

def mualliflar_home1_b(request,son):
    data = {
        'muallif': Muallif.objects.get(id=son)
    }
    return render(request, '4Dars/muallif/batafsil.html', data)

def muallif_home_edit(request,son):
    if request.method == "POST":
        if request.POST.get('bt') is None:
            n = False
        else:
            n = True
        Muallif.objects.filter(id=son).update(
            ism = request.POST.get('ism'),
            tirik = n,
            kitob_soni = request.POST.get('k_soni'),
            tugilgan_yil = request.POST.get('t_yil'),
        )
        return redirect('/mualliflar_home1/')
    data = {
        'muallif': Muallif.objects.get(id=son)
    }
    return render(request, '4Dars/muallif/muallif_edit.html', data)

#4-Dars homework 2
def recordlar_home1(request):
    data = {
        'recordlar': Record.objects.all()
    }
    return render(request, '4Dars/record/recordlar_home.html', data)

def record_home_edit(request, son):
    data = {
        'record': Record.objects.get(id=son)
    }
    return render(request, '4Dars/record/record_edit.html', data)

def record_delete1(request,son):
    Record.objects.get(id=son).delete()
    return redirect('/recordlar_home1/')





#4-Dars 6-Mashq
def muallif_home_delete(request,son):
    data = {
        'muallif': Muallif.objects.get(id=son)
    }
    return render(request, '4Dars/muallif/muallif_delete.html', data)

def muallif_delete1(request,son):
    Muallif.objects.get(id=son).delete()
    return redirect('/mualliflar_home1/')





# 7-Mashq
def kitoblar_home1(request):
    if request.method == "POST":
        forma = KitobForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect('/kitoblar_home1/')
    data = {
        'kitoblar': Kitob.objects.all(),
        'forma': KitobForm
    }
    return render(request, '4Dars/kitob/kitoblar.html', data)

def kitoblar_tas1(request, son):
    data = {
        'kitob': Kitob.objects.get(id=son)
    }
    return render(request, '4Dars/kitob/kitob_tas.html', data)
def kitob_sure_delete(request, son):
    Kitob.objects.get(id=son).delete()
    return redirect('/kitoblar_home1/')




# 8-Mashq
def record_home_delete(request, son):
    data = {
        'record': Record.objects.get(id=son)
    }
    return render(request, '4Dars/record/record_delete.html', data)

def record_sure_delete(request,son):
    Record.objects.get(id=son).delete()
    return redirect('/recordlar_home1/')


#5Dars 1-mashq
def barcha_mualliflar(request):
    data = {
        'mualliflar': Muallif.objects.all()
    }
    return render(request, '5Dars/muallif/mualliflar.html', data)

def muallif_del_sure(request, son):
    data = {
        'muallif': Muallif.objects.get(id=son)
    }
    return render(request, '5Dars/muallif/muallif_del.html', data)


def muallif_delete(request,son):
    Muallif.objects.get(id=son).delete()
    return redirect('/barcha_mualliflar/')

def muallif_full(request,son):
    data = {
        'muallif': Muallif.objects.get(id=son)
    }
    return render(request, '5Dars/muallif/muallif_full.html', data)

def muallif_edit(request,son):
    if request.method == "POST":
        if request.POST.get('tirik') == "on":
            n = True
        else:
            n = False
        Muallif.objects.filter(id=son).update(
            ism=request.POST.get('ism'),
            tirik=n,
            kitob_soni=request.POST.get('k_soni'),
            tugilgan_yil=request.POST.get('t_yil'),
        )
        return redirect('/barcha_mualliflar/')
    data = {
        'muallif': Muallif.objects.get(id=son)
    }
    return render(request, '5Dars//muallif/muallif_edit.html', data)


#5Dars 2-mashq
def barcha_recordlar_home(request):
    form = RecordForm(request.POST)
    if form.is_valid():
        Record.objects.create(
            student = form.cleaned_data.get('student'),
            kitob = form.cleaned_data.get('kitob'),
            olingan_sana = form.cleaned_data.get('olingan_sana'),
            qaytardi = form.cleaned_data.get('qaytardi'),
            qaytargan_sana = form.cleaned_data.get('qaytargan_sana'),
        )
    data = {
        'recordlar': Record.objects.all(),
        'forma': RecordForm()
    }
    return render(request, '5Dars/record/recordlar.html', data)



def kutubxona_loginView(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('l'),
                            password=request.POST.get('p'))
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/bosh_sahifa/')
    return render(request, 'login_kutubxona.html')

def kutubxona_logoutView(request):
    logout(request)
    return redirect('/')



def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p')
            )
        return redirect('/')
    return render(request, 'register.html')