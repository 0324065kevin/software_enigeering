from django.shortcuts import render ,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
import pandas as pd
import urllib.request
import json
from pandas.io.json import json_normalize
from .models import activity , Favorite
from venue.models import Venue
from django.db.models import Q
from datetime import datetime
from django.contrib.auth import authenticate, login


# Create your views here.

def getNewdataset(request):
    with urllib.request.urlopen(
            "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=6") as url:
        data_exhibition = json.loads(url.read().decode())
        data_exhibition = json_normalize(data_exhibition, 'showInfo',
                                         ['UID', 'title', 'category', 'showUnit', 'discountInfo',
                                          'descriptionFilterHtml', 'imageUrl', 'masterUnit', 'webSales',
                                          'sourceWebPromote', 'comment', 'editModifyDate'], record_prefix='Info_')
        print('exhibition', len(data_exhibition))
    with urllib.request.urlopen(
            "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=3") as url:
        data_dance = json.loads(url.read().decode())
        data_dance = json_normalize(data_dance, 'showInfo',
                                    ['UID', 'title', 'category', 'showUnit', 'discountInfo', 'descriptionFilterHtml',
                                     'imageUrl', 'masterUnit', 'webSales', 'sourceWebPromote', 'comment',
                                     'editModifyDate'], record_prefix='Info_')
        print('dance', len(data_dance))
    with urllib.request.urlopen(
            "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=1") as url:
        data_music = json.loads(url.read().decode())
        data_music = json_normalize(data_music, 'showInfo',
                                    ['UID', 'title', 'category', 'showUnit', 'discountInfo', 'descriptionFilterHtml',
                                     'imageUrl', 'masterUnit', 'webSales', 'sourceWebPromote', 'comment',
                                     'editModifyDate'], record_prefix='Info_')
        print('music', len(data_music))
    with urllib.request.urlopen(
            "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=7") as url:
        data_lecture = json.loads(url.read().decode())
        data_lecture = json_normalize(data_lecture, 'showInfo',
                                      ['UID', 'title', 'category', 'showUnit', 'discountInfo', 'descriptionFilterHtml',
                                       'imageUrl', 'masterUnit', 'webSales', 'sourceWebPromote', 'comment',
                                       'editModifyDate'], record_prefix='Info_')
        print('lecture', len(data_lecture))
    with urllib.request.urlopen(
            "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=4") as url:
        data_family = json.loads(url.read().decode())
        data_family = json_normalize(data_family, 'showInfo',
                                     ['UID', 'title', 'category', 'showUnit', 'discountInfo', 'descriptionFilterHtml',
                                      'imageUrl', 'masterUnit', 'webSales', 'sourceWebPromote', 'comment',
                                      'editModifyDate'], record_prefix='Info_')
        print('family', len(data_family))
    df = pd.concat([data_exhibition, data_dance, data_music, data_lecture, data_family], axis=0)
    print('----------------------')
    print('TOTAL:', len(data_exhibition) + len(data_dance) + len(data_music) + len(data_lecture) + len(data_family))
    # 將資料區分為venue and activity
    df = df.drop_duplicates(subset=['title'], keep="first")
    df = df.reset_index()
    del df['index']
    df.Info_endTime.astype('str')
    df.Info_time.astype('str')
    l = list(df['Info_time'])
    m = list(df['Info_endTime'])
    lis = []
    k = []
    n = []
    for i, j in zip(l, m):
        k.append(i[0:10])
        n.append(j[0:10])
        lis.append(i[0:10] + '~' + j[0:10])
    df['period'] = pd.Series(lis)
    df['Info_time'] = pd.Series(k)
    df['Info_endTime'] = pd.Series(n)

    venues = df[['title', 'Info_location', 'Info_locationName', 'Info_longitude', 'Info_latitude']]
    venues = venues.fillna('')
    lis = []
    for i in venues.Info_location:
        try:
            int(i[0])
            if i[5:8] == '台北市':
                lis.append('臺北市')
            else:
                lis.append(i[5:8])

        except ValueError:
            if i[0:3] == 'ssr':
                lis.append(' ')
            elif i[0:3] == 'm 2':
                lis.append(' ')
            elif i[0:3] == '台北市':
                lis.append('臺北市')
            else:
                lis.append(i[0:3])

        except IndexError:
            lis.append(' ')
    venues['city'] = lis

    df1 = df
    del df1['Info_location'], df1['Info_longitude'], df1['Info_latitude']
    activities = df1
    activities.Info_endTime = pd.to_datetime(df.Info_endTime)
    activities['city'] = lis
    activities.Info_time = pd.to_datetime(df.Info_time)
    activities['category'] = activities.category.replace({
        '1': '音樂',
        '3': '舞蹈',
        '4': '家庭',
        '6': '展覽',
        '7': '演講'
    })
    venues = venues.drop_duplicates(subset=['title'], keep="first")
    # 將資料寫進資料庫
    for venuee in venues.itertuples():
        try:
            venues = Venue.objects.get_or_create(
                                        location = venuee.Info_location ,
                                        locationName = venuee.Info_locationName,
                                        latitude = venuee.Info_latitude,
                                        longtitude = venuee.Info_longitude,
                                        city= venuee.city,
                                        )
        except:
            pass
    for activite in activities.itertuples():
        try:
            venuee = Venue.objects.get(locationName=activite.Info_locationName)
            activity.objects.get_or_create(endtime=activite.Info_endTime,
                                               onSales=activite.Info_onSales,
                                               price=activite.Info_price,
                                               title=activite.title,
                                               category=activite.category,
                                               ShowUnit=activite.showUnit,
                                               discontinfo=activite.discountInfo,
                                               descriptionFilterHtml=activite.descriptionFilterHtml,
                                               imageUrl=activite.imageUrl,
                                               masterUnit=activite.masterUnit,
                                               webSales=activite.webSales,
                                               sourceWebPromote=activite.sourceWebPromote,
                                               comment=activite.comment,
                                               time=activite.Info_time,
                                               editModifyDate=activite.editModifyDate,
                                               city = activite.city,
                                               period=activite.period,
                                               locationName=activite.Info_locationName,
                                               venue = venuee,
                                               )
        except:
            print('why??')





    return render(request,'data.html',locals())


