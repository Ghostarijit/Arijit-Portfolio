import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_project.settings")
django.setup()

from core.models import Profile, Skill, Experience, Project, Education, OnlineProfile

# Profile
Profile.objects.get_or_create(
    email="arijitbiswas484@gmail.com",
    defaults={
        "name": "Arijit Biswas",
        "title": "Senior Software Engineer",
        "phone": "+91 8637572235",
        "location": "Bengaluru, Karnataka, India",
        "linkedin": "https://linkedin.com/in/arijit-biswas-a371b4179/",
        "github": "https://github.com/Ghostarijit",
        "summary": "Available for immediate joining. Experienced Software Engineer (4+ years) specializing in Python, Flask, Django, FastAPI, real-time systems, scalable APIs, PostgreSQL optimization, Redis caching, AWS, and CI/CD.",
    },
)

# Skills
skills_data = [
    {"category": "Programming Languages", "skills": "Python, JavaScript, TypeScript", "order": 1},
    {"category": "Backend / Frontend", "skills": "Django, Flask, FastAPI, jQuery, DOM Manipulation, Basic React.js", "order": 2},
    {"category": "Databases", "skills": "PostgreSQL, MongoDB, MySQL", "order": 3},
    {"category": "Systems", "skills": "TCP, WebSockets, Redis, RabbitMQ, Celery", "order": 4},
    {"category": "Cloud/Tools", "skills": "AWS (EC2, S3, Lambda), Docker, Git, Nginx, Gunicorn, Linux", "order": 5},
]
for s in skills_data:
    Skill.objects.get_or_create(category=s["category"], defaults=s)

# Experience
experiences_data = [
    {
        "job_title": "Senior Software Engineer",
        "company": "Synkcode (Client: Dubai Government – Customs Department)",
        "location": "",
        "start_date": "Nov 2025",
        "end_date": "Present",
        "order": 1,
        "description": """Leading backend development for mission-critical customs systems processing 15k+ secure transactions/day across regulatory workflows.
Architected scalable Python & Django services reducing API response time by 28% through query optimization and caching strategies.
Optimized PostgreSQL queries, indexing, and execution plans resulting in 35% faster reporting pipelines and improved data retrieval efficiency.
Implemented AI-driven automation modules reducing manual verification workload by 25% and improving operational turnaround time.
Designed enterprise-grade RBAC and secure API layers improving system security posture and reducing unauthorized access risks by 40%.
Improved system uptime to 99.9% by introducing structured logging, monitoring, and proactive performance tuning.
Accelerated feature delivery cycle by 30% using CI/CD pipelines, code reviews, and GitHub Copilot-assisted development.
Collaborated with cross-functional government stakeholders to deliver scalable solutions aligned with compliance and audit requirements.""",
    },
    {
        "job_title": "Software Engineer",
        "company": "Bombay Softwares (Onsite)",
        "location": "Ahmedabad",
        "start_date": "Oct 2022",
        "end_date": "Nov 2025",
        "order": 2,
        "description": """Developed high-performance REST and WebSocket APIs handling 10k+ daily requests, improving response time by 35%.
Built scalable TCP servers processing 50k+ IoT events/day with retries, alerts & failover logic.
Designed multi-tenant SaaS backend for 15+ clients, reducing onboarding effort by 50%.
Reduced AWS cost by $400/month using Redis caching, CTE optimization & pooling.
Integrated Stripe subscription billing with webhook automation & fraud-safe workflows.
Optimized PostgreSQL using indexes, partitioning, window functions — resulting in 30% faster APIs.
Deployed production workloads using Docker + Nginx + Gunicorn enabling zero-downtime releases.
Implemented Celery + RabbitMQ pipelines for ETL, analytics, notifications & IoT event processing.
Created CI/CD pipelines for automated tests, builds, versioning & EC2 deployments.""",
    },
    {
        "job_title": "Backend Developer Trainee",
        "company": "FunctionUp (Remote)",
        "location": "",
        "start_date": "Mar 2022",
        "end_date": "Sep 2022",
        "order": 3,
        "description": """Built REST APIs using Node.js, Express, and MongoDB; implemented secure JWT authentication.
Selected as Top Performer and promoted to Teaching Assistant to guide backend batches.
Developed Python-based backend scripts and automation tools for data processing tasks.
Gained hands-on experience with Flask, PostgreSQL, Redis, and API testing workflows.
Collaborated with frontend teams and built small UI components using React.js for internal dashboards.""",
    },
]
for exp in experiences_data:
    Experience.objects.get_or_create(
        job_title=exp["job_title"], company=exp["company"], defaults=exp
    )

# Projects
projects_data = [
    {
        "title": "FitLife – Physiotherapy & Gamification Platform",
        "description": "SaaS backend for physiotherapists to assign AI-validated exercise plans, track progress, and manage corporate leaderboards. Built secure APIs, background jobs, and S3 upload workflows.",
        "tech_stack": "Python, Django, Celery, PostgreSQL, AWS S3",
        "github_link": "https://github.com/Ghostarijit",
        "live_link": "",
        "order": 1,
    },
    {
        "title": "Sensor TCP Server & Real-Time Config System",
        "description": "50k+ sensor events/day TCP server with zone thresholds, dynamic ping intervals, SMTP alerts, and async processing. Integrated real-time dashboards & Redis workers.",
        "tech_stack": "Python, Flask, Celery, Redis, PostgreSQL, AWS EC2",
        "github_link": "https://github.com/Ghostarijit",
        "live_link": "",
        "order": 2,
    },
    {
        "title": "ParkSpaceHub – Parking Space Sharing Platform",
        "description": "Full-stack app connecting parking owners with seekers. Features: secure auth, live chat, booking, map-based search, admin dashboard. Deployed with SSL + Nginx.",
        "tech_stack": "Python, Flask, PostgreSQL, Leaflet.js, AWS EC2, Nginx",
        "github_link": "https://github.com/Ghostarijit",
        "live_link": "",
        "order": 3,
    },
    {
        "title": "Product Analytics Dashboard – Return Rate & Prediction",
        "description": "Interactive dashboard to analyze product GMV, ratings, return contribution, and predictive insights. Includes charts, tables, and automated suggestion engine.",
        "tech_stack": "Flask, Pandas, Chart.js, PostgreSQL",
        "github_link": "https://github.com/Ghostarijit",
        "live_link": "",
        "order": 4,
    },
]
for proj in projects_data:
    Project.objects.get_or_create(title=proj["title"], defaults=proj)

# Education
education_data = [
    {
        "degree": "B.Sc",
        "institution": "Asutosh College, Calcutta University",
        "location": "Kolkata, India",
        "cgpa": "7.37",
        "year_range": "2018 – 2021",
        "order": 1,
    },
    {
        "degree": "ADCA (Advanced Diploma in Computer Applications)",
        "institution": "NBCE",
        "location": "Kolkata, India",
        "cgpa": "8.4",
        "year_range": "2021 – 2022",
        "order": 2,
    },
]
for edu in education_data:
    Education.objects.get_or_create(degree=edu["degree"], institution=edu["institution"], defaults=edu)

# Online Profiles
profiles_data = [
    {"platform": "LeetCode", "url": "https://leetcode.com/", "description": "Coding streaks, DS/Algo practice, optimised solutions", "order": 1},
    {"platform": "GeeksforGeeks", "url": "https://www.geeksforgeeks.org/", "description": "Articles, problem-solving history, badges", "order": 2},
]
for p in profiles_data:
    OnlineProfile.objects.get_or_create(platform=p["platform"], defaults=p)

print("Portfolio data loaded successfully!")
