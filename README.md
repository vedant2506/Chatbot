[README.md](https://github.com/user-attachments/files/32870525/README.md)
# Chatbot# KKWIEER Lost & Found Telegram Bot

A Telegram-based Lost and Found system for the KKWIEER college
community. Students can report lost or found items and manage their own
reports. Admins have additional tools to review all listings, identify
potential matches, manage listings, send announcements, and view system
statistics.

## Features

### Normal User

-   Register and access the bot through Telegram.
-   Submit a **Lost Item** report.
-   Submit a **Found Item** report.
-   Search for relevant items according to the bot's access rules.
-   View and manage their own reports.
-   Receive bot notifications.
-   Get usage instructions through the Help option.

### Admin

-   Access a separate Admin Panel.
-   View registered users.
-   View all Lost Item reports.
-   View all Found Item reports.
-   Review potential Lost--Found matches.
-   Remove or take down listings when necessary.
-   Send announcements to users.
-   View system statistics.

### Privacy and Access Control

-   Normal users cannot browse the complete Lost and Found database.
-   Users can access and manage their own reports.
-   Admin-only actions are protected by checking the Telegram user's ID.
-   Private contact details should not be exposed in public listing
    information.

## Technology Stack

  Component                   Technology
  --------------------------- --------------------------------
  Bot platform                Telegram Bot API
  Programming language        Python 3
  Telegram library            `pyTelegramBotAPI` (`telebot`)
  Database                    SQLite
  Environment configuration   `python-dotenv`

The bot is designed to run locally and does not require a paid AI API or
an automation platform.

## Requirements

-   Python 3 installed
-   A Telegram account
-   A Telegram bot token created through
    [BotFather](https://t.me/BotFather)

## Setup and Installation

### 1. Get the project

Download or clone the project repository, then open its folder in a
terminal or in Cursor.

### 2. Create a virtual environment (recommended)

**Windows:**

``` bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

If the project contains `requirements.txt`, run:

``` bash
pip install -r requirements.txt
```

If dependencies are not listed there, make sure the project requirements
include `pyTelegramBotAPI` and `python-dotenv`.

### 4. Configure environment variables

Create a `.env` file in the project root. Add your own values:

``` env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
ADMIN_IDS=YOUR_TELEGRAM_USER_ID
```

For multiple admins, use comma-separated Telegram user IDs:

``` env
ADMIN_IDS=123456789,987654321
```

Replace the example values with your actual token and admin ID(s).
**Never publish or share your bot token.** Keep `.env` out of version
control.

### 5. Run the bot

If the entry-point file is `bot.py`, run:

``` bash
python bot.py
```

Keep the terminal/process running while using the bot. If your project's
entry-point file has a different name, use that file instead.

### 6. Open the bot in Telegram

Open your bot's Telegram chat and send:

``` text
/start
```

Follow the menu to register and use the available features.

## How to Use

### Reporting a Lost Item

1.  Choose **I Lost Something**.
2.  Enter the requested item details, such as category, item name,
    description, location, and date.
3.  Review the information.
4.  Submit the report.

### Reporting a Found Item

1.  Choose **I Found Something**.
2.  Enter the requested details.
3.  Review the information.
4.  Submit the report.

### Managing Your Reports

Open **My Reports** to view and manage reports submitted by your own
Telegram account. Available actions depend on the options shown by the
bot.

### Admin Workflow

1.  Open **Admin Panel** using an authorized admin account.
2.  View users, all Lost reports, or all Found reports.
3.  Review potential matches between Lost and Found reports.
4.  Confirm or reject a suggested match, where supported.
5.  Remove a listing if required.
6.  Use announcements and statistics as needed.

## Potential Matching

The admin matching feature compares Lost and Found reports using details
such as:

-   Category
-   Item name
-   Description
-   Location
-   Date

It uses local text-similarity/rule-based comparison rather than an
external AI service. A match score indicates **similarity**, not the
probability that two reports refer to the same item.

Potential matches are intended to assist the admin. The admin makes the
final decision. Confirming a potential match does not, by itself, mean
the item has been returned or recovered.

## Database

The project uses SQLite to store application data, such as user
registrations and item reports. The database file is created or
initialized by the application according to its implementation.

Keep a backup of the database if you need to preserve reports. Do not
delete the database file unless you intentionally want to reset the
stored data.

## Testing Checklist

Before demonstrating the project, test the following:

-   [ ] `/start` works for new and returning users.
-   [ ] A normal user can submit a Lost report.
-   [ ] A normal user can submit a Found report.
-   [ ] Users can view their own reports.
-   [ ] Search follows the intended access and privacy rules.
-   [ ] Normal users cannot access the Admin Panel.
-   [ ] Admins can view all Lost and Found reports.
-   [ ] Admins can remove a listing.
-   [ ] Potential Matches are visible to admins only.
-   [ ] Admin can confirm or reject a potential match, if enabled.
-   [ ] Announcements and statistics work.
-   [ ] Invalid input or Telegram errors do not crash the bot.

## Security Notes

-   Do not commit `.env` or share your bot token.
-   Keep admin Telegram IDs configured correctly.
-   Ensure `.env`, database files, and local virtual-environment files
    are excluded through `.gitignore`.
-   Do not expose users' private contact information in listing results.
-   Back up the SQLite database before making significant changes.

## Project Status

This project is intended as a college Lost and Found solution. Feature
availability may depend on the current version of the code. Check the
bot's menus and project configuration for the exact options enabled in
your installation.
