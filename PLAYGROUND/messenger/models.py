from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    
class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)
    
    
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

m2m_changed.connect(mesages_change, sender=Thread.messages.through)