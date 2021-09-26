from django.shortcuts import render
from cafes.models import Cafe, CafeType
from django.views.generic import ListView, DetailView


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


class CafeDetail(DetailView):
    model = Cafe
    # 기본적으로 DetailView가 pk로 지정이 되어있기 때문에 내가 커스텀하려면
    # 아래의 옵션 사용해야함.
    pk_url_kwarg = 'id'


def search(request):
    # HTML Tag에서 name으로 검색, 없으면 Default로 '검색결과없음'을 띄움
    # HTML에서 가져온 데이터를 담아두려고 처리함

    # FrontUI
    UIcafetype = int(request.GET.get('cafetype',0))
    GetFromSearchBar = request.GET.get('InputCity', '검색결과없음')
    form = {'city':GetFromSearchBar, 'UIcafetype':UIcafetype}

    # DB에서 온 데이터
    cafetype = CafeType.objects.all()
    choices = {'cafetypes':cafetype}

    return render(
        request,
        'cafes/search.html',
        # UI에서 지정한 값을 지워지지않고 Default로 올려두기로 위함
        {**form, **choices}
    )