# Persional_API  
  
This project is a FastAPI-based API starter with user management, file storage, analytics, custom business logic, database, email, and third-party API integration.  
  
## Features  
- JWT Authentication (\`/token\`, \`/users/me\`, \`/register\`)  
- SQLite (dev) / Postgres-ready database  
- Email sending support (\`/send-test-email\`)  
- Third-party API integration example (\`/external/joke\`)  
- Example endpoints for extensibility (\`/analytics/hits\`, \`/uploadfile/\`)  
- Dockerfile for deployment  
  
## Local Development  
1. Install dependencies:  
   \`\`\`bash  
   pip install -r requirements.txt  
   \`\`\`  
2. Copy .env.example to .env and update secrets/configs as needed.  
3. Initialize the database tables:  
   \`\`\`bash  
   python -m app.init_db  
   \`\`\`  
4. Run the server:  
   \`\`\`bash  
   uvicorn app.main:app --reload  
   \`\`\`  
  
## Deployment  
- Recommended free/low-cost hosts: Render, Railway  
 
Post-deploy checklist

- Verify the live site at: https://<your-service>.onrender.com/docs
- Create a managed Postgres on Render (if you need production persistence) and set the `DATABASE_URL` env var in the Render service to the value Render provides.
- Add the following secrets to your GitHub repo (Settings → Secrets → Actions):
   - `RENDER_API_KEY` — Render API key with deploy permission
   - `RENDER_SERVICE_ID` — Render service ID for your web service
- After setting `DATABASE_URL` on Render, run the migration script to initialize the DB:

   ```bash
   # locally (for testing):
   python scripts/run_migrations.py

   # In CI / Render shell, ensure PYTHONPATH covers the project root and run the same script
   ```

CI / GitHub Actions

- A CI workflow is included at `.github/workflows/ci.yml` which installs dependencies and runs pytest on pushes/PRs to `main`.
- A deploy workflow is included at `.github/workflows/deploy.yml` which runs tests and optionally triggers a Render deploy if you add the `RENDER_API_KEY` and `RENDER_SERVICE_ID` secrets.
  
## Environment Variables  
See .env.example for required variables and sample values.  
  
## Extending  
- Add new endpoints in app/main.py or as new modules in app/  
- Update database models in app/models.py  
- Add business logic in app/crud.py or new modules  
  
---  
MIT License  
