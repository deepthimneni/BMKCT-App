from django.shortcuts import render, redirect
from .dbaccess import *
import base64

# Create your views here.
def index(request):
    groups = exec_sql_get_data(Sql_Queries.GET_ALL_SOME_TEXTS.value, [])
    return render(request, 'index.html', {'groups': groups})

def group_list(request, group_name, id):
    group_list = exec_sql_get_data(Sql_Queries.GET_ALL_SOME_TEXT_BOXES.value, [id])
    return render(request, 'list.html', {'group_list': group_list, 'group_name': group_name})

def delete_group(request, id):
    exec_sql(Sql_Queries.DELETE_SOME_TEXT.value, [id])
    return redirect("/")

def add_group(request):
    exec_sql(Sql_Queries.ADD_SOME_TEXT.value, [])
    return redirect("/")

def add_box(request):
    exec_sql(Sql_Queries.ADD_SOME_TEXT_BOX.value, [request.POST['id'], request.POST['content']])
    return redirect("/" + request.POST['label'] + "/" + str(request.POST['id']))
    # base64_bytes = request.POST['content'].encode('ascii')
    # message_bytes = base64.b64decode(base64_bytes)
    # message = message_bytes.decode('ascii')
    