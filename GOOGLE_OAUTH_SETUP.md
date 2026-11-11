# Google OAuth Setup Guide for CityFinder

This guide will help you set up Google OAuth authentication for your CityFinder application.

## Step-by-Step Instructions

### 1. Access Google Cloud Console

**Direct Link:** [Google Cloud Console - API Credentials](https://console.cloud.google.com/apis/credentials)

Or manually navigate:
1. Go to: https://console.cloud.google.com/
2. Click on "APIs & Services" in the left sidebar
3. Click on "Credentials"

### 2. Create or Select a Project

- If you don't have a project:
  - Click the project dropdown at the top
  - Click "New Project"
  - Enter project name (e.g., "CityFinder")
  - Click "Create"
  
- If you already have a project, select it from the dropdown

### 3. Configure OAuth Consent Screen (First Time Only)

Before creating credentials, you need to configure the OAuth consent screen:

1. Click on "OAuth consent screen" in the left sidebar
2. Choose "External" (for testing with any Google account) or "Internal" (if you have Google Workspace)
3. Click "Create"
4. Fill in the required information:
   - **App name:** CityFinder
   - **User support email:** Your email
   - **Developer contact email:** Your email
5. Click "Save and Continue"
6. On the "Scopes" page, click "Save and Continue" (default scopes are fine)
7. On "Test users" (if External), add your Google email for testing
8. Click "Save and Continue"
9. Review and click "Back to Dashboard"

### 4. Create OAuth 2.0 Client ID

1. Go back to "Credentials" in the left sidebar
2. Click "+ CREATE CREDENTIALS" at the top
3. Select "OAuth client ID"
4. For **Application type**, select "Web application"
5. Enter a name (e.g., "CityFinder Web Client")
6. Under **Authorized JavaScript origins**, click "+ ADD URI" and add:
   ```
   http://localhost:5000
   ```
7. Under **Authorized redirect URIs**, click "+ ADD URI" and add:
   ```
   http://localhost:5000/auth/google
   ```
8. Click "CREATE"

### 5. Get Your Client ID

After creating the OAuth client:
1. A dialog will appear showing your **Client ID** and **Client Secret**
2. **Copy the Client ID** - it will look like:
   ```
   1234567890-abc123def456.apps.googleusercontent.com
   ```
3. You can also find it anytime by:
   - Going to Credentials page
   - Looking under "OAuth 2.0 Client IDs"
   - Clicking on your client name

### 6. Update Your .env File

1. Open the `.env` file in your CityFinder project
2. Replace the placeholder with your actual Client ID:
   ```
   GOOGLE_CLIENT_ID=YOUR_ACTUAL_CLIENT_ID_HERE.apps.googleusercontent.com
   ```
3. Save the file

### 7. Restart Your Application

If the Flask app is already running:
1. Stop it (Ctrl+C in the terminal)
2. Start it again:
   ```bash
   py app.py
   ```

### 8. Test the Login

1. Open your browser and go to: http://localhost:5000
2. Click on "Sign in with Google"
3. You should see the Google sign-in page
4. Sign in with your Google account
5. Grant the requested permissions
6. You should be redirected to the dashboard

## Important Notes

### For Production Deployment

When you're ready to deploy your app to production:

1. Add your production domain to **Authorized JavaScript origins**:
   ```
   https://yourdomain.com
   ```

2. Add your production redirect URI to **Authorized redirect URIs**:
   ```
   https://yourdomain.com/auth/google
   ```

3. Update the OAuth consent screen with:
   - Verified domain
   - Privacy policy URL
   - Terms of service URL

4. Submit for verification if you need access to sensitive scopes

### Security Tips

- **Never commit your `.env` file** to version control (it's already in `.gitignore`)
- Keep your Client Secret confidential (you don't need it for this app since it uses client-side OAuth)
- For production, use environment variables or secret management services

## Troubleshooting

### Error: "The OAuth client was not found"
- Make sure you've copied the entire Client ID including `.apps.googleusercontent.com`
- Verify the Client ID is correctly pasted in your `.env` file
- Restart your Flask application after updating `.env`

### Error: "redirect_uri_mismatch"
- Ensure `http://localhost:5000` is added to Authorized JavaScript origins
- Ensure `http://localhost:5000/auth/google` is added to Authorized redirect URIs
- The URLs must match exactly (including http/https and port number)

### Error: "Access blocked: This app's request is invalid"
- Complete the OAuth consent screen configuration
- Make sure you've added yourself as a test user (if using External user type)

## Quick Reference Links

- [Google Cloud Console](https://console.cloud.google.com/)
- [API Credentials Page](https://console.cloud.google.com/apis/credentials)
- [OAuth Consent Screen](https://console.cloud.google.com/apis/credentials/consent)
- [Google OAuth Documentation](https://developers.google.com/identity/oauth2/web/guides/get-google-api-clientid)

---

**Need Help?** If you encounter any issues, check the troubleshooting section above or refer to the [official Google OAuth documentation](https://developers.google.com/identity/oauth2/web/guides/get-google-api-clientid).
