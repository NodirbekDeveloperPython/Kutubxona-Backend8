from django import forms
from django.core.exceptions import ValidationError
from .models import Kitob
from .models import Record

class StudentForm(forms.Form):
    i = forms.CharField(label="Ism")
    j= forms.CharField(label="Jins")
    bitiruvchi = forms.BooleanField()
    kitoblari_soni = forms.IntegerField()

    def clean_i(self):
        qiymat = self.cleaned_data.get('i')

        if not qiymat.endswith('jon') and not qiymat.endswith('bek'):
            raise ValidationError("Ism o'zbekcha emas!")
        return qiymat


    def clean_kitoblari_soni (self):
        qiymat = self.clean_data.get('kitoblari_soni')
        if qiymat > 0 or qiymat < 5:
            return qiymat
        raise ValidationError("Xato oraliq kiritildi.")


class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = ('nom', 'sahifa', 'janr', 'muallif')

class MuallifForm(forms.Form):
    ism = forms.CharField(label='Ismi')
    tirik = forms.BooleanField(label='Tirikligi')
    kitob_soni = forms.IntegerField( max_value=6, min_value=0, label='Kitob soni')
    tugilgan_yil = forms.DateField()

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'