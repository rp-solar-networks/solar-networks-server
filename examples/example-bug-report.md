# Example Bug Report

This is an example of a well-structured bug report that follows our guidelines.

## Title
Customer Portal login fails with 500 error after password reset

## System
Customer Portal (Web Application)

## Severity
High - Users cannot access their accounts after password reset

## Description
When users attempt to log in after completing a password reset, the login form returns a 500 Internal Server Error instead of successfully authenticating the user. This affects all users who have recently reset their passwords.

## Steps to Reproduce
1. Navigate to https://portal.solar-networks.com/login
2. Click on "Forgot Password" link
3. Enter email address and submit
4. Check email and click the password reset link
5. Enter new password and confirm
6. Click "Update Password"
7. Redirected to login page
8. Enter email and new password
9. Click "Login"
10. Observe 500 error

## Expected Behavior
After successfully resetting the password, the user should be able to log in with their new credentials and access their dashboard.

## Actual Behavior
The login form displays a generic "Internal Server Error" message and the user cannot access their account. The browser network tab shows a 500 status code from the `/api/auth/login` endpoint.

## Environment Details
- **Browser**: Chrome 96.0.4664.110, Firefox 95.0.1
- **OS**: Windows 10, macOS Monterey
- **Device**: Desktop and mobile tested
- **Network**: Various (home, office, mobile)
- **Time**: Occurring since December 15, 2023, 2:00 PM EST

## Error Logs
```
[2023-12-15 19:02:34] ERROR: Authentication failed for user@example.com
[2023-12-15 19:02:34] ERROR: Database connection timeout in auth module
[2023-12-15 19:02:34] ERROR: Query failed: SELECT * FROM users WHERE email = ? AND password_hash = ?
```

## Screenshots
![Login Error Screenshot](error-screenshot.png)
*Screenshot showing the 500 error message on the login page*

## Additional Context
- This issue started occurring after the maintenance window on December 15
- Affects approximately 25% of users who reset passwords
- Users who haven't reset passwords can still log in normally
- Clearing browser cache/cookies doesn't resolve the issue
- Issue persists across different browsers and devices

## Workaround
Currently, affected users need to:
1. Contact customer support
2. Support team manually resets the user's password hash in the database
3. User can then log in successfully

## Impact Assessment
- **Users Affected**: ~150 users per day
- **Business Impact**: High - prevents customer access to billing and usage data
- **Support Load**: 20+ tickets per day
- **Revenue Impact**: Potential customer churn if not resolved quickly

## Related Issues
- Similar to issue #123 from last month (database timeout)
- May be related to recent database migration (PR #456)