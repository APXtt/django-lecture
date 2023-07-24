from django.shortcuts import render, redirect
from .models import parentModel as pM, childModel as cM


def index(request):
    if request.method == 'POST':
        req = request.POST.copy()
        CRUDop = req.getlist('CRUDop')[0]
        MDop = req.getlist('MDop')[0]

        if MDop == 'pM':
            pMCRUD(CRUDop, req)
        elif MDop == 'cM':
            cMCRUD(CRUDop, req)

        return redirect('index')

    # pM = pM.objects.filter(id=1)  # 특정한 데이터를 찾을 때
    pD = pM.objects.all()  # 모든 데이터를 찾을 때
    cD = cM.objects.all()  # 모든 데이터를 찾을 때

    context = {'pM': pD,
               'cM': cD}
    return render(request, 'space1/index.html', context)


def pMCRUD(option, req):
    if option == 'Create':
        pM().save()

    elif option == 'Delete':
        target = req.getlist('target')[0]
        pM.objects.filter(id=target).delete()

    return redirect('index')


def cMCRUD(option, req):
    if option == 'Create':
        integer = int(req.getlist('Integer')[0])
        small_text = req.getlist('small_text')[0]
        large_text = req.getlist('large_text')[0]
        date = req.getlist('date')[0]
        foreign = req.getlist('foreign')[0]
        foreign = pM.objects.get(id=foreign)
        repair_state = req.getlist('repair_state')[0]

        cM(integer=integer, small_text=small_text, large_text=large_text,
           date=date, foreign=foreign, repair_state=repair_state).save()

    elif option == 'Update':
        target = req.getlist('target')[0]
        integer = int(req.getlist('Integer')[0])
        small_text = req.getlist('small_text')[0]
        large_text = req.getlist('large_text')[0]
        date = req.getlist('date')[0]
        foreign = req.getlist('foreign')[0]
        foreign = pM.objects.get(id=foreign)
        repair_state = req.getlist('repair_state')[0]

        obj = cM.objects.get(id=target)
        obj.integer = integer
        obj.small_text = small_text
        obj.large_text = large_text
        obj.date = date
        obj.foreign = foreign
        obj.repair_state = repair_state
        obj.save()

    elif option == 'Delete':
        target = req.getlist('target')[0]
        cM.objects.filter(id=target).delete()

    return redirect('index')
