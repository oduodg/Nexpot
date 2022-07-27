from django.shortcuts import render
from django.http import HttpResponse
from .models import Youtube,Places  # youtube 모델 불러오기
from django.views.generic import ListView

import json
# Create your views here.
def youtube_view(request):
    youtubes = Youtube.objects.all() # youtube 테이블의 모든 객체 불러와서 변수에 저장
    return render(request, 'template.html',{"youtubes" : youtubes})

def index(request):
    latest_video_list = Youtube.objects[:5]
    output = ', '.join([q for q in latest_video_list])
    return HttpResponse(output)

class Youtube_information(ListView):
    model = Youtube
    template_name = '../templates/template.html'
    context_object_name = 'youtube_info'
'''
class Youtube_information(ListView):
    vois = [] # youtubeVO class 배열

    youtubes = Youtube.objects.all()
    vos = youtubes
    for youtube in vos :
        # vos에 youtube 객체를 담고, pname을 검색해서 queryset 추가한다.
        places = Places.objects.filter(videoid=youtube.videoid).select_related()
        dic = {
            'youtube' : youtube,
            'places' : places,
        }
        vois.append(dic)

        
        # youtube["places"] = places
        # print('video id : ', youtube.videoid) 
        # print('title : ', youtube.title) 
        # print('places : ',   youtube.places)
        # print()

    model = Youtube
    template_name = '../templates/template.html'
    context_object_name = 'youtube_info'
    # place = Youtube.objects.select_related('videoID')

    # return HttpResponse(json.dumps(dic))


def YoutubeFunction(request):
    vois = [] # youtubeVO class 배열

    youtubes = Youtube.objects.all()
    vos = youtubes
    for youtube in vos :
        # vos에 youtube 객체를 담고, pname을 검색해서 queryset 추가한다.
        places = Places.objects.filter(videoid=youtube.videoid).select_related()
        ps = ''
        if len(places) != 0 :
            ps = str(places[0])  
        dic = {
            'title' : youtube.title,
            'channelname' : youtube.channelname,
            'pname' : ps,
        }
        vois.append(dic)

        
        # youtube["places"] = places
        # print('video id : ', youtube.videoid) 
        # print('title : ', youtube.title) 
        # print('places : ',   youtube.places)
        # print()

    model = Youtube
    template_name = '../templates/template.html'
    context_object_name = 'youtube_info'
    # place = Youtube.objects.select_related('videoID')

    return HttpResponse(json.dumps(vois))

'''
