
from src.dataset import create_sample_dataset


def test_sample_dataset():
    patients, staff = create_sample_dataset()

    assert len(patients) == 5
    assert len(staff) == 4

    assert len([s for s in staff if s.role == "doctor"]) == 3
    assert len([s for s in staff if s.role == "nurse"]) == 1

    assert patients[2].requires_nurse is True
    assert patients[4].requires_nurse is True

    assert all(patient.duration > 0 for patient in patients)
