from graphene.test import Client
from snapshottest.django import TestCase

from pycon_graphql.schemas import schema
from users.models import User


class UserAPITestCase(TestCase):

    def setUp(self):
        self.main_user = User.objects.create(
            first_name="Jhon",
            last_name="Doe",
            email="jhon@doe.com",
            profile_image="/profile/image.png",
            profile="This is the profile John Doe",
            username="johndoe"
        )
        self.main_user.set_password("123admin123")
        self.main_user.save()
        self.client = Client(schema)

    def test_api_users(self):
        self.assertMatchSnapshot(self.client.execute(
            '''query{
                  users{
                    edges{
                      node{
                        id
                        firstName
                        lastName
                        email
                        username
                      }
                    }
                  }
                }
            '''
        ))

    def test_login_user_mutation(self):
        self.assertMatchSnapshot(self.client.execute(
            '''mutation{
                  loginUser(input: {email: "me@carlosmart.co", password:"123admin123"}){
                    ok,
                    user {
                      id
                    }
                  }
                }
            '''
        ))

    def test_logout_user_mutation(self):
        self.assertMatchSnapshot(self.client.execute(
            '''
            mutation{
              logoutUser(input: {}){
                ok
              }
            }
            '''
        ))

    def test_register_user_mutation(self):
        self.assertMatchSnapshot(self.client.execute(
            '''
            mutation{
              registerUser(
                userInput: {
                  email: "me@carlosmart.co",
                  username: "carlosmart",
                  firstName: "Carlos",
                  lastName: "Martinez"
                }
              ){
                user{
                  id
                  email
                }
              }
            }
            '''
        ))

    def test_register_user_wrong_email(self):
        self.assertMatchSnapshot(self.client.execute(
            '''
            mutation{
              registerUser(
                userInput: {
                  email: "mecarlosmartco",
                  username: "carlosmart",
                  firstName: "Carlos",
                  lastName: "Martinez"
                }
              ){
                user{
                  id
                  email
                }
              }
            }
            '''
        ))

    def test_register_user_already_registered_mutation(self):
        self.assertMatchSnapshot(self.client.execute(
            '''
            mutation{
              registerUser(
                userInput: {
                  email: "jhon@doe.com",
                  username: "carlosmart",
                  firstName: "Carlos",
                  lastName: "Martinez"
                }
              ){
                user{
                  id
                  email
                }
              }
            }
            '''
        ))
        self.assertMatchSnapshot(self.client.execute(
            '''
            mutation{
              registerUser(
                userInput: {
                  email: "new_email@example.org",
                  username: "johndoe",
                  firstName: "John",
                  lastName: "Doe"
                }
              ){
                user{
                  id
                  email
                }
              }
            }
            '''
        ))
