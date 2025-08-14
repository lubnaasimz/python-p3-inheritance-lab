#!/usr/bin/env python

from user import User

import random
# The Teacher class inherits from the User class and represents a teacher.
# It has a list of knowledge that the teacher can share with students.
# The teach method returns a random piece of knowledge from the list.
class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]

    def teach(self):
        return self.knowledge[random.randint(0, len(self.knowledge) - 1)]