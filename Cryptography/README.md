# Part 2 — Cryptographic Protocol Implementation & Security Analysis

## 1. Security Principle Mapping
- **RSA:** Addressing **Confidentiality**, **Authentication**, and **Non-repudiation**. RSA provides asymmetric encryption to protect data in transit (Confidentiality) and digital signature verification to confirm identity and prevent denial of action (Authentication & Non-repudiation).
- **Diffie-Hellman:** Addressing **Confidentiality**. Diffie-Hellman enables two untrusted parties to establish a shared symmetric key over an insecure channel without transmitting the key itself.

## 2. Key Exchange vs. Encryption
Diffie-Hellman is classified strictly as a **key exchange protocol** because it allows two parties to generate a matching symmetric key without sending secret data across the wire. Unlike RSA, DH has no mechanism to directly encrypt static arbitrary messages or generate persistent public-private keypairs for asymmetric message encryption/decryption.

## 3. Threat Model & Security Posture Write-Up
- **(a) Firewall Placement & Rule:** Place a Web Application Firewall (WAF) in front of CampusConnect's application server. Example traffic rule: Enforce `ALLOW TCP PORT 443 (HTTPS)` and `DROP/DENY TCP PORT 80 (HTTP)` except for HTTP-to-HTTPS redirects.
- **(b) Host vs. Network IDS:** Deploy a **Host-based IDS (HIDS)** (e.g., OSSEC) on application servers to detect local file modifications/privilege escalation, and a **Network IDS (NIDS)** (e.g., Suricata) at edge routers to detect external port scans and SQL injection payloads in packet streams.
- **(c) HTTPS Adoption & Vulnerability Prevention:** CampusConnect MUST use HTTPS. HTTPS protects against **Credential Sniffing** and **Session Hijacking** by encrypting traffic in transit using TLS.
- **(d) Least Privilege & MFA Design:**
  - *Factors:* Knowledge factor (Password) + Possession factor (Time-based OTP / Authenticator App).
  - *Roles:* Students have `READ` access to courses and `WRITE` access only to their own submissions; Instructors have `WRITE` access to course content and grading; Admins have full system configuration privileges.
- **(e) Plausible Attack Scenario:** **Active Man-In-The-Middle (MITM) Attack**. An attacker intercepts unencrypted HTTP traffic between a student and CampusConnect, injects malicious JavaScript, and steals active session tokens. Classified as **Active** because the attacker actively intercepts and alters communications in transit.
