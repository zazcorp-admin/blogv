from django.shortcuts import render
from .models import Blog, VisitorsIp
from django.db.models import Q



def index(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'core/index.html', context)


def contents(request, pk):
    blogs = Blog.objects.get(id=pk)

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip =  get_ip(request)
    vi = VisitorsIp(ip=ip)
    print(ip)  # for check if its really get it or not
    result = VisitorsIp.objects.filter(Q(ip__contains = ip))
    if len(result) == 1:
        print('exists')
    elif len(result) > 1:
        print('exists')
    else:
        vi.save()
        print('unique')
    count = VisitorsIp.objects.all().count()
    print(count)
    context = {
        'blogs': blogs,
        'count' : count
    }
    return render(request, 'core/body.html', context)