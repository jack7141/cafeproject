from django.shortcuts import render
from cafes.models import Cafe
from django.views.generic import ListView


class HomeView(ListView):
    '''
    * 함수 사용시 render를 이용
    allCafeData = Cafe.objects.all()
    return render(request, "cafes/cafe_list.html", {'cafes' : allCafeData})
    '''
    model = Cafe
    paginate_by = 10
    paginate_orphans = 5
    ordering = 'created'
    # 기존 Html로 넘어가는 context의 이름을 변경함 object_list -> cafes
    context_object_name = 'cafes'



def CafeDetail(request, id):
    return render(request, "cafes/detail.html")