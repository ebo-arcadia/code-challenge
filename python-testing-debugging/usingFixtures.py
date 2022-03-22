# what is fixture? - way of providing data, test doubles, state setup. it is function
# when to use it and why? - when the data used for testing multiple functions is the same
# when not to use it and why? - when testing data has variations or different or when writing test using the same test data
# how fixture is created and how to use it in code?

import pytest

people = [
    {
        "given_name": "Alfonsa",
        "family_name": "Ruiz",
        "title": "Senior Software Engineer",
    },
    {
        "given_name": "Sayid",
        "family_name": "Khan",
        "title": "Project Manager",
    },
]

def format_data_for_display(people):
    return people

def format_data_for_excel(people):
    return people


@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]


def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]

def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) == """given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
"""
