from typing import Annotated, Dict, List, Optional
from pydantic import AnyUrl, BaseModel, EmailStr, Field, computed_field, field_validator, model_validator


class Patient(BaseModel):
    name: Annotated[
        str,
        Field(
            max_length=50,
            title="Name of the patient.",
            description="Enter the name of the following patient in less than 50 characters.",
        ),
    ]
    email: EmailStr
    linked_in: AnyUrl
    age: int
    weight: float = Field(gt=0)
    height: float = Field(gt=0)
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    

    #@computed_field
    #@property
    #def calculate_bmi(self) -> float:
    #    return round(self.weight / (self.height**2), 2)

# def insert_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print('Inserted')

# patient_info = {'name': 'Priyanshu', 'age': 24}
# patient1 = Patient(**patient_info)
# insert_patient_data(patient1)

#field_validator = adding metadatas, single
    #@field_validator("email")
    #@classmethod
    #def email_validator(cls, value):
        #valid_domains = ["gmail.com", "hotmail.com"]
        #domain_name = value.split("@")[-1]
        #if domain_name not in valid_domains:
        #    raise ValueError("Invalid Domain")
        #return value

#model_validator = used for multiple additions of metadats
    #@model_validator(mode="after")
    #def validate_emergency_contact(self):
    #    if self.age > 60 and "emergency" not in self.contact_details:
    #        raise ValueError("Patient > 60 need to have emergency contact")
    #    return self

#computed_field = when value is provided by the developer

def update_patient_data(patient: Patient):
    print(
        patient.name,
        patient.email,
        patient.age,
        patient.weight,
        patient.height,
        patient.calculate_bmi,
        patient.married,
        patient.allergies,
        patient.contact_details,
    )
    print("Updated")


updated_patient_info = {
    "name": "Priyanshu Raj",
    "email": "iamdevpriyanshu@gmail.com",
    "linked_in": "http://linked.com",
    "age": 24,
    "weight": 100.01,
    "height": 1.30,
    "married": False,
    "allergies": ["smoke", "dust"],
    "contact_details": {
        "email": "iamdevpriyanshu@gmail.com",
        "phone": "+916204482220",
    },
}

patient2 = Patient(**updated_patient_info)
update_patient_data(patient2)