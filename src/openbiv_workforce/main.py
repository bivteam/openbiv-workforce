#!/usr/bin/env python
import sys
import warnings

from openbiv_workforce.crew import OpenbivWorkforce

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """Run the crew."""
    inputs = {
        "nganh_nghe": "Spa/Thẩm mỹ",
        "muc_tieu": "Tăng inbox và lịch hẹn",
        "ngan_sach_thang": "15.000.000 VND",
        "kenh_chinh": "Facebook"
    }

    try:
        OpenbivWorkforce().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    inputs = {
        "nganh_nghe": "Spa/Thẩm mỹ",
        "muc_tieu": "Tăng inbox và lịch hẹn",
        "ngan_sach_thang": "15.000.000 VND",
        "kenh_chinh": "Facebook"
    }
    try:
        OpenbivWorkforce().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    try:
        OpenbivWorkforce().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    inputs = {
        "nganh_nghe": "Spa/Thẩm mỹ",
        "muc_tieu": "Tăng inbox và lịch hẹn",
        "ngan_sach_thang": "15.000.000 VND",
        "kenh_chinh": "Facebook"
    }

    try:
        OpenbivWorkforce().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


def run_with_trigger():
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "nganh_nghe": trigger_payload.get("nganh_nghe", ""),
        "muc_tieu": trigger_payload.get("muc_tieu", ""),
        "ngan_sach_thang": trigger_payload.get("ngan_sach_thang", ""),
        "kenh_chinh": trigger_payload.get("kenh_chinh", "")
    }

    try:
        result = OpenbivWorkforce().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
