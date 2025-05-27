from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    thread = models.ForeignKey('Thread', related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class ThreadManager(models.Manager):
    def find(self, user1, user2):
        queryset = self.filter(users=user1).filter(users=user2)
        if len(queryset) > 0:
            return queryset[0]
        else:
            return None
    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)

        if thread is None:  
            thread = Thread.objects.create()
            thread.users.add(user1, user2)
        return thread

        
class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    updated = models.DateTimeField(auto_now=True)

    objects = ThreadManager()

    class Meta:
        ordering = ['-updated']

def mesages_change(sender,  **kwargs):
   instance = kwargs.pop('instance', None)
   action = kwargs.pop('action', None) 
   pk_set = kwargs.pop('pk_set', None)
   print(instance, action, pk_set)
   
   false_pk_set = set()
   if action == "pre_add":
       for msg_pk in pk_set:
           msg = Message.objects.get(pk=msg_pk)
           if msg.user not in instance.users.all():
               print("el ({}) no pertenece a los usuarios del hilo".format(msg.user))
               false_pk_set.add(msg_pk)

   # buscar el mensaje en el pk_set y eliminarlo
   pk_set.difference_update(false_pk_set)    

   # forzar la actualizacion haciendo un save
   instance.save()
   


