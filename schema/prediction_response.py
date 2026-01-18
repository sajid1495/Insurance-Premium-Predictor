from pydantic import BaseModel, Field, computed_field
from typing import List, Literal

#pydantic model to structure prediction response
class PredictionResponse(BaseModel):
    prediction: Literal["low", "medium", "high"] = Field(..., description="Predicted insurance premium category")
    confidence: float = Field(..., description="Confidence score of the prediction")
    class_probabilities: dict = Field(..., description="Probabilities for each insurance premium category")
    
    @computed_field
    @property
    def model_version(self) -> str:
        return "1.0.0"  
    
    @computed_field
    @property
    def notes(self) -> str:
        return "This prediction is based on the provided user input and the trained machine learning model."
    
    