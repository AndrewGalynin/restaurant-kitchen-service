from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from kitchen.models import DishType, Dish


class PublicViewsTests(TestCase):
    def test_login_required(self):
        res = self.client.get(reverse("kitchen:dish-list"))
        self.assertNotEqual(res.status_code, 200)
        self.assertEqual(res.status_code, 302)


class PrivateViewsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_cook", password="password123"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(name="Dessert")
        DishType.objects.create(name="Pizza")

        res = self.client.get(reverse("kitchen:dish-type-list"))

        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context["dish_type_list"]), 2)
        self.assertTemplateUsed(res, "kitchen/dish_type_list.html")

    def test_search_dish_types(self):
        DishType.objects.create(name="Dessert")
        DishType.objects.create(name="Pizza")

        res = self.client.get(reverse("kitchen:dish-type-list") + "?name=Pizz")

        self.assertEqual(len(res.context["dish_type_list"]), 1)
        self.assertEqual(res.context["dish_type_list"][0].name, "Pizza")

    def test_search_dishes(self):
        dish_type = DishType.objects.create(name="Main")
        Dish.objects.create(name="Burger", description="Beef burger", price=100, dish_type=dish_type)
        Dish.objects.create(name="Pizza", description="Cheese pizza", price=150, dish_type=dish_type)

        res = self.client.get(reverse("kitchen:dish-list") + "?name=Burger")

        self.assertEqual(len(res.context["dish_list"]), 1)
        self.assertEqual(res.context["dish_list"][0].name, "Burger")