# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Dalle','Internal Med.',[11,10,9,8,4]),
                Doctor('Jone','Smith','Pediatrics',[5,5,6,7,4]), 
                Doctor('Jone','Carlos','Cardiology',[3,7,7,7,6]),
                Doctor('Teach','Marchall','Orthopedic',[7,7,3,3,3]),
                Doctor('Trafalgar','Law','Neuro',[3,8,8,3,3])]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234',['cough','mild-fever'],'None',['Cold']),
                 Patient('Mike','Jones', 37,'07555551234','L2 2AB',['heavy breathing','fever'],'None',['Migraine']), 
                 Patient('Daivd','Smith', 15, '07123456789','C1 ABC',['cough'],'None',['Flu'])]
    discharged_patients = []
    
    # keep trying to login tell the login details are correct
  
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin detais')
        print(' 6- View Patients based on family')
        print(' 7- Store patient data in file')
        print(' 8- Load patient data from a file')
        print(' 9- Relocate patients')
        print(' 10- Management report')
        print(' 11- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
         #ToDo1
            admin.doctor_management(doctors)

        elif op == '2':
            # 2- View or discharge patients
            #ToDo2
            admin.view(patients)

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    #ToDo3
                    admin.discharge(patients , discharged_patients)
                    

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            # 3 - view discharged patients
            #ToDo4
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()

        elif op == '6':
            admin.view_patient_family(patients)

        elif op == '7':
            admin.store_patient_data(patients)

        elif op == '8':
            admin.load_patients_data(patients, doctors)

        elif op == '9':
            admin.relocate_patients(patients , doctors)

        elif op == '10':
            admin.management_report(patients, doctors)

        elif op == '11':
            # 6 - Quit
            #ToDo5
            break

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
