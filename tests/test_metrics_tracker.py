"""
tests/test_metrics_tracker.py — Tests unitaires Livrable #8
"""
import pytest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from metrics.tracker import (
    track, get_runs, get_kpis, clear_metrics,
    OP_ANALYSIS, OP_SELECTOR, OP_SCENARIO, OP_MOCK_SYNC,
    STATUS_SUCCESS, STATUS_ERROR,
)


@pytest.fixture(autouse=True)
def clean_db():
    """RAZ avant chaque test."""
    clear_metrics()
    yield
    clear_metrics()


class TestTrack:
    def test_track_basic(self):
        track(OP_ANALYSIS, 100, STATUS_SUCCESS)
        runs = get_runs(limit=10)
        assert len(runs) == 1
        assert runs[0]["operation"] == OP_ANALYSIS
        assert runs[0]["duration_ms"] == 100
        assert runs[0]["status"] == STATUS_SUCCESS

    def test_track_with_details(self):
        track(OP_SELECTOR, 200, STATUS_SUCCESS, broken=3, fixed=2)
        runs = get_runs(limit=1)
        assert runs[0]["details"]["broken"] == 3
        assert runs[0]["details"]["fixed"] == 2

    def test_track_error_status(self):
        track(OP_SCENARIO, 50, STATUS_ERROR)
        runs = get_runs(limit=1)
        assert runs[0]["status"] == STATUS_ERROR

    def test_track_all_operations(self):
        for op in [OP_ANALYSIS, OP_SELECTOR, OP_SCENARIO, OP_MOCK_SYNC]:
            track(op, 100, STATUS_SUCCESS)
        assert get_kpis()["total_runs"] == 4


class TestGetRuns:
    def test_get_runs_order(self):
        track(OP_ANALYSIS, 10, STATUS_SUCCESS)
        track(OP_SELECTOR, 20, STATUS_SUCCESS)
        runs = get_runs(limit=10)
        # Les plus récents en premier
        assert runs[0]["operation"] == OP_SELECTOR
        assert runs[1]["operation"] == OP_ANALYSIS

    def test_get_runs_filter_by_op(self):
        track(OP_ANALYSIS, 10, STATUS_SUCCESS)
        track(OP_SELECTOR, 20, STATUS_SUCCESS)
        track(OP_ANALYSIS, 30, STATUS_SUCCESS)
        runs = get_runs(operation=OP_ANALYSIS, limit=10)
        assert len(runs) == 2
        assert all(r["operation"] == OP_ANALYSIS for r in runs)

    def test_get_runs_limit(self):
        for _ in range(10):
            track(OP_MOCK_SYNC, 5, STATUS_SUCCESS)
        runs = get_runs(limit=3)
        assert len(runs) == 3

    def test_get_runs_empty(self):
        assert get_runs() == []


class TestGetKpis:
    def test_kpis_empty(self):
        kpis = get_kpis()
        assert kpis["total_runs"] == 0
        assert kpis["success_rate_pct"] == 0.0

    def test_kpis_100_percent_success(self):
        track(OP_ANALYSIS, 100, STATUS_SUCCESS)
        track(OP_ANALYSIS, 200, STATUS_SUCCESS)
        kpis = get_kpis()
        assert kpis["total_runs"] == 2
        assert kpis["success_rate_pct"] == 100.0
        assert kpis["avg_duration_ms"] == 150

    def test_kpis_mixed_status(self):
        track(OP_ANALYSIS, 100, STATUS_SUCCESS)
        track(OP_ANALYSIS, 100, STATUS_ERROR)
        kpis = get_kpis()
        assert kpis["success_rate_pct"] == 50.0

    def test_kpis_by_operation(self):
        track(OP_ANALYSIS, 100, STATUS_SUCCESS)
        track(OP_SELECTOR, 200, STATUS_SUCCESS)
        track(OP_SCENARIO, 300, STATUS_ERROR)
        kpis = get_kpis()
        by_op = kpis["by_operation"]
        assert OP_ANALYSIS in by_op
        assert OP_SELECTOR in by_op
        assert OP_SCENARIO in by_op
        assert by_op[OP_SCENARIO]["success_rate_pct"] == 0.0

    def test_kpis_avg_duration(self):
        track(OP_ANALYSIS, 100, STATUS_SUCCESS)
        track(OP_ANALYSIS, 300, STATUS_SUCCESS)
        kpis = get_kpis()
        assert kpis["avg_duration_ms"] == 200


class TestClearMetrics:
    def test_clear_all(self):
        track(OP_ANALYSIS, 100, STATUS_SUCCESS)
        track(OP_SELECTOR, 100, STATUS_SUCCESS)
        deleted = clear_metrics()
        assert deleted == 2
        assert get_kpis()["total_runs"] == 0

    def test_clear_by_operation(self):
        track(OP_ANALYSIS, 100, STATUS_SUCCESS)
        track(OP_SELECTOR, 100, STATUS_SUCCESS)
        deleted = clear_metrics(operation=OP_ANALYSIS)
        assert deleted == 1
        remaining = get_runs(limit=10)
        assert len(remaining) == 1
        assert remaining[0]["operation"] == OP_SELECTOR

    def test_clear_empty_returns_zero(self):
        assert clear_metrics() == 0
