from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Annotated, Literal
from config.city_tier import tier_1_cities, tier_2_cities 


#pydantic model to validate incoming data
class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, description="Age of the user in years", example=30)] 
    weight:Annotated[float, Field(..., gt=0, description="Weight of the user in kilograms", example=70.0)]
    height: Annotated[float, Field(..., gt=0, description="Height of the user in centimeters", example=175.0)]
    income_lpa: Annotated[float, Field(..., gt=0, description="Income of the user in lakhs per annum", example=5.0)]
    smoker: Annotated[bool, Field(..., description="Whether the user is a smoker", example="true")]
    city: Annotated[str, Field(..., description="City of residence", example="Mumbai")]
    occupation: Annotated[Literal["retired", "freelancer", "student", "government_job", "business_owner", "unemployed", "private_job"], Field(..., description="Occupation of the user", example="retired")]

    @field_validator('city')
    @classmethod
    def normalize_city(cls, v: str) -> str:
        v =  v.strip().title()
        return v
    
    
    @computed_field
    @property
    def bmi(self) -> float:
        height_in_meters = self.height / 100
        return round(self.weight / (height_in_meters ** 2), 2) 
    

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3