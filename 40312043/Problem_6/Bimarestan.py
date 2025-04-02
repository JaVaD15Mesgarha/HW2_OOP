class Person:
    id_generator = {"P": 1, "D": 1, "N": 1 }

    def __init__(self, first_name, last_name, age, gender):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__gender = gender

    def get_details(self):
        return f"Name: {self.__first_name} {self.__last_name}\n Age: {self.__age}\n Gender: {self.__gender}"


class Patient(Person):
    def __init__(self, first_name, last_name, age, gender, disease, doctor):
        super().__init__(first_name, last_name, age, gender)
        self.__disease = disease
        self.__doctor = doctor
        role = "P"
        self.__id = f"{role}{Person.id_generator[role]:03d}"
        Person.id_generator[role] += 1

    def get_patient_details(self):
        return f"{self.get_details()}\n ID: {self.__id}\n Disease: {self.__disease}\n Assigned Doctor: {self.__doctor._Person__first_name} {self.__doctor._Person__last_name}"


class Doctor(Person):
    def __init__(self, first_name, last_name, age, gender, specialization):
        super().__init__(first_name, last_name, age, gender)
        self.__specialization = specialization
        self.__patients = []
        role = "D"
        self.__id = f"{role}{Person.id_generator[role]:03d}"
        Person.id_generator[role] += 1

    def add_patient(self, patient):
        self.__patients.append(patient)

    def get_doctor_details(self):
        patients_list = "No Patients"
        if self.__patients:
            patients = []
            for patient in self.__patients:
                patients.append(patient.get_details())
            patients_list = ", ".join(patients)
        return f"{self.get_details()}\n ID: {self.__id}\n Specialization: {self.__specialization}\n Patients: {patients_list}"


class Nurse(Person):
    def __init__(self, first_name, last_name, age, gender, department):
        super().__init__(first_name, last_name, age, gender)
        self.__department = department
        role = "N"
        self.__id = f"{role}{Person.id_generator[role]:03d}"
        Person.id_generator[role] += 1

    def get_nurse_details(self):
        return f"{self.get_details()}\n ID: {self.__id}\n Department: {self.__department}"


class Appointment:
    appointment_id = 1
    def __init__(self, patient, doctor, appointment_time):
        self.__patient = patient
        self.__doctor = doctor
        self.__appointment_time = appointment_time
        self.__status = "Scheduled"
        self.__id = f"{Appointment.appointment_id:03d}"
        Appointment.appointment_id += 1

    def cancel_appointment(self):
        self.__status = "Canceled"

    def get_appointment_details(self):
        return f"Patient: {self.__patient._Person__first_name} {self.__patient._Person__last_name} \n Doctor: {self.__doctor._Person__first_name} {self.__doctor._Person__last_name}\n Date and Time: {self.__appointment_time}\n Status: {self.__status}"


class Hospital:
    def __init__(self):
        self.__patients = []
        self.__doctors = []
        self.__nurses = []
        self.__appointments = []

    def find_doctor(self, first_name, last_name):
        for doctor in self.__doctors:
            if doctor._Person__first_name == first_name and doctor._Person__last_name == last_name:
                return doctor
        return None
    
    def find_patient(self, first_name, last_name):
        for patient in self.__patients:
            if patient._Person__first_name == first_name and patient._Person__last_name == last_name:
                return patient
        return None

    def add_patient(self, patient):
        self.__patients.append(patient)

    def add_doctor(self, doctor):
        self.__doctors.append(doctor)

    def add_nurse(self, nurse):
        self.__nurses.append(nurse)

    def schedule_appointment(self, appointment):
        self.__appointments.append(appointment)

    def canceling_appointment(self, appointment_id):
        for appointment in self.__appointments:
            if appointment._Appointment__id == appointment_id:
                appointment.cancel_appointment()
                return f"Appointment canceled successfully:\n" \
                    f"Patient: {appointment._Appointment__patient._Person__first_name} {appointment._Appointment__patient._Person__last_name}\n" \
                    f"Doctor: Dr. {appointment._Appointment__doctor._Person__first_name} {appointment._Appointment__doctor._Person__last_name}\n" \
                    f"Date and Time: {appointment._Appointment__appointment_time}\n" \
                    f"Status: {appointment._Appointment__status}"
        return "Appointment not found!"

    def get_all_patients(self):
        return [f"{p._Person__first_name} {p._Person__last_name}, ID: {p._Patient__id}, Disease: {p._Patient__disease}" for p in self.__patients]

    def get_all_doctors(self):
        return [f"Dr. {d._Person__first_name} {d._Person__last_name}, ID: {d._Doctor__id}, Specialization: {d._Doctor__specialization}" for d in self.__doctors]

    def get_all_nurses(self):
        return [n.get_nurse_details() for n in self.__nurses]

    def get_all_appointments(self):
        return [f"Patient: {a._Appointment__patient._Person__first_name} {a._Appointment__patient._Person__last_name}, Doctor: Dr. {a._Appointment__doctor._Person__first_name} {a._Appointment__doctor._Person__last_name}, Date: {a._Appointment__appointment_time}, Status: {a._Appointment__status}, ID: {a._Appointment__id}" for a in self.__appointments
        ]


