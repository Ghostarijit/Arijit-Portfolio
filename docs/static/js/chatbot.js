// Chatbot for Arijit's Portfolio
const chatbotToggle = document.getElementById('chatbot-toggle');
const chatbot = document.getElementById('chatbot');
const chatbotClose = document.getElementById('chatbot-close');
const chatbotInput = document.getElementById('chatbot-input');
const chatbotSend = document.getElementById('chatbot-send');
const chatbotMessages = document.getElementById('chatbot-messages');

// Toggle chatbot
chatbotToggle.addEventListener('click', () => {
    chatbot.classList.toggle('active');
    const bubble = document.querySelector('.zudo-bubble');
    if (chatbot.classList.contains('active')) {
        chatbotInput.focus();
        if (bubble) bubble.style.display = 'none';
    } else {
        if (bubble) bubble.style.display = '';
    }
});

chatbotClose.addEventListener('click', () => {
    chatbot.classList.remove('active');
});

// Send message
chatbotSend.addEventListener('click', sendMessage);
chatbotInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});

function sendMessage() {
    const text = chatbotInput.value.trim();
    if (!text) return;

    addMessage(text, 'user');
    chatbotInput.value = '';

    // Show typing animation
    const typing = document.createElement('div');
    typing.className = 'chatbot-typing';
    typing.innerHTML = '<span></span><span></span><span></span>';
    chatbotMessages.appendChild(typing);
    chatbotMessages.scrollTop = chatbotMessages.scrollHeight;

    setTimeout(() => {
        typing.remove();
        const reply = getReply(text);
        addMessage(reply, 'bot');
    }, 800);
}

function addMessage(text, type) {
    const msg = document.createElement('div');
    msg.className = `chat-msg ${type}`;
    if (type === 'bot') {
        msg.innerHTML = text.replace(/\n/g, '<br>');
    } else {
        msg.textContent = text;
    }
    chatbotMessages.appendChild(msg);
    chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
}

// Knowledge base
const data = {
    name: "Arijit Biswas",
    role: "Team Lead & Senior Software Engineer",
    phone: "+91 8637572235",
    email: "arijitbiswas484@gmail.com",
    location: "Bengaluru, Karnataka, India",
    experience: "4+ years",
    company: "Synkcode (Client: Dubai Government – Customs Department)",
    previousCompany: "Bombay Softwares, Ahmedabad (Oct 2022 – Nov 2025)",
    availability: "Available for immediate joining",
    skills: "Python, Django, Flask, FastAPI, JavaScript, TypeScript, PostgreSQL, MongoDB, Redis, RabbitMQ, Celery, AWS (EC2, S3, Lambda), Docker, Git, Nginx, Gunicorn, WebSockets, TCP",
    projects: [
        "FitLife – Physiotherapy & Gamification Platform (Django, Celery, PostgreSQL, AWS S3)",
        "Sensor TCP Server – 50k+ events/day with Redis workers (Flask, Celery, Redis)",
        "ParkSpaceHub – Parking Space Sharing Platform (Flask, PostgreSQL, Leaflet.js)",
        "Product Analytics Dashboard – Return Rate & Prediction (Flask, Pandas, Chart.js)"
    ],
    achievements: [
        "15k+ secure transactions/day for Dubai Government customs",
        "28% faster API response time through optimization",
        "35% faster reporting pipelines with PostgreSQL optimization",
        "99.9% system uptime with monitoring",
        "50k+ IoT events/day TCP server",
        "Reduced AWS cost by $400/month",
        "Designed multi-tenant SaaS for 15+ clients"
    ],
    education: "B.Sc from Asutosh College (CGPA 7.37), ADCA from NBCE (CGPA 8.4)",
    github: "github.com/Ghostarijit",
    linkedin: "linkedin.com/in/arijit-biswas-a371b4179/"
};

