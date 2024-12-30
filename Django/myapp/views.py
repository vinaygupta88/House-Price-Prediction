from django.shortcuts import render
import os
import pickle
# Create your views here.
def index(request):
    if request.method=='POST':
        MInc=float(request.POST['MInc'])
        HAge=float(request.POST['HAge'])
        room=float(request.POST['room'])
        bed=float(request.POST['bed'])
        popu=float(request.POST['popu'])
        Occ=float(request.POST['Occ'])
        lat=float(request.POST['lat'])
        Lon=float(request.POST['Lon'])
        path=os.path.dirname(__file__)
        model=pickle.load(open(os.path.join(path,'house.pkl'),'rb'))
        res=model.predict([[MInc,HAge,room,bed,popu,Occ,lat,Lon]])[0]
        return render(request,"index.html",{"res":res})
    return render(request,"index.html")