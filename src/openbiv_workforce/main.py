#!/usr/bin/env python
import sys
import warnings

from openbiv_workforce.crew import OpenbivWorkforce

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """Run the crew."""
    inputs = {
        "ten_du_an": "Tăng trưởng khách hàng cho Spa",
        "linh_vuc": "Spa/Thẩm mỹ",
        "muc_tieu_kinh_doanh": "Tăng lịch hẹn mới + tăng doanh thu dịch vụ chính",
        "ngan_sach_du_kien": "15.000.000 VND/tháng",
        "deadline": "30 ngày",
        "ghi_chu_them": "Kênh chính Facebook, khách ưu tiên lead chất lượng"
    }

    try:
        OpenbivWorkforce().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    inputs = {
        "ten_du_an": "Tăng trưởng khách hàng cho Spa",
        "linh_vuc": "Spa/Thẩm mỹ",
        "muc_tieu_kinh_doanh": "Tăng lịch hẹn mới + tăng doanh thu dịch vụ chính",
        "ngan_sach_du_kien": "15.000.000 VND/tháng",
        "deadline": "30 ngày",
        "ghi_chu_them": "Kênh chính Facebook, khách ưu tiên lead chất lượng"
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
        "ten_du_an": "Tăng trưởng khách hàng cho Spa",
        "linh_vuc": "Spa/Thẩm mỹ",
        "muc_tieu_kinh_doanh": "Tăng lịch hẹn mới + tăng doanh thu dịch vụ chính",
        "ngan_sach_du_kien": "15.000.000 VND/tháng",
        "deadline": "30 ngày",
        "ghi_chu_them": "Kênh chính Facebook, khách ưu tiên lead chất lượng"
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
        "ten_du_an": trigger_payload.get("ten_du_an", ""),
        "linh_vuc": trigger_payload.get("linh_vuc", ""),
        "muc_tieu_kinh_doanh": trigger_payload.get("muc_tieu_kinh_doanh", ""),
        "ngan_sach_du_kien": trigger_payload.get("ngan_sach_du_kien", ""),
        "deadline": trigger_payload.get("deadline", ""),
        "ghi_chu_them": trigger_payload.get("ghi_chu_them", "")
    }

    try:
        result = OpenbivWorkforce().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
