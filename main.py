"""
Insurance Premium Calculator API

This API calculates insurance premiums based on age, risk level, and coverage amount.
Formula: Premium = Base × (1 + AgeFactor) × (1 + RiskLoading)
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from typing import Literal
from enum import Enum

# Initialize FastAPI application
app = FastAPI(
    title="Insurance Premium Calculator",
    description="Calculate insurance premiums based on age, risk level, and coverage",
    version="1.0.0"
)


# Pydantic Models - Think of these as "data validation templates"
# Just like Excel data validation rules, these ensure data quality before processing

class RiskLevel(str, Enum):
    """Risk level categories - like dropdown options in a form"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class PremiumRequest(BaseModel):
    """
    Input validation model - defines what data clients must send
    
    This is like a data entry form with built-in validation rules:
    - Age must be a whole number between 0-120
    - Risk level must be one of: low, medium, high
    - Coverage must be a positive number
    """
    age: int = Field(
        ...,  # Required field (the ... means "no default value")
        ge=0,  # Greater than or equal to 0
        le=120,  # Less than or equal to 120
        description="Age of the insured person (0-120 years)"
    )
    risk_level: RiskLevel = Field(
        ...,
        description="Risk assessment level: low, medium, or high"
    )
    coverage: float = Field(
        ...,
        gt=0,  # Greater than 0 (must be positive)
        description="Coverage amount in currency (must be positive)"
    )
    
    class Config:
        """Configuration for the model - provides example data for API docs"""
        schema_extra = {
            "example": {
                "age": 35,
                "risk_level": "medium",
                "coverage": 100000
            }
        }


class PremiumResponse(BaseModel):
    """
    Output model - defines what the API returns
    
    Provides a detailed breakdown of the calculation for transparency
    """
    base_premium: float = Field(description="Base premium amount")
    age_factor: float = Field(description="Age-based multiplier (as decimal, e.g., 0.10 = 10%)")
    risk_loading: float = Field(description="Risk-based multiplier (as decimal)")
    final_premium: float = Field(description="Calculated total premium")
    coverage: float = Field(description="Coverage amount")
    breakdown: str = Field(description="Human-readable calculation breakdown")


# Business Logic Functions

def calculate_age_factor(age: int) -> float:
    """
    Calculate age-based risk factor
    
    Age ranges and their corresponding factors:
    - 0-25 years: 0% increase (factor = 0.0)
    - 26-40 years: 10% increase (factor = 0.10)
    - 41-60 years: 25% increase (factor = 0.25)
    - 61+ years: 50% increase (factor = 0.50)
    
    Returns:
        float: Age factor as a decimal (e.g., 0.10 for 10%)
    """
    if age <= 25:
        return 0.0
    elif age <= 40:
        return 0.10
    elif age <= 60:
        return 0.25
    else:
        return 0.50


def calculate_risk_loading(risk_level: RiskLevel) -> float:
    """
    Calculate risk-based loading factor
    
    Risk levels and their loadings:
    - Low: 0% increase (factor = 0.0)
    - Medium: 20% increase (factor = 0.20)
    - High: 50% increase (factor = 0.50)
    
    Returns:
        float: Risk loading as a decimal
    """
    risk_loadings = {
        RiskLevel.LOW: 0.0,
        RiskLevel.MEDIUM: 0.20,
        RiskLevel.HIGH: 0.50
    }
    return risk_loadings[risk_level]


def calculate_premium(age: int, risk_level: RiskLevel, coverage: float, base: float = 1000.0) -> dict:
    """
    Calculate insurance premium using the formula:
    Premium = Base × (1 + AgeFactor) × (1 + RiskLoading)
    
    Args:
        age: Age of the insured
        risk_level: Risk assessment level
        coverage: Coverage amount
        base: Base premium amount (default: $1000)
    
    Returns:
        dict: Calculation results with breakdown
    """
    age_factor = calculate_age_factor(age)
    risk_loading = calculate_risk_loading(risk_level)
    
    # Apply the formula
    final_premium = base * (1 + age_factor) * (1 + risk_loading)
    
    # Create human-readable breakdown
    breakdown = (
        f"Base: ${base:,.2f} × "
        f"(1 + {age_factor:.2f}) × "
        f"(1 + {risk_loading:.2f}) = "
        f"${final_premium:,.2f}"
    )
    
    return {
        "base_premium": base,
        "age_factor": age_factor,
        "risk_loading": risk_loading,
        "final_premium": round(final_premium, 2),
        "coverage": coverage,
        "breakdown": breakdown
    }


# API Endpoints

@app.get("/")
async def root():
    """Root endpoint - provides API information"""
    return {
        "message": "Insurance Premium Calculator API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "calculate": "POST /calculate - Calculate insurance premium"
        }
    }


@app.post("/calculate", response_model=PremiumResponse)
async def calculate_premium_endpoint(request: PremiumRequest):
    """
    Calculate insurance premium based on age, risk level, and coverage
    
    This endpoint:
    1. Receives data (Pydantic automatically validates it)
    2. If invalid, returns error with details (Pydantic handles this)
    3. If valid, calculates premium using the formula
    4. Returns detailed breakdown
    
    Args:
        request: PremiumRequest object with age, risk_level, and coverage
    
    Returns:
        PremiumResponse: Calculated premium with detailed breakdown
    
    Raises:
        HTTPException: If calculation fails (422 for validation errors handled by Pydantic)
    """
    try:
        # Calculate premium
        result = calculate_premium(
            age=request.age,
            risk_level=request.risk_level,
            coverage=request.coverage
        )
        
        return PremiumResponse(**result)
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error calculating premium: {str(e)}"
        )


# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy", "service": "insurance-premium-calculator"}
