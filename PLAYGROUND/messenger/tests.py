from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Thread
# Create your tests here.

class ThreadTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1', 'password')
        self.user2 = User.objects.create_user('user2', 'password')
        self.user3 = User.objects.create_user('user3', 'password')
        self.thread = Thread.objects.create()
        # self.thread.users.add(self.user1, self.user2)

    def test_add_user_tu_thread(self):
        self.thread.users.add(self.user1, self.user2)
        self.assertEqual(len(self.thread.users.all()), 2)

    def test_filter_thread_by_user(self):
        self.thread.users.add(self.user1, self.user2)
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(threads[0], self.thread)

    def test_filter_non_existent_thread(self):
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(len(threads), 0)

    def test_add_message_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content="Hello")
        message2 = Message.objects.create(user=self.user1, content="adios")
        self.thread.messages.add(message1, message2)
        self.assertEqual(len(self.thread.messages.all()), 2)

        for message in self.thread.messages.all():
            print(message.content, message.user.username)
    
    def test_add_message_from_user_not_in_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content="Hello")
        message2 = Message.objects.create(user=self.user1, content="adios")
        message3 = Message.objects.create(user=self.user3, content="soy un espia")
        self.thread.messages.add(message1, message2, message3)
        # Check that the message from user3 is not in the thread
        self.assertEqual(len(self.thread.messages.all()), 2)
        
    
    def test_find_thread_whit_custom_manager(self):
        self.thread.users.add(self.user1, self.user2)
        thread = Thread.objects.find(self.user1, self.user2)
        self.assertEqual(self.thread, thread)
    
    def test_find_or_create_thread_whit_custom_manager(self):
        self.thread.users.add(self.user1, self.user2)
        thread = Thread.objects.find_or_create(self.user1, self.user2)
        self.assertEqual(self.thread, thread)
        thread = Thread.objects.find_or_create(self.user1, self.user3)
        self.assertIsNotNone(thread)