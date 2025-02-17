import matplotlib.pyplot as plt
import numpy as np
from Doctor import Doctor
from Patient import Patient


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        #ToDo1
        return self.__username in username and self.__password == password

    def find_index(self,index,doctors):    
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True
        
        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        first_name = input("Enter the first name: ")
        surname = input("Enter the surname: ")
        speciality = input("Enter the speciality: ")
        appointment = []
        return Doctor(first_name , surname  , speciality, appointment)
    

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        op = input("Option: ")


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4
            new_doctor = self.get_doctor_details()
            first_name = new_doctor.get_first_name()
            surname = new_doctor.get_surname()
            
            
            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    #ToDo5
                    name_exists = True
                    break # save time and end the loop
            #ToDo6
            if name_exists == False:
                doctors.append(new_doctor)
                print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")
                    
                        # doctor_index is the ID mines one (-1)

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = input('Input: ')

            #ToDo8
            if op == "1":
                new_first_name = input("Enter new first name: ")
                doctors[index].set_first_name(new_first_name)

            elif op == "2":
                new_surname = input("Enter new surname: ")
                doctors[index].set_surname(new_surname)

            elif op == "3":
                new_speciality = input("Enter new speciality: ")
                doctors[index].set_speciality(new_speciality)
                
        # Delete
        elif op == '4':
            while True:
                print("-----Delete Doctor-----")
                print('ID |          Full Name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                    
                        break
                        
                    else:
                        print("Doctor not found")
                        # doctor_index is the ID mines one (-1)

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')
                #ToDo9
            print(f"Dr.{doctors[index].full_name()} deleted sucessfully.")
            del doctors[index]
        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo10
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) - 1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].set_appointments(doctors[doctor_index].get_appointments() + [1])
            
                print('The patient is now assigned to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")
        self.view(patients)
        patient_index = input('Please enter the patient ID: ')
        
        #ToDo12
        try:
            patient_index = int(patient_index) -1
            
            if patient_index in range(len(patients)):
                discharge_patients.append(patients[patient_index])
                del patients[patient_index]
                print('Patient discharged sucessfully')    
            
        except ValueError: 
            print('The id entered is incorrect')
            return 
     

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo13
        self.view(discharged_patients)

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            #ToDo14
            username = input("Enter the new username: ")
            self.__username = username

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password

        elif op == 3:
            #ToDo15
            address = input("Enter the address: ")
            self.__address = address

        else:
            #ToDo16
            print("Invalid option!")

    def patients_family(self,patients):
        patient_family ={}
        for patient in patients:
            surname = patient.get_surname()

            if surname not in patient_family:
                patient_family[surname] = []
            patient_family[surname].append(patient)

        
        return patient_family
    
    def view_patient_family(self, patients):
        patient_family = self.patients_family(patients)
        for surname , member in patient_family.items():
            print(f"Family: {surname}")
            print(f'{"Name":^30}|{"Doctor assigned":^30}|{"Age":^5}|{"Mobile No":^15}|{"Postcode":^10}')
            for members in member:
                print(members)


    def store_patient_data(self,patients):
        with open("patient.txt", 'a') as fp:
            for patient in patients:
                fp.write(f'{patient.get_first_name()}|{patient.get_surname()}|{patient.get_age()}|{patient.get_mobile()}|{patient.get_postcode()}|{patient.get_symptoms()}\n')
        print("Patient data stored sucessfully.")
      
    def load_patients_data(self, patients, doctors):
        with open("patient_data.txt", "r") as fp:
                for line in fp:
                    part = line.strip().split("|")
                    if len(part) == 8:
                        first_name = part[0].strip()
                        surname = part[1].strip()
                        age = part[2].strip()
                        mobile = part[3].strip()
                        postcode = part[4].strip()
                        symptoms = eval(part[5].strip())
                        doctor = part[6].strip()
                        illness = eval(part[7].strip())

                    new_patient = Patient(first_name , surname, age, mobile, postcode , symptoms, doctor, illness)
                    patients.append(new_patient)

                    for dr in doctors:
                        if dr.full_name() == doctor:
                            dr.add_patient(new_patient)

        print("Data imprted from patient.txt sucessfully")

    def relocate_patients(self,patients,doctors):
        count = 1
        available_patient = []
        print("-----Relocate patients-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        for patient in patients:
            if patient.get_doctor() != 'None':
                print(f'{count:3}|{patient}')
                available_patient.append(patient)
                count = count + 1
        patient_index = input('Please enter the patient ID: ')

        try:

            patient_index = int(patient_index) -1

            if patient_index not in range(count-1):
                print('The id entered was not found.')
                return 

        except ValueError:
            print('The id entered is incorrect')
            return 
        
        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        available_patient[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) - 1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                doctors[doctor_index].add_patient(patient_index)
                available_patient[patient_index].link(doctors[doctor_index].full_name())

                print(f'Patient {available_patient[patient_index].full_name()} is  relocated to the Dr {doctors[doctor_index].full_name()}.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')

        

    def management_report(self, patients ,doctors):  
        running = True
        while running:
            print("-------------Management---------------")
            print('1. Total no of doctors in system.')
            print('2. Total no of patients per doctor.')
            print('3. Total no of appointments per month per doctor.')
            print('4. Total no of patients based on the illness type.')
            print('5. View diagram report')
            print("(NOte: Import the data first for better view diagram)")
            print('6. Go back')
            option = input("Option: ")
            if option == "1":
                print("Total no of doctors in system are:")
                print(len(doctors))

            elif option == '2':
                for doctor in doctors:
                    count = 0
                    print(f'Dr {doctor.full_name()}') 
                    print("-------------PATIENT LIST-----------------")
                    for patient in patients:
                        if doctor.full_name() == patient.get_doctor():
                            print(patient.full_name())
                            count = count + 1
                    print("-------------------------------------------")
                    print(f'Total patient of Dr {doctor.full_name()}: {count}')

            elif option == "3":
                for doctor in doctors:
                    print(f'Dr. {doctor.full_name()}')
                    print("---------------------------------")
                    appointment = doctor.get_appointments()
                    count = 1
                    for item in appointment:
                        print(f'Appointments for month {count}: {item}')
                        count += 1

            elif option == "4":
                illness = self.sorting_illness(patients)
                print('------------------ILLNESS--------------------')
                for illness , patient in illness.items():
                    print(f"----------patient's suffering {illness}----------")
                    for patients in patient:
                        print(patients)
                    print(f'Total patients :{len(patient)}')
                    
            elif option == "5":

                #Total no of doctor in system
                xpoints = ['Doctors'] 
                ypoints = [len(doctors)]  
                plt.ylim(0,9)

                plt.bar(xpoints, ypoints)
                plt.title("Total Number of Doctors in the System")
                plt.xlabel("Total")
                plt.ylabel("Number of Doctors")
                plt.grid(axis='y')
                plt.show()

                #Total no of patients per doctor
                
                xpoints = []
                for doctor in doctors:
                    points = doctor.full_name()
                    xpoints.append(points)

                plt.ylim(0,15)
                ypoints = []
                for doctor in doctors:
                    points = len(doctor.get_patient())
                    ypoints.append(points)
                
                plt.grid(axis = 'y')
                plt.bar(xpoints,ypoints )
                plt.xlabel("Doctors")
                plt.ylabel("No. of patients")
                plt.title("Total no of Patients per Doctor")
                plt.show()


                # Total no of appointments per doctor
                xpoints = [1,2,3,4,5]
                for doctor in doctors:
                    ypoints = np.array(doctor.get_appointments())
                    if len(ypoints) != 5:
                        ypoints =  np.pad(ypoints, (0, 5 - len(ypoints)), 'constant', constant_values=0)
                    plt.plot(xpoints , ypoints , marker = 'o', label = doctor.full_name())
                
                plt.xlabel("Months")
                plt.ylabel("Number of Appointments")
                plt.title("Number of Appointments of Doctors per month")
                plt.legend()
                plt.xticks(xpoints)
                plt.show()


                #Total no of patients based on illness type
                illness = self.sorting_illness(patients)
                labels = []
                data = []
                for illness , no_patients in illness.items():
                    labels.append(f'{illness}: ({len(no_patients)}) ')
                    data.append(len(no_patients))
                
                plt.pie(data , labels=labels)
                plt.xlabel(f'Total no of patients: {len(patients)}')
                plt.title("Total no of patients based on illness type")
                plt.show()

            elif option == "6":
                running = False

            else:
                print("Invalid option!")

    def sorting_illness(self, patients):
        illness = {}
        for patient in patients:
            symptom_list = patient.get_illness()

            for symptom in symptom_list:
                if symptom not in illness:
                    illness[symptom] = []
                illness[symptom].append(patient.full_name())

        return illness