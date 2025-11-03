from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view()
# def student_data(request):
#     return Response({'msg':'This is GET'})

@api_view(['GET','POST'])
def student_data(request):
    if request.method == 'GET':
        return Response({'msg':'This is GET'})
    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'This is POST'})
    

