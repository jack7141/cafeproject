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
    UIparking = request.GET.get("inputPark", False)
    GetFromSearchBar = request.GET.get('InputCity', '검색결과없음')
    form = {'city':GetFromSearchBar, 'UIcafetype':UIcafetype, 'UIparking':UIparking}


    # DB에서 온 데이터
    cafetype = CafeType.objects.all()

    choices = {'cafetypes':cafetype }
    # ------------------------------------------------------------------------------------------------------------------
    # View: FrontEnd에서 가져온 데이터를 통해서 DB를 검색해서 필요한 데이터만 화면에 다시 Render
    # 검색조건을 통해서 내가 원하는 방을 띄워준다.
    # ------------------------------------------------------------------------------------------------------------------
    
    filterArgs = {}

    if UIparking != False:
        filterArgs['parkSite'] = True

    if UIcafetype != 0:
        # cafetype은 Cafe 클래스의 foreignKey!
        filterArgs['cafetype__id'] = UIcafetype

    cafes = Cafe.objects.filter(**filterArgs)

    return render(
        request,
        'cafes/search.html',
        # UI에서 지정한 값을 지워지지않고 Default로 올려두기로 위함
        # '*변수'일 경우는 인자의 갯수가 제한이 없다
        # '**변수'일 경우 딕셔너리형태의 데이터로 보낸다.
        {**form, **choices, 'cafes':cafes}
    )