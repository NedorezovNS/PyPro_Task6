import unittest
from unittest import TestCase

from parameterized import parameterized

from modules import app
from modules.tests_data import *


class TestApp(TestCase):

    @parameterized.expand([
        (courses_cd, durations_cd, expected_cd)
    ])
    def test_courses_duration(self, courses, durations, expected):
        result = app.courses_duration(courses, durations)
        self.assertEqual(result, expected)

    @parameterized.expand([
        (mentors_top3, expected_top3)
    ])
    def test_top_3_names(self, mentors, expected):
        result = app.top_3_names(mentors)
        self.assertEqual(result, expected)

    @parameterized.expand([
        (courses_nsf, mentors_nsf, durations_nsf, expected_nsf)
    ])
    def test_namesake_finder(self, courses, mentors, durations, expected):
        result = app.namesake_finder(courses, mentors, durations)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
