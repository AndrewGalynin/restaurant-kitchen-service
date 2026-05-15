from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from kitchen.models import DishType, Ingredient, Dish


class ModelsTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Pizza")
        self.assertEqual(str(dish_type), "Pizza")

    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(name="Tomato")
        self.assertEqual(str(ingredient), "Tomato")

    def test_cook_str_and_absolute_url(self):
        cook = get_user_model().objects.create_user(
            username="gordon_ramsay",
            password="password123",
            years_of_experience=15
        )
        self.assertEqual(str(cook), "gordon_ramsay")
        self.assertEqual(
            cook.get_absolute_url(),
            reverse("kitchen:cook-detail", kwargs={"pk": cook.pk})
        )

    def test_dish_str_and_absolute_url(self):
        dish_type = DishType.objects.create(name="Main Course")
        dish = Dish.objects.create(
            name="Steak",
            description="Juicy steak",
            price=250.00,
            dish_type=dish_type
        )
        self.assertEqual(str(dish), "Steak")
        self.assertEqual(
            dish.get_absolute_url(),
            reverse("kitchen:dish-detail", kwargs={"pk": dish.pk})
        )