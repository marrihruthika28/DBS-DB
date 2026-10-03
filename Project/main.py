# =====================================================================
# CAPACITY CONNECT — FASTAPI ANALYTICS & SKILL INTELLIGENCE SERVICE
# Concept: CO3 (FastAPI, Pydantic, Dependency Injection, JWT Security, OpenAPI)
# =====================================================================

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import jwt

# CO3: FastAPI application instance with automated OpenAPI Swagger documentation
app = FastAPI(
    title="Capacity Connect — Skill Intelligence & Assessment API",
    description="CO3 microservice with Pydantic validation & dynamic course-specific skill gap detection",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBearer()
SECRET_KEY = "enterprise_capacity_jwt_secret_key"
ALGORITHM = "HS256"

# CO3: Dependency Injection for JWT Authentication
def verify_jwt_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="CO3: Invalid or expired JWT token"
        )

# CO3: Pydantic models for request & response validation
class CourseSkillRequirement(BaseModel):
    skill: str = Field(..., example="Python OOP")
    required_level: int = Field(..., ge=1, le=5, example=4)

class TraineeSkillCompetency(BaseModel):
    skill: str = Field(..., example="Python OOP")
    current_level: int = Field(..., ge=0, le=5, example=2)

class CourseSkillGapRequest(BaseModel):
    course_id: str
    course_title: str
    enrolled_skills: List[CourseSkillRequirement]
    trainee_competencies: List[TraineeSkillCompetency]

class SkillGapItem(BaseModel):
    skill: str
    current_level: int
    required_level: int
    gap: int
    priority: str
    recommendation: str

class CourseSkillGapResponse(BaseModel):
    course_id: str
    course_title: str
    overall_readiness_pct: float
    gap_breakdown: List[SkillGapItem]

# CO3: REST API endpoint using Dependency Injection and Pydantic validation
@app.post("/api/v1/analytics/course-skill-gap", response_model=CourseSkillGapResponse)
def calculate_course_skill_gap(
    request: CourseSkillGapRequest, 
    user: dict = Depends(verify_jwt_token)
):
    """
    CO3: Dynamic Course-Specific Skill-Gap Detection.
    Evaluates trainee against competencies required by their enrolled course,
    rather than a generic external role.
    """
    trainee_map = {item.skill.lower(): item.current_level for item in request.trainee_competencies}
    
    breakdown = []
    total_required = 0
    total_acquired = 0

    for req in request.enrolled_skills:
        curr = trainee_map.get(req.skill.lower(), 1)
        gap = max(0, req.required_level - curr)
        
        total_required += req.required_level
        total_acquired += min(curr, req.required_level)

        if gap >= 2:
            priority = "High"
            recommendation = f"Urgent focus required on {req.skill} before advanced assessments."
        elif gap == 1:
            priority = "Medium"
            recommendation = f"Review foundational modules for {req.skill}."
        else:
            priority = "Satisfied"
            recommendation = f"Meets or exceeds target competency for {req.skill}."

        breakdown.append(SkillGapItem(
            skill=req.skill,
            current_level=curr,
            required_level=req.required_level,
            gap=gap,
            priority=priority,
            recommendation=recommendation
        ))

    readiness = round((total_acquired / max(1, total_required)) * 100, 1)

    return CourseSkillGapResponse(
        course_id=request.course_id,
        course_title=request.course_title,
        overall_readiness_pct=readiness,
        gap_breakdown=breakdown
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