function getReply(input) {
    const q = input.toLowerCase();

    // Greetings
    if (q.match(/^(hi|hello|hey|hii|namaste|sup|hola)/)) {
        return `Hey! 👋 I'm Zudo — Arijit's portfolio assistant. Ask me about his skills, experience, projects, or contact info!`;
    }

    // Name
    if (q.match(/name|who|kaun|kon/)) {
        return `He's ${data.name} — ${data.role} at ${data.company}.`;
    }

    // Contact
    if (q.match(/contact|email|mail|phone|number|call|reach/)) {
        return `📧 Email: ${data.email}\n📱 Phone: ${data.phone}\n📍 Location: ${data.location}\n${data.availability}!`;
    }

    // Experience
    if (q.match(/experience|work|company|job|career|kaam|kya karta/)) {
        return `${data.experience} of experience.\n\n🔹 Current: ${data.company} (Nov 2025 – Present) — Leading backend for customs systems, 15k+ txns/day.\n\n🔹 Previous: ${data.previousCompany} — Built REST/WebSocket APIs, TCP servers, multi-tenant SaaS.\n\n🔹 Started at FunctionUp as Backend Developer Trainee.`;
    }

    // Skills
    if (q.match(/skill|tech|stack|language|framework|kya aata|technology/)) {
        return `🛠️ Tech Stack:\n\n• Languages: Python, JavaScript, TypeScript\n• Backend: Django, Flask, FastAPI\n• Databases: PostgreSQL, MongoDB, MySQL\n• Systems: Redis, RabbitMQ, Celery, WebSockets, TCP\n• Cloud: AWS (EC2, S3, Lambda), Docker, Nginx, Gunicorn`;
    }

    // Projects
    if (q.match(/project|built|banaya|portfolio/)) {
        return `📂 Key Projects:\n\n${data.projects.map((p, i) => `${i+1}. ${p}`).join('\n')}\n\nCheck the Projects section above for details!`;
    }

    // Achievements
    if (q.match(/achieve|accomplish|result|impact|number|stats/)) {
        return `🏆 Key Achievements:\n\n${data.achievements.map(a => `• ${a}`).join('\n')}`;
    }

    // Education
    if (q.match(/education|college|degree|study|padhai|qualification/)) {
        return `🎓 ${data.education}`;
    }

    // Availability / Hiring
    if (q.match(/available|hire|join|hiring|notice|joining/)) {
        return `✅ ${data.availability}! Reach out at ${data.email} or ${data.phone}.`;
    }

    // Location
    if (q.match(/location|city|where|kaha|based/)) {
        return `📍 Based in ${data.location}.`;
    }

    // GitHub / LinkedIn
    if (q.match(/github|linkedin|social|profile|link/)) {
        return `🔗 GitHub: ${data.github}\n🔗 LinkedIn: ${data.linkedin}`;
    }

    // Python / Django specific
    if (q.match(/python|django|flask|fastapi/)) {
        return `Python is Arijit's primary language with 4+ years of hands-on experience. He works with Django (current role — government customs systems), Flask (TCP servers, parking platform), and FastAPI. Expert in building scalable REST APIs, background jobs with Celery, and PostgreSQL optimization.`;
    }

    // AWS / Cloud
    if (q.match(/aws|cloud|docker|deploy|devops/)) {
        return `☁️ Cloud & DevOps:\n• AWS: EC2, S3, Lambda\n• Docker + Nginx + Gunicorn for zero-downtime deployments\n• CI/CD pipelines for automated tests & EC2 deployments\n• Reduced AWS cost by $400/month through optimization`;
    }

    // Database
    if (q.match(/database|postgres|sql|mongo|redis|db/)) {
        return `🗄️ Database expertise:\n• PostgreSQL — indexes, partitioning, CTEs, window functions (30-35% faster queries)\n• MongoDB — used with Node.js projects\n• Redis — caching, real-time workers\n• MySQL — general experience`;
    }

    // Salary (polite decline)
    if (q.match(/salary|ctc|package|compensation|pay/)) {
        return `💼 For salary discussions, please reach out directly at ${data.email}. Happy to discuss!`;
    }

    // Thanks
    if (q.match(/thank|thanks|dhanyawad|shukriya/)) {
        return `You're welcome! 😊 Feel free to ask anything else or reach out at ${data.email}.`;
    }

    // Default
    return `I can help with questions about Arijit's skills, experience, projects, education, or contact info. Try asking:\n\n• "What are his skills?"\n• "Tell me about his experience"\n• "What projects has he built?"\n• "How to contact him?"`;
}
