from django.shortcuts import render,redirect
import os
from django.conf import settings
from django.http import HttpResponse
import pandas as pd
from dashboard import comp_code


def download(request):

    
    name = request.session.get('game')
    name2 = request.session.get('came')
    C = request.session.get('stay')
    D = request.session.get ('hay')

    if request.method == 'POST':
        dat = request.POST
        action = dat.get("down")
        if action == "download":
            file_path = os.path.join(settings.MEDIA_ROOT, name)
            if os.path.exists(file_path):
                with open(file_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        if action == "download2":
            file_path = os.path.join(settings.MEDIA_ROOT, name2)
            if os.path.exists(file_path):
                with open(file_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
    return render(request, "dash/result.html", {"first":C, "second":D})


def result_view(request):

    if request.method == 'POST':
        
        file1=request.FILES['file_one']
        file2=request.FILES['file_two']

        data = request.POST
        action = data.get("criteria")
        decision = data.get("download")
        compare = data.get("compare")

        name = 'excel/comp_{}'.format(file1)
        name2 = 'excel/comp_{}'.format(file2)

        fileA = pd.read_excel(file1)
        fileB = pd.read_excel(file2)
        fileI = pd.read_excel(file1)
        fileII = pd.read_excel(file2) 

        if action == "highlight":
            ask = "not"
            fileA,fileB = comp_code.high(fileA,fileB, ask),comp_code.high(fileII,fileI, ask)
        
            A = fileA.style.applymap(comp_code.highlight_cells)
            B = fileB.style.applymap(comp_code.highlight_cells)
    
            A = comp_code.color(A)
            B = comp_code.color(B)

            C = A.to_html(index=False)
            D = B.to_html(index=False)
            
            A.to_excel('media/excel/comp_{}'.format(file1),index = False, header = True, engine = 'openpyxl')
            B.to_excel('media/excel/comp_{}'.format(file2),index = False, header = True, engine = 'openpyxl')

            request.session['game'] = name
            request.session['came'] = name2
            request.session['stay'] = C
            request.session['hay'] = D

            return redirect("result")

        if decision == 'merge':
            ask = "merge"
            fileA = comp_code.high(fileA,fileB, ask)
        
            A = fileA.style.applymap(comp_code.highlight_cells)
    
            A = comp_code.color(A)
            C = A.to_html(index=False)

            A.to_excel('media/excel/comp_{}'.format(file1),index = False, header = True, engine = 'openpyxl')
            
            request.session['game'] = name
            request.session['stay'] = C

            return redirect("result")

        elif action == "remove":
            fileA,fileB = comp_code.rem(fileA,fileB),comp_code.rem(fileII,fileI)
        
            A = fileA.style.applymap(comp_code.highlight_cells)
            B = fileB.style.applymap(comp_code.highlight_cells)

            A = comp_code.color(A)
            B = comp_code.color(B)
    
            C = A.to_html(index=False)
            D = B.to_html(index=False)
            
            A.to_excel('media/excel/comp_{}'.format(file1),index = False, header = True, engine = 'openpyxl')
            B.to_excel('media/excel/comp_{}'.format(file2),index = False, header = True, engine = 'openpyxl')

            request.session['game'] = name
            request.session['came'] = name2
            request.session['stay'] = C
            request.session['hay'] = D

            return redirect("result")

    return render(request, "index.html")
    


    
    
        
        
        
        
        
