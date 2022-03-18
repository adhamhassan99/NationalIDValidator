
from datetime import datetime
from rest_framework.response import Response
import json
from rest_framework.decorators import api_view




governorates = {'01': 'Cairo',
                '02': 'Alexandria',
                '03': 'Port Said',
                '04': 'Suez',
                '11': 'Damietta',
                '12': 'Dakahlia',
                '13': 'Ash Sharqia',
                '14': 'Kaliobeya',
                '15': 'Kafr El - Sheikh',
                '16': 'Gharbia',
                '17': 'Monoufia',
                '18': 'El Beheira',
                '19': 'Ismailia',
                '21': 'Giza',
                '22': 'Beni Suef',
                '23': 'Fayoum',
                '24': 'El Menia',
                '25': 'Assiut',
                '26': 'Sohag',
                '27': 'Qena',
                '28': 'Aswan',
                '29': 'Luxor',
                '31': 'Red Sea',
                '32': 'New Valley',
                '33': 'Matrouh',
                '34': 'North Sinai',
                '35': 'South Sinai',
                '88': 'Foreign'}


@api_view(['POST'])
def ValidateId(request):
    ID=(json.loads(request.body))["ID"]
    if len(str(ID))!=14 or type(ID)==str:
        return Response("ID IS INVALID. PLEASE ENTER A VALID ID")
    ID=str(ID)
    userInfo={}
    userInfo["Gender"]=getGender(ID)
    userInfo["Birth_Place"]=governorates[ID[7:9]]
    userInfo["Birth_Date"]=getBirthDate(ID)

    return Response(userInfo)

def getBirthDate(id:str):
    BirthDate=f'{getBirthYear(id)}-{id[3:5]}-{id[5:7]}'
    return BirthDate
    

def getBirthYear(id:str):
    year=((int(id[0])+18)*100)-100
    year+=int(id[1:3])
    return year

def getGender(id:str):
    if int(id[12])%2==0:
        return "Female"
    return "Male"