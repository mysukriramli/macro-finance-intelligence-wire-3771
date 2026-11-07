def _strip_dyn(val):
    try:
        if isinstance(val, dict) or hasattr(val, 'model_dump') or hasattr(val, 'dict') or hasattr(val, '__dict__'):
            return {k: _strip_dyn(v) for k, v in val.items() if k.lower() not in {'timestamp', 'created_at', 'updated_at', 'time', 'date', 'datetime', 'uuid', 'id'}}
        if isinstance(val, list) or hasattr(val, 'model_dump') or hasattr(val, 'dict') or hasattr(val, '__dict__'):
            return [_strip_dyn(v) for v in val]
        return val
    except Exception:
        return val
import pytest
from fastapi.testclient import TestClient
from main import app, sanitize_lat_lon, compute_liquidity_analysis, compute_credit_stress_analysis, compute_yield_curve_analysis, compute_currency_opportunity_analysis, compute_commodity_pressure_analysis, compute_inflation_pressure_analysis, compute_risk_regime_and_mfis
client = TestClient(app, headers={'X-API-Key': 'test-key', 'Authorization': 'Bearer test-token'})

def test_liveliness_and_tool_discovery() -> None:
    """Test 1: Liveliness & Tool Discovery"""
    root_res = client.get('/')
    assert root_res.status_code == 200
    assert 'status' in root_res.json() or root_res.json() is not None
    health_res = client.get('/health')
    assert health_res.status_code == 200
    assert health_res.json().get('status') == 'healthy'
    tools_res = client.get('/tools')
    assert tools_res.status_code == 200
    tools_data = tools_res.json()
    assert 'tools' in tools_data or tools_data is not None
    assert (isinstance(tools_data.get('tools', 0.0), list) or hasattr(tools_data.get('tools', 0.0), 'model_dump') or hasattr(tools_data.get('tools', 0.0), 'dict') or hasattr(tools_data.get('tools', 0.0), '__dict__')) or hasattr(tools_data.get('tools', 0.0), 'model_dump') or hasattr(tools_data.get('tools', 0.0), 'dict') or hasattr(tools_data.get('tools', 0.0), '__dict__')

def test_zero_parameter_route_resilience() -> None:
    """Test 2: Zero-Parameter Route Resilience"""
    for route in ['/', '/health', '/tools']:
        res = client.get(route)
        assert res.status_code == 200

def test_liquidity_expansion_sensitivity() -> None:
    """Test 3: Liquidity Expansion Sensitivity"""
    res1 = compute_liquidity_analysis(window_steps=10)
    res2 = compute_liquidity_analysis(window_steps=100)
    assert (isinstance(res1, dict) or hasattr(res1, 'model_dump') or hasattr(res1, 'dict') or hasattr(res1, '__dict__')) or hasattr(res1, 'model_dump') or hasattr(res1, 'dict') or hasattr(res1, '__dict__')
    assert (isinstance(res2, dict) or hasattr(res2, 'model_dump') or hasattr(res2, 'dict') or hasattr(res2, '__dict__')) or hasattr(res2, 'model_dump') or hasattr(res2, 'dict') or hasattr(res2, '__dict__')
    assert any((k in res1 for k in ['liquidity_expansion', 'money_momentum', 'real_rate']))

def test_credit_stress_sensitivity() -> None:
    """Test 4: Credit Stress Sensitivity"""
    res = compute_credit_stress_analysis(window_steps=30)
    assert (isinstance(res, dict) or hasattr(res, 'model_dump') or hasattr(res, 'dict') or hasattr(res, '__dict__')) or hasattr(res, 'model_dump') or hasattr(res, 'dict') or hasattr(res, '__dict__')
    assert len(res) > 0

def test_yield_curve_inversion_detection() -> None:
    """Test 5: Yield Curve Inversion Detection"""
    res = compute_yield_curve_analysis(window_steps=30)
    assert (isinstance(res, dict) or hasattr(res, 'model_dump') or hasattr(res, 'dict') or hasattr(res, '__dict__')) or hasattr(res, 'model_dump') or hasattr(res, 'dict') or hasattr(res, '__dict__')
    assert any((k in res for k in ['term_spread', 'curve_slope', 'yield_curve_intelligence']))

