
from src.models import Patient, Staff, Appointment
from src.constraints import validate_appointment


def test_valid_appointment():
    patient = Patient(
        "P1", 20, "Routine", 720, "morning", ["D1"]
    )

    staff = [
        Staff("D1", "doctor", 480, 750)
    ]

    appointment = Appointment("P1", "D1", 600, 20)

    assert validate_appointment(
        appointment, patient, staff, []
    ) == []


def test_doctor_overlap():
    patient = Patient(
        "P2", 10, "Urgent", 600, "morning", ["D1"]
    )

    staff = [
        Staff("D1", "doctor", 480, 750)
    ]

    existing = [
        Appointment("P1", "D1", 540, 20)
    ]

    appointment = Appointment("P2", "D1", 550, 10)

    violations = validate_appointment(
        appointment, patient, staff, existing
    )

    assert "Doctor has an overlapping appointment." in violations


def test_ineligible_doctor():
    patient = Patient(
        "P3", 10, "Routine", 600, "morning", ["D2"]
    )

    staff = [
        Staff("D1", "doctor", 480, 750)
    ]

    appointment = Appointment("P3", "D1", 540, 10)

    violations = validate_appointment(
        appointment, patient, staff, []
    )

    assert "Doctor is not eligible for this patient." in violations


def test_nurse_overlap():
    patient = Patient(
        "P2", 10, "Urgent", 600, "morning", ["D1"], True
    )

    staff = [
        Staff("D1", "doctor", 480, 750),
        Staff("D2", "doctor", 480, 750),
        Staff("N1", "nurse", 480, 750)
    ]

    existing = [
        Appointment("P1", "D2", 540, 20, "N1")
    ]

    appointment = Appointment("P2", "D1", 550, 10, "N1")

    violations = validate_appointment(
        appointment, patient, staff, existing
    )

    assert "Nurse has an overlapping appointment." in violations


def test_outside_doctor_availability():
    patient = Patient(
        "P3", 20, "Routine", 720, "afternoon", ["D1"]
    )

    staff = [
        Staff("D1", "doctor", 480, 750)
    ]

    appointment = Appointment("P3", "D1", 740, 20)

    violations = validate_appointment(
        appointment, patient, staff, []
    )

    assert "Appointment falls outside doctor availability." in violations


def test_duplicate_patient_appointment():
    patient = Patient(
        "P2", 10, "Routine", 600, "morning", ["D1"]
    )

    staff = [
        Staff("D1", "doctor", 480, 750)
    ]

    existing = [
        Appointment("P2", "D1", 540, 10)
    ]

    appointment = Appointment("P2", "D1", 570, 10)

    violations = validate_appointment(
        appointment, patient, staff, existing
    )

    assert "Patient already has an appointment." in violations
