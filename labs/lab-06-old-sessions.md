# Lab 06: Old Sessions

## Category

Web Exploitation

## Difficulty

Easy

## Challenge Description

This lab demonstrates an insecure session management vulnerability. The website allows sessions to stay active for a long time and exposes active session IDs through a public endpoint.

Because of this, a normal user can reuse another user's session ID and become that user without knowing their username or password.

## Objective

Find the flag by exploiting the old session vulnerability.

## Tools Used

* Web browser
* Chrome DevTools
* Cookies inspection
* Page source inspection

## Step 1: Launch the Lab

First, I launched the lab instance from CYLab Security Academy.

The website opened a login page for a simple social media application called **The New Twitter**.

## Step 2: Register a Normal User

I registered a normal user account.

Example:

```text
Username: piseth
Password: 123
```

After logging in, I was redirected to the homepage.

## Step 3: Inspect the Session Cookie

I opened Chrome DevTools and checked the website cookies.

```text
F12 → Application → Cookies → target website
```

I found a cookie named:

```text
session
```

The cookie had a long expiration date, which means the user session stays valid for a long time.

This is already suspicious because secure applications should not keep sensitive sessions active for too long.

## Step 4: Inspect the Page Source

Next, I opened the page source using:

```text
Ctrl + U
```

Inside the page source, I found a useful clue in the comments section:

```text
Hey I found a strange page at /sessions
```

This means there may be a hidden or sensitive endpoint called `/sessions`.

## Step 5: Visit the `/sessions` Endpoint

I opened the following path:

```text
/sessions
```

The page showed active session values.

Example:

```text
session: ADMIN_SESSION_VALUE, {'_permanent': True, 'key': 'admin'}
session: USER_SESSION_VALUE, {'_permanent': True, 'key': 'piseth'}
```

This is a serious security issue because valid session IDs should never be exposed to users.

## Step 6: Copy the Admin Session

From the `/sessions` page, I copied only the admin session value.

Important: I copied only the value after `session:` and did not copy the extra text.

Example:

```text
ADMIN_SESSION_VALUE
```

## Step 7: Replace My Session Cookie

I went back to Chrome DevTools:

```text
Application → Cookies → session → Value
```

Then I replaced my current `session` cookie value with the admin session value.

After changing the cookie, I refreshed the homepage.

## Step 8: Access the Website as Admin

After refreshing the page, the website authenticated me as:

```text
admin
```

The flag appeared on the homepage.

## Flag

```text
picoCTF{s3t_s3ss10n_3xp1rat10n5_2766ccb8}
```

## Vulnerability Explanation

The application is vulnerable to session hijacking.

The `/sessions` endpoint exposes active session IDs. Since session IDs are used to identify logged-in users, leaking them is the same as leaking login access.

When I replaced my own session cookie with the admin session value, the server trusted the cookie and logged me in as admin.

## Impact

An attacker could use this vulnerability to:

* Steal another user's session
* Access private user data
* Impersonate an admin
* Bypass login completely
* Perform actions as another user

## Recommended Fixes

To fix this vulnerability, the application should:

* Remove public access to `/sessions`
* Never expose session IDs to users
* Use short session expiration times
* Invalidate sessions after logout
* Regenerate session IDs after login
* Store sessions securely on the server
* Add proper authorization checks to sensitive endpoints
* Use secure cookie settings such as `HttpOnly`, `Secure`, and `SameSite`

## Lesson Learned

Session IDs are as sensitive as passwords. If a session ID is leaked, an attacker can use it to impersonate the user without knowing the username or password.

Secure session management is important in every web application.
