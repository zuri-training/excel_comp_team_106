import os
from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import pandas as pd
from dashboard import comp_code



@login_required
def result_view(request):

    if request.method == 'POST':
        
        file1=request.FILES['file_one']
        file2=request.FILES['file_two']

        data = request.POST
        action = data.get("criteria")

        #getting the names of the uploaded files into variables
        name = '{}'.format(file1)
        name2 = '{}'.format(file2)
        #assigning two seperate instances to both files
        fileA = pd.read_excel(file1)
        fileB = pd.read_excel(file2)
        fileI = pd.read_excel(file1)
        fileII = pd.read_excel(file2) 

        #logic to sort through each cell in both files appending the duplicate cells and different cells
        # into respective lists so as to count the
        #number of duplicates and differences present
        f,z=[],[]
        for i, j in zip(fileA,fileB):
            a,b = 0,0
            a,b = [],[]
            for m,n in zip(fileA[i],fileB[j]):
                a.append(m)
                b.append(n)
            for m,n in zip(range(len(a)),range(len(b))):
                #list for differnces
                if a[m] != b[n]:
                    z.append(a[m])
                #list for duplicates
                if a[m] == b[n]:
                    f.append(a[m])
        #assigning the length of each list ino a variable as tuples        
        number = len(z), len(f)
        #getting the variable as json to be transferred into another view
        request.session['num'] = number

        if action == "highlight":
            #the value for the flag "ask"
            ask = "not"
            #assigning seperate instances of the respective files to variables fileA and fileB so
            #as to prevent fileB from working on data fileA has already processed through the imported "high" function
            fileA,fileB = comp_code.high(fileA,fileB, ask),comp_code.high(fileII,fileI, ask)
            #applying the data into the pandas style method to get highlight and reassigning them to variables A and B
            A = fileA.style.applymap(comp_code.highlight_cells)
            B = fileB.style.applymap(comp_code.highlight_cells)
            #passing the variable into an imported function that will style them for html viewing
            A = comp_code.color(A)
            B = comp_code.color(B)
            #turning the dataframe to html with a new set of variable names 
            #so as to be able to preserve the data as dataframes in the old variables
            C = A.to_html(index=False)
            D = B.to_html(index=False)
            #obtaining the cells with differences so as to properly make comments on the changes 
            #across both files
            z=[]
            for i, j in zip(fileA,fileB):
                 a,b = 0,0
                 a,b = [],[]
                 for m,n in zip(fileA[i],fileB[j]):
                    a.append(m)
                    b.append(n)
                 for m,n in zip(range(len(a)),range(len(b))):
                    if a[m] != b[n]:
                        #creating a list with formatted analysis
                        z.append("Value in {};  Column: {}, Row: {}, was changed from {} to {}".format(name,i,m,a[m],b[n]))
            #attaching the list into a new variable name
            g = z
            #defining the directory the dataframes are to be exported into as excel files
            file_pathA = os.path.join(settings.MEDIA_ROOT, name)
            #exporting as excel file into the defined directory
            A.to_excel(file_pathA,index = False, header = True, engine = 'openpyxl')
            file_pathB = os.path.join(settings.MEDIA_ROOT, name2)
            B.to_excel(file_pathB,index = False, header = True, engine = 'openpyxl')
            
            #sending the names of both files, the new html styled tables and the comment list
            # as json data into anothe view. 
            request.session['game'] = name
            request.session['came'] = name2
            request.session['stay'] = C
            request.session['hay'] = D
            request.session['ana'] = g
            
            #redirecting to the result view
            return redirect("result")
        
        #if the decision is to merge the differences in both files
        #only one file will be processed and sent
        if action == 'merge':
            ask = "merge"
            fileA = comp_code.high(fileA,fileB, ask)
        
            A = fileA.style.applymap(comp_code.highlight_cells)
    
            A = comp_code.color(A)
            C = A.to_html(index=False)

            z=[]
            for i, j in zip(fileA,fileB):
                 a,b = 0,0
                 a,b = [],[]
                 for m,n in zip(fileA[i],fileB[j]):
                    a.append(m)
                    b.append(n)
                 for m,n in zip(range(len(a)),range(len(b))):
                    if a[m] != b[n]:
                        z.append("Value in {};  Column: {}, Row: {}, was changed from {}".format(name,i,m,a[m]))
            
            g = z

            file_pathA = os.path.join(settings.MEDIA_ROOT, name)
            A.to_excel(file_pathA,index = False, header = True, engine = 'openpyxl')
             
            request.session['game'] = name
            request.session['stay'] = C
            request.session['ana'] = g 

            return redirect("merge")

        elif action == "remove":
            fileA,fileB = comp_code.rem(fileA,fileB),comp_code.rem(fileII,fileI)
        
            A = fileA.style.applymap(comp_code.remove_cells)
            B = fileB.style.applymap(comp_code.remove_cells)

            A = comp_code.color(A)
            B = comp_code.color(B)
    
            C = A.to_html(index=False)
            D = B.to_html(index=False)

            z=[]
            for i, j in zip(fileA,fileB):
                 a,b = 0,0
                 a,b = [],[]
                 for m,n in zip(fileA[i],fileB[j]):
                    a.append(m)
                    b.append(n)
                 for m,n in zip(range(len(a)),range(len(b))):
                    if a[m] != b[n]:
                        z.append("Value in {};  Column: {}, Row: {}, was changed from {} to {}".format(name,i,m,a[m],b[n]))
            g = z
            
            file_pathA = os.path.join(settings.MEDIA_ROOT, name)
            fileA.to_excel(file_pathA,index = False, header = True, engine = 'openpyxl')
            file_pathB = os.path.join(settings.MEDIA_ROOT, name2)
            fileB.to_excel(file_pathB,index = False, header = True, engine = 'openpyxl')
       
            request.session['game'] = name
            request.session['came'] = name2
            request.session['stay'] = C
            request.session['hay'] = D
            request.session['ana'] = g

            return redirect("result")

    return render(request, "index.html")



