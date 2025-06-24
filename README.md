# Toxicity Detection App (Azure Ready)

This is a lightweight Flask application that uses a Hugging Face model (`unitary/toxic-bert`) to detect toxic content in user input. It includes logging, testing, simulated mode for Azure deployment, and a basic static front end for user interaction.

## Features
- `/analyze`: POST endpoint for toxicity detection
- `/health`: health check endpoint
- Static front-end to submit text
- Simulated mode using `SIMULATE_MODEL=true`
- GitHub Actions CI/CD
- Azure App Service deployable (Free Tier)

## Setup Locally
```bash
git clone <your-repo>
cd toxicity-detector-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export SIMULATE_MODEL=false
python main.py
```

## Run Tests
```bash
pytest
```

## Deploy to Azure
1. Create an **Azure App Service** (Linux, Python 3.9, Free Tier)
2. Go to **Deployment Center** > GitHub > Connect your repo
3. Add secrets in GitHub repo:
   - `AZURE_WEBAPP_NAME`: Your app name
   - `AZURE_WEBAPP_PUBLISH_PROFILE`: From Azure portal > Get Publish Profile
4. Push to `main` branch to trigger deploy.

## Simulated Mode for Azure
Set the following app setting in Azure:
```
SIMULATE_MODEL=true
```
This bypasses model loading and returns mock responses for cost-free testing.

---

## API Usage
### POST /analyze
```json
{
  "text": "You're awful."
}
```
### Response
```json
[
  { "label": "toxic", "score": 0.89 }
]
```

### GET /health
Returns `{"status": "healthy"}`

---

## Static Frontend
A basic HTML frontend is available at the root path `/`. Users can paste text and click a button to evaluate toxicity in real-time.

---

## License
MIT