# @csrf_protect
def getactivity(request):
    return render(request,'activitysearch.html',locals())

# @csrf_protect
def queryactivity(request):

    # print(1)
    activities = activity.objects.all()
    query1 = request.POST.get("q1")
    query2 = request.POST.get("q2")
    query3 = request.POST.get("q3")
    query4 = request.POST.get("q4")


    if query1:
        query2 = datetime.strptime(query2, '%Y-%m-%d').date()

        activities = activities.filter(
            Q(title__icontains=query1) &
            Q(time__lte=query2, endtime__gte=query2) &
            Q(city__icontains=query3) &
            Q(category__icontains=query4)).distinct()
    elif query2:
        query2 = datetime.strptime(query2, '%Y-%m-%d').date()

        activities = activities.filter(
            Q(title__icontains=query1) &
            Q(time__lte=query2, endtime__gte=query2) &
            Q(city__icontains=query3) &
            Q(category__icontains=query4)).distinct()
    elif query3:
        query2 = datetime.strptime(query2, '%Y-%m-%d').date()

        activities = activities.filter(
            Q(title__icontains=query1) &
            Q(time__lte=query2, endtime__gte=query2) &
            Q(city__icontains=query3) &
            Q(category__icontains=query4)).distinct()
    elif query4:
        query2 = datetime.strptime(query2, '%Y-%m-%d').date()

        activities = activities.filter(
            Q(title__icontains=query1) &
            Q(time__lte=query2, endtime__gte=query2) &
            Q(city__icontains=query3) &
            Q(category__icontains=query4)).distinct()

    return render(request, 'activitysearch.html', locals())

def activity_detail(request,id):
    activities = activity.objects.get(id=id)
    return render(request,'activitydetail.html',locals())

def favorite(request,id):
    print("views:")
    activities = activity.objects.get(id=id)
    print(id)
    print(request.user.id)
    print(activities)
    created = Favorite.objects.get_or_create(
        user=request.user,
        activity_fk=activities,
    )
    print(created[1])
    if created[1] == False:
        Favorite.objects.get(activity_fk=activities).delete()
        return JsonResponse({'success': '成功刪除'})
    return JsonResponse({'success':'成功新增'})


def delet_favorite(request,id):
    print(id)
    Favorite.objects.get(id=id).delete()
    return redirect('/myfavorite')

def collection(request):
    user = request.session['id']
    print(user)
    users =  User.objects.get(username = user)
    collect = Favorite.objects.filter(user = users)
    return render(request, 'myfavorite.html', locals())

def home(request):
    print('abc')
    activities = activity.objects.all()
    return render(request, 'index.html', locals())
