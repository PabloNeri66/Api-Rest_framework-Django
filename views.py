from app.models import Todo
from app.serializers import TodoSerializer

# from rest_framework.decorators import api_view
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.exceptions import NotFound


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


#GET E POST:

#class TodoListAndCreate(generics.ListCreateAPIView):
#   queryset = Todo.objects.all()
#   serializer_class = TodoSerializer
 
 
 
 #modo Hard(todo a parte funcional dos modulos importados!):
 
 #   def get(self, request):
 #       todo = Todo.objects.all()
 #       serializer = TodoSerializer(todo, many=True)
 #       return Response(serializer.data)
 # 
 #   def post(self, request):
 #       serializer =  TodoSerializer(data=request.data)
 #       if serializer.is_valid():
 #          serializer.save()
 #           return Response(serializer.data, status = status.HTTP_201_CREATED)
 #       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#GET E PUT E DELETE:

#class TodoDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Todo.objects.all()
    #serializer_class = TodoSerializer


# modo Hard:


#    def get_object(self, pk):
#        try:
#            return Todo.objects.get(pk=pk)
#        except Todo.DoesNotExist:
#            raise NotFound()
#   
#   
#    def get(self, request, pk):
#        todo = self.get_object(pk)
#        serializer = TodoSerializer(todo)
#        return Response(serializer.data)
#    
#    def put(self, request, pk):
#        todo = self.get_object(pk)
#        serializer = TodoSerializer(todo, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#           return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#    
#    def delete(self, request, pk):
#        todo = self.get_object(pk)
#        todo.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
        



    