def main():
    hospital = Hospital()

    while True:
        print("\nHospital Management System")
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Add Nurse")
        print("4. Schedule & Cancel Appointment")
        print("5. Show All Patients")
        print("6. Show All Doctors")
        print("7. Show All Nurses")
        print("8. Show All Appointments")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("Enter doctor's first name: ")
            last_name = input("Enter doctor's last name: ")
            age = input("Enter doctor's age: ")
            gender = input("Enter doctor's gender: ")
            specialization = input("Enter specialization: ")
            doctor = Doctor(first_name, last_name, age, gender, specialization)
            hospital.add_doctor(doctor)
            print("Doctor added successfully:\n", doctor.get_doctor_details())

        elif choice == "2":
            first_name = input("Enter patient's first name: ")
            last_name = input("Enter patient's last name: ")
            age = input("Enter patient's age: ")
            gender = input("Enter patient's gender: ")
            disease = input("Enter disease: ")

            doctor_name = input("Enter your doctor's First & Last Name: ").split(" ")
            doctor = hospital.find_doctor(doctor_name[0], doctor_name[1])

            if doctor:
                patient = Patient(first_name, last_name, age, gender, disease, doctor)
                doctor.add_patient(patient)
                hospital.add_patient(patient)
                print("Patient added successfully:\n", patient.get_patient_details())
            else:
                print("Doctor Not Found!")
    
        elif choice == "3":
            first_name = input("Enter nurse's first name: ")
            last_name = input("Enter nurse's last name: ")
            age = input("Enter nurse's age: ")
            gender = input("Enter nurse's gender: ")
            department = input("Enter department: ")
            nurse = Nurse(first_name, last_name,  age, gender, department)
            hospital.add_nurse(nurse)
            print("Nurse added successfully:\n", nurse.get_nurse_details())

        elif choice == "4":
            print("Appointement Menu")
            appointment_choice = input("1. Scheduling\n2. Canceling\nEnter Your Choice: ")
            if appointment_choice == "1" :
                patient_name = input("Enter Patient's First & Last Name: ").split(" ")
                doctor_name = input("Enter Doctor's First & Last Name: ").split(" ")
                appointment_time = input("Enter appointment time: ")

                patient = hospital.find_patient(patient_name[0], patient_name[1])
                doctor = hospital.find_doctor(doctor_name[0], doctor_name[1])

                if patient and doctor:
                    appointment = Appointment(patient, doctor, appointment_time)
                    hospital.schedule_appointment(appointment)
                    print("Appointment scheduled successfully!")
                    print(appointment.get_appointment_details())
                else:
                    print("Doctor or Patient Not Found!")
            elif appointment_choice == "2":
                appointment_id = input("Enter Appointment ID to cancel: ")
                result = hospital.canceling_appointment(appointment_id)
                print(result)

        elif choice == "5":
            print("All Patients:")
            for patient in hospital.get_all_patients():
                print(patient)
        
        elif choice == "6":
            print("All Doctors:")
            for doctors in hospital.get_all_doctors():
                print(doctors)
            
        elif choice == "7":
            print("All Nurses:")
            for nurses in hospital.get_all_nurses():
                print(nurses)

        elif choice == "8":
            print("All Appointments:")
            for appointments in hospital.get_all_appointments() :
                print(appointments)
        
        elif choice == "9":
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()