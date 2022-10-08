"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('kitoblar/', kitoblar),

    path('admin/', admin.site.urls),
    path('sinashga/', sinashga),
    path('bosh_sahifa/', bosh_sahifa),
    path('salom/', salomlash),
    path('Student2/', mashqlar),
    path('Student3/', mashqlar3),
    path('talaba/<int:son>',talaba),
    #Vazifalar
    path('mualliflar/', mualliflar),
    path('muallif/<int:son>/', muallif),
    path('kitoblar_3/', kitoblar_3),
    path('kitob_4/<int:son>/', kitob_haqida),
    path('record_5/', recordlar),
    path('muallif6/', Tmualliflar),
    path('kitoblar7/', hamma_kitoblar),
    path('maxMuallif8/', kitobi_kop_muallif),
    path('recordlar9/', oxirgi_recordlar),
    path('muallif10/', tirik_muallif_kitobi),
    path('kitob11/', badiiy_kitoblar),
    path('student12/', Astudent),
    path('muallif13/', yoshi_katta_mualliflar),
    path('muallif14/', kop_kitobli_mualliflar),
    path('student15/', Erkak_studentlar),
    path('record16/<int:son>/',batafsil_record),
    path('student17', bitiruvchi_studentlar_recordlari),





    #2-Dars
    path('talabalar/', barcha_talabalar),


    path('talaba_ochir/<int:son>/', talaba_ochir),

    path('kitoblar/', kitoblar),
    path('kitob_ochir/<int:son>/', kitob_ochir),

    # 2Dars Homework
    path('recordlar1/', barcha_recordlar),

    path('mualliflar2/', barcha_mualliflar2),

    path('muallif_ochir/<int:son>/', muallif_ochir),

    path('recordlar3/', hamma_recordlar3),
    path('record_ochir3/<int:son>/', record_ochir3),

    path('mualliflar4/', hamma_mualliflar4),

    #3-Dars mashqlar
    path('students/', all_students),
    path('talabaa/<int:son>/', talaba_haqida),
    path('student4_delete/<int:son>/', student_ochir),

    path('kitoblar4/', kitoblar4),
    path('/kitob_id/<int:son>/', kitob_h4),

    #Vazifa 1
    path('mualliflar4_1/', mualliflar4),
    path('/m4_del/<int:son>/', mualliflar41),

    #Vazifa 2
    path('recordlar2/', recordlar2),
    path('/records/<int:son>/', batafsil_record2),


    #4-dars mashq1
    path('studentlar4/', studentlar4),
    path('talaba4_ochir/<int:son>/', talaba4_ochir),
    path('talaba_edit/<int:son>/', student_tahrirlash),
    path('talaba_tas/<int:son>/', talaba_tasdiqlash),


    #mashq2
    path('mualliflar44/', mualliflar44),
    path('muallif_edit/<int:son>', mualliflar_edit),

    #4-Dars homeworks 1
    path('mualliflar_home1/', mualliflar_home1),
    path('mualliflar_home1_b/<int:son>/', mualliflar_home1_b),
    path('muallif_home_edit/<int:son>/', muallif_home_edit),

    #4-Dars homework 2
    path('recordlar_home1/', recordlar_home1),
    path('record_home_edit/<int:son>/', record_home_edit),
    path('record_delete1', record_delete1),



    # 6-mashq
    path('muallif_home_delete/<int:son>/', muallif_home_delete),
    path('muallif_delete1/<int:son>/',muallif_delete1),

    # 7-mashq

    path('kitoblar_home1/', kitoblar_home1),
    path('kitoblar_tas1/<int:son>/', kitoblar_tas1),
    path('kitob_sure_delete/<int:son>/', kitob_sure_delete),

    #8-mashq
    path('record_home_delete/<int:son>/', record_home_delete),
    path('record_sure_delete/<int:son>/', record_sure_delete),


    # 5-Dars 1-mashq
    path('barcha_mualliflar/', barcha_mualliflar),
    path('muallif_del_sure/<int:son>/', muallif_del_sure),
    path('muallif_delete/<int:son>/', muallif_delete),
    path('muallif_full/<int:son>/', muallif_full),
    path('muallif_edit/<int:son>/', muallif_edit),

    #5-Dars 2-mashq
    path('barcha_recordlar_home/', barcha_recordlar_home),

    path('', kutubxona_loginView),

    path('register/', register),
]
