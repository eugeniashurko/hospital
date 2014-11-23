__author__ = 'Саша'
import HMS.HMS.Staff as Staff


class Patient(Staff.Person):

    def __init__(self):
        self.medicalCard = None;
        self.id = None