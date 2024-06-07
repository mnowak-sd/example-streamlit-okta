# Example Streamlit Okta

## Setup

### Configure Okta

Setup an Okta Application Registration,

1. Create an Okta Developer Account at https://developer.okta.com/
2. Sign in and go to your dashboard, for example: https://dev-72969785-admin.okta.com/admin/getting-started
3. Navigate to 'Applications', then 'Create App Integration'
4. Select 'OIDC - OpenID Connect'
5. Select 'Web Application'
6. Add an 'App integration name'
7. Enable refresh tokens
8. Configure the 'Sign-in redirect URIs' using the same value configured in `.env.example` (below)
9. Set the 'Sign-out redirect URIs' to your application homepage
10. Optionally, set the base URI of your app as a Trusted Origin
11. Under 'Assignments' (if in your development environment; for ease of use) select 'Allow everyone in your organization to access'. _(Note: in production, you most likely will need assignments tied to group memberships configured for the app.)_

### Configure development environment

Setup the development dependencies,
```py
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

Configure the environment by setting values in `.env`, see `.env.example` for more details.

### Run and test

Start the streamlit application,
```
python -m streamlit run dashboard.py
```

Click the 'Sign in' button and sign in.

🎉