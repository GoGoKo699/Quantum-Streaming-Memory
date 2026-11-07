#!/usr/bin/env python3
"""Run the three scientific checks and bind their results to source hashes."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys

import numpy


HERE = Path(__file__).resolve().parent
CASES = [
    ("verify_qss_primitive.py", "qss_primitive_verification.json"),
    ("verify_streaming_schedule.py", "streaming_schedule_verification.json"),
    ("verify_no_feedback_pipeline.py", "no_feedback_pipeline_verification.json"),
]


def main():
    if not __debug__:
        raise SystemExit("Run without -O: the scientific checks use assertions.")
    for program, _ in CASES:
        result = subprocess.run(
            [sys.executable, "-E", str(HERE / program)],
            cwd=HERE, text=True, capture_output=True,
        )
        if result.returncode:
            sys.stderr.write(result.stdout + result.stderr)
            raise SystemExit(result.returncode)
        print(f"PASS: {program}")

    primitive, feedback, pipeline = [
        json.loads((HERE / output).read_text()) for _, output in CASES
    ]
    # Assert the intended test families, not just successful program exit.
    assert len(primitive["checks"]) == 3
    assert all(row["choi_output_and_syndrome_fidelity"] == 1.0
               and row["max_amplitude_error"] == 0.0
               for row in primitive["checks"])
    assert feedback["status"] == pipeline["status"] == "PASS"
    assert feedback["total_cases"] == 33707
    assert pipeline["total_cases"] == 38217
    sources = [name for name, _ in CASES] + ["run_all.py", "requirements.txt"]
    report = {
        "status": "PASS",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "python": platform.python_version(),
        "numpy": numpy.__version__,
        "source_sha256": {
            name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
            for name in sources
        },
        "qss": primitive,
        "feedback_schedule": {
            key: value for key, value in feedback.items()
            if key != "phase_rotation_sample"
        },
        "no_feedback_pipeline": {
            key: value for key, value in pipeline.items()
            if key != "short_horizon_example"
        },
        "scope": "Finite coherent-algebra and symbolic schedule checks; universal claims use the written proofs.",
    }
    (HERE / "verification_report.json").write_text(json.dumps(report, indent=2) + "\n")
    print("PASS: 3 exact decoder identities; 33,707 feedback schedules; 38,217 no-feedback pipelines.")
    print("Wrote verification/verification_report.json with exact program hashes.")


if __name__ == "__main__":
    main()
