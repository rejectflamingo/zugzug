from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import connection
import logging

def executeSQL(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer

    #override get_queryset or create queryset
    def get_queryset(self):
        queryset = Image.objects.all()
        return queryset

    def create(self, request):
        anime_id = request.data.get('anime_id', None)
        image_medium = request.data.get('image_medium', None)
        image_large = request.data.get('image_large', None)

        # sql = "SELECT * FROM User_user WHERE username = {};".format(username)
        # res = executeSQL(sql)
        try:
            user = Image.objects.raw('SELECT * FROM Image where anime_id = %s, [anime_id]')

        except Image.DoesNotExist:
            instance = Image.objects('UPDATE Image SET anime_id = %s, image_medium = %s, image_large = %s', [anime_id, image_medium, image_large])
        # try:
        #     logging.error('test1')
            
        #     user = Image.objects.raw('SELECT * FROM Image where anime_id = %s', [anime_id])
        #     #user = Image.objects.get(anime_id=anime_id)

        #     if (len(user) == 0): 
        #         raise(Image.DoesNotExist)
        #     logging.error(len(user))

        # except Image.DoesNotExist:
           
        #     instance = Image.objects(' INSERT INTO Image (anime_id, image_medium, image_large) VALUES(%s, %s, %s)' %   (anime_id, image_medium, image_large))
            #instance = User(username=username, password=password, email=email, firstname=firstname, lastname=lastname)
            instance.save()
            return Response({"response": {"error":"OK", "anime_id": instance.anime_id, "image_medium":instance.image_medium, "image_large":instance.image_large}, "status": 201}, status=status.HTTP_201_CREATED)
        else:
            
            return Response({"response": {"error":"anime_id already exists."}, "status": 400}, status=status.HTTP_400_BAD_REQUEST)

