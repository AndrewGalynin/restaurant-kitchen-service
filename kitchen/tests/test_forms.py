from django.test import TestCase

from kitchen.forms import CookExperienceUpdateForm, DishSearchForm


class FormsTests(TestCase):
    def test_cook_experience_update_form_valid(self):
        form = CookExperienceUpdateForm(data={"years_of_experience": 5})
        self.assertTrue(form.is_valid())

    def test_cook_experience_update_form_invalid_negative(self):
        form = CookExperienceUpdateForm(data={"years_of_experience": -2})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["years_of_experience"],
            ["Work experience cannot be negative."]
        )

    def test_dish_search_form_valid(self):
        form = DishSearchForm(data={"name": "Pizza"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "Pizza")
