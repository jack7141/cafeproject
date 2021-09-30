from django import forms
from cafes.models import Cafe, CafeType
from ConsVar import ConstVar
# View단에서 처리할 Form의 형식을 만들어줌
class SearchForm(forms.Form):

    # 지역
    city = forms.ChoiceField(required=False, choices=ConstVar.COUNTRY_CHOICES, label='지역')

    # 카페종류
    cafetypes = forms.ModelChoiceField(required=False, queryset=CafeType.objects.all(), label='카페종류')

    # 주차시설
    parking = forms.BooleanField(required=False, label='주차시설')
    
    # 지역마다 표시되는 항목 따르게 처리해야함     


