# CAPACITY CONNECT — Final Full-Stack Implementation

> **Empowering People, Skills & Organizational Growth**

CAPACITY CONNECT is an enterprise-grade digital capacity building and learning management portal engineered with a clean, minimal White + Blue design system, zero mock data, real-time multi-user synchronization, and full polyglot distributed architecture.

---

## 📂 Git Repository Structure

This repository is organized into three clean, independently deployable tiers:

```
capacity-connect-final-draft/
├── frontend/                     # Minimal White + Blue Enterprise React Application
│   ├── src/                      # UI Components, Pages & Real-time State Services
│   ├── package.json              # Frontend dependencies (React 19, Tailwind v4, jsPDF)
│   └── README.md
├── backend/                      # Distributed Multi-Language Microservices
│   ├── spring-boot/              # Java Spring Boot enterprise service (CO4, CO5)
│   │   ├── pom.xml
│   │   └── src/main/java/com/capacityconnect/...
│   ├── fastapi/                  # Python FastAPI skill-gap intelligence service (CO3)
│   │   ├── main.py
│   │   └── requirements.txt
│   ├── nodejs-gateway/           # Node.js API Gateway & Real-time Broadcaster (CO4)
│   │   └── server.ts
│   ├── Dockerfile                # Multi-stage production container build (CO6)
│   └── docker-compose.yml        # Full system multi-container orchestration (CO6)
├── database/                     # Relational & Polyglot Database Definitions
│   ├── schema.sql                # MySQL Workbench 8.0+ Normalized Schema & CTEs (CO1)
│   ├── mongodb_schema.js         # MongoDB Real-time Chat Document Store (CO2)
│   ├── vector_search.sql         # pgvector Semantic Embeddings & Cosine Search (CO2)
│   └── README.md                 # MySQL Workbench execution instructions
└── docs/
    └── CO_MAPPING.md             # Detailed Course Outcome (CO1 - CO6) Technical Mapping
```

---

## 🎯 Targeted Requirements & Modifications Implemented

1. **Homepage Tagline**:
   - Replaced old tagline with: `"Empowering People, Skills & Organizational Growth"`.
   - Brand Title: `CAPACITY CONNECT`.
   - Opens to public homepage when unauthenticated (never auto-logs in as admin).
2. **Header**:
   - Removed `"ENTERPRISE LMS"` completely.
   - Includes real-time notification badge, instant role switcher, and 1-click **Git Package** export button.
3. **Master Admin & Co-Admin Protocol**:
   - Master Admin: **K. Gayathri Srivalli** (`gayathri@gmail.com`).
   - No hardcoded password; authenticates via real authentication system.
   - Non-admin users submit a Co-Admin request with justification.
   - Master Admin receives a real-time notification with requester details, timestamp, and **Approve / Decline** buttons.
   - Requesters never receive Master Admin PINs or credentials.
4. **Trainee Dashboard**:
   - Removed generic *"AI Skill-Gap Intelligence"* card from the dashboard home.
   - Removed *"AI Learning Assistant"* completely from the application.
   - Removed *"Real-Time Sync"* box under Trainee Portal sidebar.
   - Dashboard contains only **My Learning** (no `+ Create Course` in trainee dashboard).
   - Renamed *"Secure Assessments"* to **Assessments**.
   - Trainee can **ONLY** take assessments authored by trainers who accepted their skill exchange request for that course.
   - Dynamic **Course-Specific Skill-Gap Detection**: Compares trainee competencies directly against the enrolled course requirements.
   - Minimalist, high-quality downloadable **PDF Certificates** via jsPDF.
5. **Trainer Dashboard**:
   - Removed *"AI Learning Assistant"* completely.
   - In Trainees & Skill Requests: View incoming proposals (*"I want to learn X, I can teach Y"*), with real **Accept** and **Decline** actions.
   - Real-time synchronization: Trainee immediately sees *"Request Accepted"* or *"Request Declined"*.
   - In Course Management: Removed *"My Learning"*; trainers only create, publish, and manage courses.
   - In Certificates: Shows certificates issued to trainees once work is completed, with an **Issue Certificate** modal.
   - Public visibility: Trainer profiles are immediately publicly visible to all trainees in the Trainer Directory.
6. **Admin Dashboard**:
   - Removed *"Competency Standards"* completely.
   - **Course Oversight**: View and **Delete** any published course across any trainer.
   - **Assessments Log**: View and **Delete** assessments published by any trainer, and review trainee scores.
   - **Knowledge Moderation**: Review, approve, reject, or **Delete** resources uploaded by trainers.
   - **Issued Credentials**: View and **Delete** any certificate issued across the platform.
7. **Zero Mock Data Guarantee**:
   - Database starts completely clean with no fake trainers, courses, or assessments. Real records created from the UI persist and update live.

---

## 🎓 Course Outcome (CO1 - CO6) Technical Highlights

- **CO1 (SQL & Normalization)**: `/database/schema.sql` contains 13 normalized tables with foreign keys, cascading rules, `vw_trainee_course_skill_gaps` Common Table Expression (CTE), and `vw_trainee_assessment_rankings` Window Functions (`RANK()`, `DENSE_RANK()`, `AVG()`).
- **CO2 (NoSQL & Vector Storage)**: Document schema for real-time chat in `/database/mongodb_schema.js` and pgvector HNSW cosine similarity search in `/database/vector_search.sql`.
- **CO3 (FastAPI & Pydantic)**: Dynamic course-specific skill-gap calculation with Pydantic request validation and JWT dependency injection in `/backend/fastapi/main.py`.
- **CO4 (Spring Boot & Node.js)**: Spring Boot REST controllers in `/backend/spring-boot/` and Node.js real-time event streaming in `server.ts`.
- **CO5 (Microservices & Kafka)**: Asynchronous event publishing (`TrainerRequestAccepted`, `AssessmentSubmitted`) via `KafkaProducerService.java`.
- **CO6 (Docker & CI/CD)**: Complete multi-service orchestration in `/backend/docker-compose.yml` and GitHub Actions pipeline in `/.github/workflows/ci-cd.yml`.

---

## 🚀 Pushing to Git

To push the clean separated codebase to your Git repository:

```bash
git init
git add frontend/ backend/ database/ docs/ README.md .github/
git commit -m "feat: capacity connect final draft - frontend, backend, database"
git branch -M main
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```
