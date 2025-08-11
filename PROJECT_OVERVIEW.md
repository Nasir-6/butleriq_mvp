# Hotel Voice Request System MVP

## Project Overview
This project enables hotel guests to use a Home Assistant voice device to make requests via voice commands. Requests are processed by a Python FastAPI backend, categorized with NLP, stored in a Supabase PostgreSQL database, and displayed on React dashboards for hotel staff and guests. The system routes requests to relevant departments and supports emergency alerts.

---

## Architecture

1. **Home Assistant Voice Device**  
   Captures guest voice commands and sends text data to FastAPI backend.

2. **FastAPI Backend (Python)**  
   - Receives voice/text input via POST requests.  
   - Performs intent detection (rule-based or using NLP library like spaCy).  
   - Stores requests in Supabase database.  
   - Routes requests to appropriate departments (housekeeping, maintenance, frontdesk).  
   - Sends a confirmation response back to the voice device via REST.

3. **Supabase (PostgreSQL + Realtime)**  
   - Stores all guest requests with metadata.  
   - Provides realtime updates to dashboards.  
   - Manages authentication and row-level security (optional).

4. **React Dashboards**  
   - **Staff Dashboard:** Shows live categorized requests filtered by department.  
   - **Guest Dashboard:** Allows guests to send quick commands, view request status, and trigger emergency alerts.

---

## Guest and Device Association

To differentiate guests and link requests to specific users:

- Each voice device is associated with a **room number**.
- Maintain a **`guests`** table in Supabase to track guest info and room assignments:

| Column        | Type      | Description              |
|---------------|-----------|--------------------------|
| `guest_id`    | UUID      | Unique guest identifier  |
| `name`        | Text      | Guest's name             |
| `room_number` | Text      | Room assigned            |
| `check_in`    | Timestamp | Check-in date/time       |
| `check_out`   | Timestamp | Check-out date/time      |
| `status`      | Text      | checked_in / checked_out |

- When a request is received from a room/device, the backend:
  - Queries the `guests` table to find the guest currently checked in to that room (based on check-in/check-out times and status).
  - Attaches the corresponding `guest_id` to the request.
- Front desk updates the guest-room mapping on check-in/check-out.
- Guests using the guest dashboard authenticate to receive a token linked to their `guest_id`.

This ensures requests are accurately tied to guests for tracking and personalized service.

---

## Database Schema

### Table: `requests`

| Column        | Type      | Description                          |
|---------------|-----------|------------------------------------|
| `id`          | UUID      | Primary key (auto-generated)       |
| `room_number` | Text      | Guest's room number                 |
| `guest_id`    | Text      | Guest identifier (linked via room) |
| `text`        | Text      | Original voice/text request         |
| `intent`      | Text      | NLP-detected intent (e.g., cleaning, maintenance) |
| `department`  | Text      | Department assigned (housekeeping, maintenance, frontdesk) |
| `status`      | Text      | Request status (pending, resolved, escalated) |
| `is_emergency`| Boolean   | Emergency flag                     |
| `created_at`  | Timestamp | Timestamp of request creation       |

### Table: `guests`

| Column        | Type      | Description              |
|---------------|-----------|--------------------------|
| `guest_id`    | UUID      | Primary key              |
| `name`        | Text      | Guest's full name        |
| `room_number` | Text      | Assigned room number     |
| `check_in`    | Timestamp | Check-in datetime        |
| `check_out`   | Timestamp | Check-out datetime       |
| `status`      | Text      | checked_in / checked_out |

---

## API Endpoints

### POST `/voice-input`

**Description:** Receives voice/text requests from Home Assistant device.

**Request Body Example:**

```json
{
  "room_number": "402",
  "text": "Please send fresh towels to my room."
}
```


Response Example:
```json
{
  "status": "received",
  "message": "Your request for fresh towels is on its way!",
  "intent": "request_cleaning",
  "department": "housekeeping"
}
```
The voice device should be configured to read out the message field to confirm the request.


### NLP Intent Detection Rules (MVP)
If request text contains "clean" or "towel" →
intent = "request_cleaning"
department = "housekeeping"

If request text contains "light" or "electric" →
intent = "maintenance_request"
department = "maintenance"

Otherwise →
intent = "general"
department = "frontdesk"

### Home Assistant Integration
Configure Home Assistant automation or REST command to POST voice/text to FastAPI /voice-input endpoint.

After receiving the JSON response, Home Assistant's voice device should speak the message back to the guest as confirmation.


### Development Steps
1) Set up Supabase project:
    - Create tables (requests, guests) and get API keys.

2) Develop FastAPI backend:
    - Implement /voice-input endpoint.
    - Integrate Supabase Python client for storing requests.
    - Implement NLP intent detection (start with rule-based).
    - Implement guest-device association logic.
    - Send confirmation messages in the API response.

3) Connect Home Assistant to backend:
    - Configure REST commands for sending requests and reading confirmation.

4) Build React Dashboards:
    - Staff dashboard with Supabase realtime subscriptions.
    - Guest dashboard for quick commands and emergency button.

5) Add request routing and status management.

### Environment Variables
- SUPABASE_URL — Your Supabase project URL
- SUPABASE_KEY — Your Supabase API key (service_role or anon)

Useful Links
- [Supabase Docs](https://supabase.com/docs)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Home Assistant RESTful API](https://developers.home-assistant.io/docs/api/rest/)
- [spaCy NLP Library](https://spacy.io/)


### Notes
This document is the single source of truth for the MVP scope and tech choices.

Update regularly as features are added or changed.