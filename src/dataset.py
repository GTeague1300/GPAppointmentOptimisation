
from src.models import Patient, Staff


def create_sample_dataset():
    """Create a small synthetic GP practice dataset."""

    patients = [
        Patient(
            patient_id="P1",
            duration=20,
            urgency="Routine",
            latest_start=720,
            preferred_period="late_morning",
            eligible_doctors=["D1", "D2"]
        ),
        Patient(
            patient_id="P2",
            duration=10,
            urgency="Urgent",
            latest_start=570,
            preferred_period="early_morning",
            eligible_doctors=["D2", "D3"]
        ),
        Patient(
            patient_id="P3",
            duration=20,
            urgency="Long-term",
            latest_start=1020,
            preferred_period="any",
            eligible_doctors=["D3"],
            requires_nurse=True
        ),
        Patient(
            patient_id="P4",
            duration=10,
            urgency="Routine",
            latest_start=1020,
            preferred_period="afternoon",
            eligible_doctors=["D3"]
        ),
        Patient(
            patient_id="P5",
            duration=10,
            urgency="Urgent",
            latest_start=600,
            preferred_period="morning",
            eligible_doctors=["D2"],
            requires_nurse=True
        )
    ]

    staff = [
        Staff("D1", "doctor", 480, 750),
        Staff("D2", "doctor", 480, 750),
        Staff("D3", "doctor", 480, 1080),
        Staff("N1", "nurse", 480, 1080)
    ]

    return patients, staff
