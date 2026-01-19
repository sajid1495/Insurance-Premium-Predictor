# Insurance Premium Predictor API

A FastAPI-based REST API that predicts insurance premium categories (low, medium, high) using machine learning. The API takes user health and demographic information and returns a premium prediction with confidence scores.

## 🚀 Features

- **Machine Learning Prediction**: Uses a trained ML model to predict insurance premium categories
- **Input Validation**: Pydantic-based schema validation for all inputs
- **Computed Fields**: Automatically calculates BMI, lifestyle risk, age group, and city tier
- **Confidence Scores**: Returns prediction confidence and probabilities for all classes
- **Health Check Endpoint**: Monitor API and model status

## 📁 Project Structure

```
insurance_premium_predictor/
├── main.py                     # FastAPI application entry point
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── Dockerfile                  # Docker container configuration
├── .gitignore                  # Git ignore rules
├── config/
│   └── city_tier.py            # City tier classifications (Tier 1, 2, 3)
├── model/
│   ├── model.pkl               # Trained ML model
│   └── predict.py              # Prediction logic
└── schema/
    ├── user_input.py           # Input validation schema
    └── prediction_response.py  # Response schema
```

## 🛠️ Installation

### Prerequisites
- Python 3.10+
- pip

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/sajid1495/Insurance-Premium-Predictor.git
   cd Insurance-Premium-Predictor
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Running the API

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## 🐳 Docker

### Build the Docker Image

```bash
docker build -t insurance-premium-predictor .
```

### Run the Container

```bash
docker run -d -p 8000:8000 insurance-premium-predictor
```

The API will be available at `http://localhost:8000`

## 📚 API Endpoints

### `GET /`
Welcome message

**Response:**
```json
{
  "message": "Welcome to the Insurance Premium Prediction API!"
}
```

### `GET /health`
Health check endpoint to verify API and model status

**Response:**
```json
{
  "status": "OK",
  "model_version": "1.0.0",
  "model_loaded": true
}
```

### `POST /predict`
Predict insurance premium category based on user input

**Request Body:**
```json
{
  "age": 30,
  "weight": 70.0,
  "height": 175.0,
  "income_lpa": 5.0,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

**Input Parameters:**

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `age` | int | Age in years (>0) | 30 |
| `weight` | float | Weight in kg (>0) | 70.0 |
| `height` | float | Height in cm (>0) | 175.0 |
| `income_lpa` | float | Annual income in lakhs (>0) | 5.0 |
| `smoker` | bool | Smoking status | true/false |
| `city` | string | City of residence | "Mumbai" |
| `occupation` | string | User's occupation | See options below |

**Occupation Options:**
- `retired`
- `freelancer`
- `student`
- `government_job`
- `business_owner`
- `unemployed`
- `private_job`

**Response:**
```json
{
  "response": {
    "prediction": "medium",
    "confidence": 0.7523,
    "class_probabilities": {
      "low": 0.1234,
      "medium": 0.7523,
      "high": 0.1243
    }
  }
}
```

## 🧮 Computed Fields

The API automatically computes the following fields from user input:

| Field | Formula/Logic |
|-------|---------------|
| **BMI** | `weight / (height_in_meters)²` |
| **Age Group** | `young` (<25), `adult` (25-44), `middle_aged` (45-59), `senior` (60+) |
| **Lifestyle Risk** | `high` (smoker + BMI>30), `medium` (smoker OR BMI>27), `low` (otherwise) |
| **City Tier** | `tier_1` (metros), `tier_2` (major cities), `tier_3` (others) |

## 🏙️ City Tier Classification

**Tier 1 Cities:** Mumbai, Delhi, Bangalore, Chennai, Kolkata, Hyderabad, Pune

**Tier 2 Cities:** Jaipur, Chandigarh, Indore, Lucknow, Patna, Ranchi, Visakhapatnam, Coimbatore, Bhopal, Nagpur, and more...

**Tier 3 Cities:** All other cities

## 📖 API Documentation

Once the server is running, access the interactive API documentation:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## 🧪 Tech Stack

- **FastAPI** - Modern, fast web framework
- **Pydantic** - Data validation using Python type annotations
- **Pandas** - Data manipulation
- **Scikit-learn** - Machine learning (model)
- **Uvicorn** - ASGI server

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
