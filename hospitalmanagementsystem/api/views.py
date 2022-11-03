from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Department, Client, Person, Employee
from api.serializers import DepartmentSerializer, ClientSerializer, EmployeeSerializer
from api.forms import CreateUserForm

from django.http import JsonResponse

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/appointment/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of appointments'
        },
        {
            'Endpoint': '/appointment/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/appointment/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new appointment with data sent in post request'
        },
        {
            'Endpoint': '/appointment/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing appointment with data sent in post request'
        },
        {
            'Endpoint': '/appointment/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting appointment'
        },
    ]
    return Response(routes)

@api_view(['POST'])
def registerPage(request):
    form = CreateUserForm(request.POST)
    if form.is_valid():
        form.save()
    print(form)
    # context = {'form': form}

    return Response('Done')

def loginPage(request):
    return Response('Done')

@api_view(['GET'])
def getAppointments(request):
    return Response('APPOINTMENTS')

#Departments

@api_view(['GET', 'POST'])
def getDepartments(request):
    """
    List all departments, or create a new department.
    """
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    if request.method == 'POST':    
        serializer = DepartmentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(id=id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def getDepartment(request, pk):
    """
    Retrieve, update or delete a department.
    """
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DepartmentSerializer(department, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = DepartmentSerializer(instance=department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Clients

@api_view(['GET', 'POST'])
def getClients(request):

    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    if request.method == 'POST':    
        newClient = Client(request.data)
        newClient.save()
        print(f"Created new client: {newClient.name}")
        return Response('Done')

@api_view(['GET', 'PUT', 'DELETE'])
def getClient(request, pk):

        if request.method == 'GET':
            client = Client.objects.get(id=pk)
            serializer = ClientSerializer(client, many=False)
            return Response(serializer.data)

        if request.method == 'PUT':
            data = request.data
            client = Client.objects.get(id=pk)
            serializer = ClientSerializer(instance=client, data=data)
            if serializer.is_valid():
                serializer.save()
            return serializer.data

        if request.method == 'DELETE':
            client = Client.objects.get(id=pk)
            client.delete()
            return Response(f'Client {pk} was deleted')