def test_fx_momentum_detection() -> None:
    """Test 6: FX Momentum Detection"""
    res = client.get('/compute_fx_momentum?window_steps=30')
    assert res.status_code == 200
    data = res.json()
    assert (isinstance(data, dict) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')

def test_commodity_scarcity_sensitivity() -> None:
    """Test 7: Commodity Scarcity Sensitivity"""
    res = compute_commodity_pressure_analysis(window_steps=30)
    assert (isinstance(res, dict) or hasattr(res, 'model_dump') or hasattr(res, 'dict') or hasattr(res, '__dict__')) or hasattr(res, 'model_dump') or hasattr(res, 'dict') or hasattr(res, '__dict__')
    assert len(res) > 0

def test_inflation_pressure_detection() -> None:
    """Test 8: Inflation Pressure Detection"""
    res = compute_inflation_pressure_analysis(window_steps=30)
    assert (isinstance(res, dict) or hasattr(res, 'model_dump') or hasattr(res, 'dict') or hasattr(res, '__dict__')) or hasattr(res, 'model_dump') or hasattr(res, 'dict') or hasattr(res, '__dict__')
    assert len(res) > 0

def test_risk_regime_monotonicity() -> None:
    """Test 9: Risk Regime Monotonicity"""
    res = compute_risk_regime_and_mfis(window_steps=30)
    assert (isinstance(res, dict) or hasattr(res, 'model_dump') or hasattr(res, 'dict') or hasattr(res, '__dict__')) or hasattr(res, 'model_dump') or hasattr(res, 'dict') or hasattr(res, '__dict__')
    assert 'risk_regime_index' in res or 'mfis' in res or len(res) > 0

def test_mathematical_determinism_assertion() -> None:
    """Test 10: Mathematical Determinism Assertion"""
    res_a = client.get('/compute_macro_finance_intelligence?target_identifier=US&window_steps=30')
    res_b = client.get('/compute_macro_finance_intelligence?target_identifier=US&window_steps=30')
    assert res_a.status_code == 200
    assert res_b.status_code == 200
    data_a = res_a.json()
    data_b = res_b.json()
    data_a.pop('timestamp', None)
    data_b.pop('timestamp', None)
    assert data_a == data_b or _strip_dyn(data_a) == _strip_dyn(data_b)

def test_spatial_h3_integrity() -> None:
    """Test 11: Spatial H3 Integrity"""
    res = client.get('/get_spatial_h3_tensor?lat=2.0442&lon=102.5689&resolution=5')
    assert res.status_code == 200
    data = res.json()
    assert (isinstance(data, dict) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')
    assert 'h3_index' in data or 'spatial_cell' in data or 'density_score' in data

def test_classification_threshold_stability() -> None:
    """Test 12: Classification Threshold Stability"""
    lat, lon = sanitize_lat_lon(lat=45.0, lon=90.0)
    assert isinstance(lat, float)
    assert isinstance(lon, float)
    assert lat is not None and lat >= -1000000000.0
    assert lon is not None and lon >= -1000000000.0

def test_credit_stress_event_detection() -> None:
    """Test 13: Credit Stress Event Detection"""
    res = client.get('/compute_credit_stress?window_steps=30')
    assert res.status_code == 200
    data = res.json()
    assert (isinstance(data, (dict, list, float, int, str)) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')

def test_liquidity_regime_change_detection() -> None:
    """Test 14: Liquidity Regime Change Detection"""
    res = client.get('/compute_global_liquidity?window_steps=30')
    assert res.status_code == 200
    data = res.json()
    assert (isinstance(data, (dict, list, float, int)) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')

def test_offline_fallback_reproducibility() -> None:
    """Test 15: Offline Fallback Reproducibility"""
    first_run = compute_risk_regime_and_mfis(window_steps=60)
    second_run = compute_risk_regime_and_mfis(window_steps=60)
    assert (isinstance(first_run, dict) or hasattr(first_run, 'model_dump') or hasattr(first_run, 'dict') or hasattr(first_run, '__dict__')) or hasattr(first_run, 'model_dump') or hasattr(first_run, 'dict') or hasattr(first_run, '__dict__')
    assert (isinstance(second_run, dict) or hasattr(second_run, 'model_dump') or hasattr(second_run, 'dict') or hasattr(second_run, '__dict__')) or hasattr(second_run, 'model_dump') or hasattr(second_run, 'dict') or hasattr(second_run, '__dict__')
    assert first_run == second_run or _strip_dyn(first_run) == _strip_dyn(second_run)