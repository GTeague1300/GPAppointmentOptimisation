
from src.models import Patient, Staff, Appointment


def validate_appointment(
    appointment: Appointment,
    patient: Patient,
    staff: list[Staff],
    appointments: list[Appointment]
) -> list[str]:
    """Return any constraint violations for an appointment."""

    violations = []

    # 1. Check that the assigned doctor exists and is eligible.
    doctor = next(
        (member for member in staff
         if member.staff_id == appointment.doctor_id
         and member.role == "doctor"),
        None
    )

    if doctor is None:
        violations.append("Assigned doctor does not exist.")

    elif appointment.doctor_id not in patient.eligible_doctors:
        violations.append("Doctor is not eligible for this patient.")

    # 2. Check appointment duration.
    if appointment.duration != patient.duration:
        violations.append("Appointment duration does not match patient requirement.")

    # 3. Check that the appointment falls within doctor availability.
    if doctor is not None:
        if (appointment.start_time < doctor.available_from
                or appointment.end_time > doctor.available_until):
            violations.append("Appointment falls outside doctor availability.")

    # 4. Check for overlapping appointments with the same doctor.
    for existing in appointments:
        if existing.patient_id == appointment.patient_id:
            violations.append("Patient already has an appointment.")
            break

        if existing.doctor_id == appointment.doctor_id:
            if (appointment.start_time < existing.end_time
                    and existing.start_time < appointment.end_time):
                violations.append("Doctor has an overlapping appointment.")
                break

    # 5. Check nurse requirements.
    if patient.requires_nurse:
        if appointment.nurse_id is None:
            violations.append("Patient requires a nurse.")

        else:
            nurse = next(
                (member for member in staff
                 if member.staff_id == appointment.nurse_id
                 and member.role == "nurse"),
                None
            )

            if nurse is None:
                violations.append("Assigned nurse does not exist.")

            else:
                if (appointment.start_time < nurse.available_from
                        or appointment.end_time > nurse.available_until):
                    violations.append("Appointment falls outside nurse availability.")

                for existing in appointments:
                    if existing.nurse_id == appointment.nurse_id:
                        if (appointment.start_time < existing.end_time
                                and existing.start_time < appointment.end_time):
                            violations.append("Nurse has an overlapping appointment.")
                            break

    elif appointment.nurse_id is not None:
        violations.append("Patient does not require a nurse.")

    # 6. Check time-slot alignment (10-minute intervals).
    if appointment.start_time % 10 != 0:
        violations.append("Appointment does not start on a 10-minute boundary.")

    return violations
