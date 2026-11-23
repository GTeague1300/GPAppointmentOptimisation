
from dataclasses import dataclass
from typing import Optional


@dataclass
class Patient:
    patient_id: str
    duration: int
    urgency: str
    latest_start: int
    preferred_period: str
    eligible_doctors: list[str]
    requires_nurse: bool = False


@dataclass
class Staff:
    staff_id: str
    role: str
    available_from: int
    available_until: int


@dataclass
class Appointment:
    patient_id: str
    doctor_id: str
    start_time: int
    duration: int
    nurse_id: Optional[str] = None

    @property
    def end_time(self) -> int:
        return self.start_time + self.duration
