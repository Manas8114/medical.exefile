# medical.exefile

Medical application executable — Windows desktop app for clinic/hospital management.

## Features

- Patient registration and records (EMR-lite)
- Appointment scheduling with calendar view
- Prescription management (drug database, interactions)
- Billing and invoicing
- Lab test ordering and results
- User roles: Admin, Doctor, Nurse, Receptionist

## Tech Stack

- Language: C# (.NET Framework / .NET 6+) or C++ (Qt) or Java (packaged as exe)
- Database: SQLite (local) or SQL Server (network)
- UI: WPF / WinForms / Qt / JavaFX

## Run

```bash
# If .NET
./medical.exe

# If Java
java -jar medical.jar

# If native
./medical
```

## Database Schema (Expected)

```
patients (id, name, dob, gender, contact, address, history)
appointments (id, patient_id, doctor_id, datetime, status)
prescriptions (id, patient_id, doctor_id, drugs, dosage, notes)
billing (id, patient_id, items, total, paid, date)
users (id, username, role, password_hash)
```

## Notes

- Repo name suggests single-file executable distribution
- Academic/early-stage project (2024)
- Check releases for compiled binary
- Source may be in separate repo