@login_required
def download(request):

    #recieving all the transferred data into the download view
    #name of the files
    name = request.session.get('game')
    name2 = request.session.get('came')
    #html instances of the processed files
    C = request.session.get('stay')
    D = request.session.get ('hay')
    #a list with analysis of the compared files
    g = request.session.get('ana')
    #a tuple containing the number of duplicates and differences present in the files
    number = request.session.get ('num')
    #assigning the values to different variables
    diff, sim = number
    
    #if the download button is pressed in the templates, this process will start
    if request.method == 'POST':
        dat = request.POST
        action = dat.get("down")
        if action == "download":
            #obtainig the path the excel files where exported to
            file_path = os.path.join(settings.MEDIA_ROOT, name)
            if os.path.exists(file_path):
                #downloading them
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
    
    return render(request, "dash/result.html", {"first":C, "second":D, "analysis":g, "diff":diff,"sim":sim, "name1":name,"name2":name2})


#view for merge result option, with only one result and download
@login_required
def mergeload(request):

    #recieving all the transferred data into the download view
    #name of the files
    name = request.session.get('game')
    #html instances of the processed files
    C = request.session.get('stay')
    #a list with analysis of the compared files
    g = request.session.get('ana')
    #a tuple containing the number of duplicates and differences present in the files
    number = request.session.get ('num')
    #assigning the values to different variables
    diff, sim = number
    
    #if the download button is pressed in the templates, this process will start
    if request.method == 'POST':
        dat = request.POST
        action = dat.get("down")
        if action == "download":
            #obtainig the path the excel files where exported to
            file_path = os.path.join(settings.MEDIA_ROOT, name)
            if os.path.exists(file_path):
                #downloading them
                with open(file_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
    
    
    return render(request, "dash/merge.html", {"first":C, "analysis":g, "diff":diff,"sim":sim, "name1":name})


def contactview(request):
    return render(request, "dash/contact.html")
    

def aboutusview(request):
    return render(request, "dash/aboutus.html")


def policyview(request):
    return render(request, "dash/privacypolicy.html")


def termsview(request):
    return render(request, "dash/terms.html")
    





    


    
    
        
        
        
        
        
