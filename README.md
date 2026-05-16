# KhidmatAI - Agentic Service Orchestrator for the Informal Economy (Challenge 2)

KhidmatAI is an AI-powered home services orchestration platform tailored for Pakistan's informal economy sectors (modeled for G-13/G-10 Islamabad). The application empowers local, non-tech-savvy technicians by automating end-to-end booking logic, intent extraction, and down-stream tracking through multi-agent workflows.

---

## 🚀 Core Architecture (Google Antigravity Platform Layout)
The core backend runs a distributed **Multi-Agent Orchestration Network** built natively inside the Vertex AI Agent Builder ecosystem:

1. **Intent Extraction Agent:** Parses messy contextual inputs in English, Urdu, and Roman Urdu (e.g., *'mujay Kal subah G-13 mein AC technician chahiye'*) to structure core token parameters.
2. **Provider Matching Agent:** Queries and ranks verified local technicians dynamically based on localized sector parameters, current availability, and ratings.
3. **Booking Manager Agent:** Simulates calendar/slot allocation constraints and locks the assignment under a unique tracking hash (`BK-XXXX`).
4. **Automated Follow-up Agent:** Handles asynchronous downstream triggers, generating structured text milestones (1-hour reminders, en-route warnings, and post-service feedback collection strings).
5. **Master Orchestrator State Controller:** Manages structural trace validation across the sub-agents to provide 100% processing transparency.

---

## 📱 Mobile Client Integration & Security
- **Frontend Framework:** Standalone Android Application (Native Java, API 24+) built using Material Design 3 guidelines.
- **Enterprise Handshake:** Bypasses basic static API limits by using a cryptographically secure, self-signed **IAM JWT Service Account Token** framework mapping connection metrics directly back to Google Cloud Enterprise Infrastructure logs under official hackathon credits.

---

## 🛠️ How to Test & Deploy Locally

### Prerequisites
- Android Studio (Ladybug or newer)
- Android Physical Device or Emulator (API 24+)
- Active Google Cloud Project with Agent Platform API enabled.

### Setup Instructions
1. Clone the repository to your local directory:
   ```bash
   git clone [https://github.com/OWAISARSHED/KhidmatAI-Agentic-Orchestrator.git](https://github.com/OWAISARSHED/KhidmatAI-Agentic-Orchestrator.git)

   Open the cloned folder inside Android Studio.

Let Gradle sync completely.

Ensure your Service Account JSON credentials match the configuration definitions inside MainActivity.java (PROJECT_ID, CLIENT_EMAIL, and PRIVATE_KEY).

Connect your test device and press Shift + F10 to compile and run the application.

📊 Live Orchestration Layout
When a user submits a request, the standalone client automatically maps and updates the layout frame using specific agent sequence tags:

Plaintext
╔══════════════════════════════╗
   KhidmatAI - Request Complete
╚══════════════════════════════╝
📋 REQUEST DETAILS -> [Extracted parameters]
👨‍🔧 MATCHED PROVIDER -> [Ranked algorithm logic]
✅ BOOKING CONFIRMED -> [Secure Token logged]
🔔 FOLLOW-UP SEQUENCE -> [Automated alerts mapped]
Developed for the #AISeekho2026 Antigravity Hackathon. Bridging the gap between formal enterprise infrastructure and the informal economy.
