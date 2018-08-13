from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


# def login(request,nid):
#     print(nid)
#     return HttpResponse("Login")
# def login2(request,p1,x1):
#     print(p1,x1)
#     return HttpResponse("Login2")
USER_LIST = []
for item in range(94):
    temp = {'id':item,'username':'alex'+str(item),'email':'email'+str(item)}
    USER_LIST.append(temp)



def index(request, page):
    print(page) #1.0-9  2.10-19 3.20-29
    page = int(page)
    start = (page-1)*10
    end = page*10
    user_list = USER_LIST[start:end]
    return render(request,'index.html',{'user_list':user_list})


def detail(request,nid):
    nid = int(nid)
    current_detail = USER_LIST[nid]     #current_detail列表中的一个元素，数据类型为字典
    return render(request,'detail.html',{'current_detail':current_detail})


def template(request):
    return render(request,
                  'template.html',
                  {'k1':'v1','k2':[11,22,33,44,]}
                  )