class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms, doctor,illness):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        #ToDo1
        
        self.__doctor = doctor
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__symptoms = symptoms
        self.__illness = illness

    
    def full_name(self) :
        """full name is first_name and surname"""
        #ToDo2
        return f'{self.__first_name} {self.__surname}'
    
    def get_first_name(self):
        return self.__first_name
    
    def get_surname(self):
        return self.__surname
    
    def get_age(self):
        return self.__age
    
    def get_mobile(self):
        return self.__mobile
    
    def get_postcode(self):
        return self.__postcode
    
    def get_symptoms(self):
        return self.__symptoms

    def get_doctor(self) :
        #ToDo3
        return self.__doctor
    
    def get_illness(self):
        return self.__illness

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        #ToDo4
        print(self.__symptoms)

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
    
