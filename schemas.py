from datetime import timezone as dt_timezone
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field

class HealthResponse(BaseModel):
    """Health check response schema."""
    status: str = Field(default='healthy', description='Service health status')
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat(), description='UTC ISO timestamp')

class ToolItem(BaseModel):
    """Individual tool registration metadata."""
    name: str = Field(..., description='Tool name identifier')
    description: str = Field(..., description='Tool capability description')
    input_schema: Dict[str, Any] = Field(default_factory=dict, description='JSON Schema for inputs')

class ToolsResponse(BaseModel):
    """Container for registered MCP agent tools."""
    tools: List[Dict[str, Any]] = Field(default_factory=list, description='List of available tools')

class MacroFinanceIntelligenceRequest(BaseModel):
    """Input request model for primary macro finance analysis."""
    target_identifier: str = Field(default='global_macro', description='Target country or global scope identifier')
    query_parameter: str = Field(default='full_macro_analysis', description='Specific query focus or pipeline mode')
    lat: float = Field(default=0.0, ge=-90.0, le=90.0, description='Latitude coordinate')
    lon: float = Field(default=0.0, ge=-180.0, le=180.0, description='Longitude coordinate')
    window_steps: int = Field(default=30, ge=5, le=365, description='Lookback / simulation window steps')
    lookback_days: int = Field(default=365, ge=30, le=3650, description='Lookback horizon in days')

class ExplainabilityDetail(BaseModel.ConfigDict if hasattr(BaseModel, 'ConfigDict') else object):
    """Explainability weights and primary driver breakdown."""
    pass

class MacroFinanceIntelligenceResponse(BaseModel):
    """Output schema for macro finance intelligence wire analysis."""
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat(), description='Analysis UTC timestamp')
    status: str = Field(default='healthy', description='Execution status')
    primary_metric: float = Field(default=0.0, description='Primary macro finance index score (0-100)')
    secondary_score: float = Field(default=0.0, description='Secondary risk regime score')
    state_index: float = Field(default=0.0, description='Composite agent state index')
    classification: str = Field(default='NEUTRAL', description='Primary economic classification state')
    explainability: Dict[str, Any] = Field(default_factory=lambda: {'primary_driver': 'global_liquidity', 'weights': {'liquidity': 0.25, 'yield_curve': 0.2, 'fx': 0.2, 'commodity': 0.15, 'credit': 0.2}}, description='Scoring breakdown and weights')

class SpatialH3TensorRequest(BaseModel):
    """Input request for spatial H3 macro intelligence tensor."""
    lat: float = Field(default=2.0442, ge=-90.0, le=90.0, description='Latitude coordinate')
    lon: float = Field(default=102.5689, ge=-180.0, le=180.0, description='Longitude coordinate')
    resolution: int = Field(default=5, ge=0, le=15, description='H3 spatial resolution index')

class SpatialH3TensorResponse(BaseModel):
    """Output schema for spatial H3 macro intelligence tensor."""
    h3_index: str = Field(default='856520d3fffffff', description='H3 hexagonal index string')
    spatial_cell: str = Field(default='856520d3fffffff', description='Spatial cell identifier')
    density_score: float = Field(default=0.0, description='Monetary/Liquidity density score')
    terrain_state_index: float = Field(default=0.0, description='Regional pressure/terrain state index')
    status: str = Field(default='ACTIVE', description='Cell operational status')

class GlobalLiquidityRequest(BaseModel):
    country: str = Field(default='US', description='Target country code')
    lookback_days: int = Field(default=365, description='Lookback period in days')

class GlobalLiquidityResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    liquidity_expansion: float = Field(default=0.0)
    money_momentum: float = Field(default=0.0)
    gli_score: float = Field(default=0.0)
    classification: str = Field(default='NEUTRAL')

class CreditStressRequest(BaseModel.ConfigDict if hasattr(BaseModel, 'ConfigDict') else object):
    country: str = Field(default='US')
    window_steps: int = Field(default=30)

class CreditStressResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    credit_spread: float = Field(default=0.0)
    stress_velocity: float = Field(default=0.0)
    csi_score: float = Field(default=0.0)
    classification: str = Field(default='LOW')

class YieldCurveRequest(BaseModel):
    country: str = Field(default='US')

class YieldCurveResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    term_spread: float = Field(default=0.0)
    curve_slope: float = Field(default=0.0)
    yci_score: float = Field(default=0.0)
    classification: str = Field(default='NORMAL')

class CurrencyOpportunityRequest(BaseModel):
    base_currency: str = Field(default='USD')
    target_currency: str = Field(default='EUR')

class CurrencyOpportunityResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    fx_momentum: float = Field(default=0.0)
    volatility: float = Field(default=0.0)
    coi_score: float = Field(default=0.0)
    classification: str = Field(default='STABLE')

class InflationPressureRequest(BaseModel):
    country: str = Field(default='US')

class InflationPressureResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    acceleration: float = Field(default=0.0)
    persistence: float = Field(default=0.0)
    ipi_score: float = Field(default=0.0)
    classification: str = Field(default='MODERATE')

class CommodityPressureRequest(BaseModel):
    commodity_symbol: str = Field(default='BRENT')

class CommodityPressureResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    scarcity: float = Field(default=0.0)
    momentum: float = Field(default=0.0)
    cpi_score: float = Field(default=0.0)
    classification: str = Field(default='BALANCED')

class RiskRegimeRequest(BaseModel):
    scope: str = Field(default='GLOBAL')

class RiskRegimeResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    rri_score: float = Field(default=0.0)
    mfis_score: float = Field(default=0.0)
    decision_state: str = Field(default='NEUTRAL')
    classification: str = Field(default='NEUTRAL')

class GenericAnalysisRequest(BaseModel):
    """Generic payload container for tools requiring flexible parameters."""
    target_identifier: str = Field(default='global', description='Target identifier')
    query_parameter: str = Field(default='default', description='Query mode or parameter')
    lat: float = Field(default=0.0, ge=-90.0, le=90.0)
    lon: float = Field(default=0.0, ge=-180.0, le=180.0)
    window_steps: int = Field(default=30, ge=1, le=365)

class GenericAnalysisResponse(BaseModel):
    """Generic response container for analytical tools."""
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    status: str = Field(default='success')
    score: float = Field(default=50.0)
    metric_value: float = Field(default=0.0)
    classification: str = Field(default='NEUTRAL')
    details: Dict[str, Any] = Field(default_factory=dict)