import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from profiles.models import Profile, ProfileStatus
from profiles.api.serializers import ProfileSerializers, ProfileStatusSerializers

# testare endpoint per la registrazione
class RegistrationTestCase(APITestCase):

    def test_regitratation(self):
        data = { 
            "username" : "testcase",
            "email" : "test@local.com",
            "password1" : "cambiami1",
            "password2" : "cambiami1"
        }

        response = self.client.post("/api/rest-auth/registration/", data)

        self.assertEqual(response.status_code , status.HTTP_201_CREATED)

class ProfileViewTestCase(APITestCase):
    list_url = reverse("profile-list") # router - basename


    def setUp(self):
        # andiamo a popolare il db con alcune instance per i nostri test
        # il nostro Profile verra' creato automaticamente grazie a SIGNAL
        self.user = User.objects.create_user(username="davinci", password="pwddavinci")
        
        # andiamo a generare un Token
        self.token = Token.objects.create(user=self.user)

        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_detail_retrieve(self):
        response = self.client.get(reverse("profile-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"],"davinci")

    # test endpoint update
    def test_profile_update_by_user(self):
        response = self.client.put(reverse("profile-detail", kwargs={"pk": 1}),
        {"city": "bellacitta", "bio": "genio trai i geni"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
            {
            "id": 1, 
            "user" : "davinci", 
            "city": "bellacitta", 
            "bio": "genio trai i geni",
            "avatar" : None
            }
        )

    def test_profile_update_by_random_user(self):
        random_user = User.objects.create_user(username="random_usr", password="123123")
        self.client.force_authenticate(user=random_user)

        # proviamo a modificare la "bio" dello user "davinci" da questo 
        # user random
        response = self.client.put(reverse("profile-detail", kwargs={"pk": 1}),
        {"bio": "hacked!!!"})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class ProfileStatusViewTestCase(APITestCase):
    url = reverse("status-list") # fornito dal nostro router - basename

    print(f"::::::::::::::::::: ProfileStatusViewTestCase url reverse {url}")

    def setUp(self):
        self.user = User.objects.create_user(username="davinci", password="pwddavinci")
        # andiamo a generare un Token
        self.token = Token.objects.create(user=self.user)
        # qui dobbiamo craere anche uno Status
        self.status = ProfileStatus.objects.create(user_profile=self.user.profile,
                                                status_content="test status")

        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_status_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_status_list_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test creazione di un nuovo status
    def test_status_create(self):
        data = {"status_content" : "nuovo stato !!!"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user_profile"],"davinci")
        self.assertEqual(response.data["status_content"],"nuovo stato !!!")

    # test "retrieve" singolo status
    def test_single_status_retrieve(self):
        serializer_data = ProfileStatusSerializers(instance=self.status).data
        response = self.client.get(
            reverse("status-detail", kwargs={"pk":1})
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEquals(serializer_data, response_data)

    # endpoint di aggioramento per i nostri status
    # sia con un User Owner che con uno Random
    def test_status_update_owner(self):
        data = {"status_content": "stato UPDATE !!!!!!"}
        response = self.client.put(
                                reverse("status-detail",kwargs={"pk":1}),
                                data=data
                                )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status_content"], "stato UPDATE !!!!!!")

    def test_status_update_random_user(self):
        random_user = User.objects.create_user(username="random_usr", password="123123")
        self.client.force_authenticate(user=random_user)

        data = {"status_content": "stato UPDATE HACKED!!!"}
        response = self.client.put(
                                reverse("status-detail",kwargs={"pk":1}),
                                data=data
                                )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)