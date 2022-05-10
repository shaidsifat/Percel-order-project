from django import forms  
from .models import createorder,createnewpercel,createcheckorder

class createnewpercelForm(forms.ModelForm):

    class Meta():
        model =  createnewpercel
        fields = "__all__"

class createorderForm(forms.ModelForm):

    class Meta():
        model = createorder
        fields = "__all__"
         #ields = ['pub_date', 'headline', 'content', 'reporter']


class createcheckorderForm(forms.ModelForm):

    class Meta():
        model = createcheckorder
        fields = ['product_divison','product_weight']