from django.shortcuts import render
#from excel_comp_team_106.dashboard.forms import FileForm
import pandas as pd
from django.contrib.auth.decorators import login_required
import pandas as pd
import comp_code

#@login_required
#def file_upload_view(request):
#    """Process files uploaded by users"""
#    if request.method == 'POST':
#        form = FileForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
            # Get the current instance object to display in the template
#
#            file_obj = form.instance
#            return render(request, 'index.html', {'form': form, 'file_obj': file_obj})
#    else:
#        form = FileForm()
#    return render(request, 'compare/index.html', {'form': form})

#def process_files(request):
#    pass

@login_required
def file_upload_view(request):

    if request.method == "POST":
        
        data = request.POST
        action = data.get("criteria")
        decision = data.get("download")
        file1=request.FILES['upload']
        file2=request.FILES['upload']
        #object1=file.objects.create(file=file1)not yet
        #object2=file.objects.create(file=file2)
        file1 = pd.read_excel(file1)
        file2 = pd.read_excel(file2)  
        ask = "not"
        if action == "highlight":
            if decision == 'merge':
                ask = "merge"
            else:
                ask = "not"
            p,m = comp_code.high(file1,file2, ask),comp_code.high(file2,file1, ask)
        elif action == "remove":
            p,m = comp_code.rem(file1,file2),comp_code.rem(file2,file1)
        context1=file1.objects.all()
        context2=file2.objects.all()


    return render(request, "compare/index.html", {"context1": context1,"context2": context2})


def result_view(request):

    def highlight_cells(val):
        pat = str(val)
        color = 'orange' if pat[0] == '*' else 'blue'
        return 'background-color: {}'.format(color)

    s = p.style.applymap(highlight_cells)
    h = m.style.applymap(highlight_cells)
    
    
    s = s.set_properties(
    **{'border': '1px black solid !important'}).set_table_attributes(
    'style="border-collapse:collapse"').set_table_styles([{
        'selector': '.col_heading',
        'props': 'background-color: cyan; color: black; border-collapse: collapse; border: 1px black solid !important;'
    }])
    h = h.set_properties(
    **{'border': '1px black solid !important'}).set_table_attributes(
    'style="border-collapse:collapse"').set_table_styles([{
        'selector': '.col_heading',
        'props': 'background-color: cyan; color: black; border-collapse: collapse; border: 1px black solid !important;'
    }])
    first = s.to_html(index=False)
    second = h.to_html(index=False)
    
    frame = {'compare': first,
               'compare2': second,}
    return render (request, "result.html", context = frame)