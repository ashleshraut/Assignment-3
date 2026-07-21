# CampusConnect Notifications Service Architecture Document

## 1. High-Level Design (HLD)

### System Components
1. **Presentation Layer:** Client apps (Web/Mobile) receiving real-time push and rendering inbox notifications.
2. **Business Layer (Notification Processing Engine):** Coordinates trigger events, parses template variables, and validates recipient preferences.
3. **Data-Access Layer:** Interfaces with the storage engine to read/write notification states and delivery logs.
4. **Database Layer:** Persists persistent storage for user preferences, templates, and delivery logs.

### Event Flow Strategy
1. Event Trigger (e.g., `AssignmentPostedEvent`) occurs in Core Service.
2. Core Service publishes event to Notification Queue.
3. Notification Engine consumes event, checks recipient preferences via Data Access Layer.
4. Engine dispatches notification across configured channels (Email, Push, SMS).

---

## 2. Architectural Style Choice

**Chosen Style:** Event-Driven Architecture (EDA)

### Advantages
1. **Asynchronous Decoupling:** Core actions (e.g., grading) complete instantly without waiting for notification delivery.
2. **High Scalability:** Notification processing workers can scale independently under heavy load.
3. **Fault Tolerance:** If downstream email services fail, events remain queued and retried without crashing primary workflows.

### Challenges
1. **Eventual Consistency:** Users may experience minor delays between action occurrence and notification arrival.
2. **Debugging Complexity:** Distributed tracing across event brokers requires specialized telemetry tools (OpenTelemetry).

---

## 3. Low-Level Design (LLD)

### Class Definitions

#### `Notification` Class
- **Attributes:**
  - `notification_id: str`
  - `recipient_id: str`
  - `message_body: str`
  - `channel_type: str`
  - `status: str`
- **Methods:**
  - `create_payload() -> dict`
  - `mark_as_sent() -> bool`

#### `NotificationDispatcher` Class
- **Attributes:**
  - `channel_providers: dict`
- **Methods:**
  - `register_channel(channel_type: str, provider: INotificationChannel) -> None`
  - `dispatch(notification: Notification) -> bool`

### SOLID Interface Definition

```python
from abc import ABC, abstractmethod

class INotificationChannel(ABC):
    @abstractmethod
    def send(self, recipient_id: str, message: str) -> bool:
        pass
