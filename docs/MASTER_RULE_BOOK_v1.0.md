# MASTER RULE BOOK – VERSION 1.0

## DeFiTuna LP Dashboard
### Evidence-Based Market Forecasting & Decision Intelligence System

---

## 1. PURPOSE OF THE SYSTEM

The DeFiTuna LP Dashboard is a thinking and forecasting support system, not a trading or execution system.

Its purpose is to:
- Observe the market objectively
- Measure current and historical market behavior
- Classify the current market environment
- Forecast probable future market behavior based strictly on evidence
- Explain findings in clear human language
- Guide how a liquidity provider should behave

The system does NOT:
- Execute trades
- Place or manage liquidity
- Optimize profit automatically
- Make guarantees

All outputs are advisory, explainable, and evidence-bound.

---

## 2. CORE PHILOSOPHY – EVIDENCE SUPREMACY

### MASTER LAW

The system must not make assumptions, guesses, or intuitive claims at any point.

Every conclusion, forecast, recommendation, or warning must be backed by:
1. Current observable market data, and/or
2. Historical facts observed under comparable market states.

If evidence is insufficient, conflicting, or unstable, the system must:
- Lower confidence
- Default to neutrality
- Explicitly state uncertainty

Confidence is earned through evidence and consistency, never assumed.

---

## 3. ARCHITECTURE & MODULE BOUNDARIES

### 3.1 Layered Architecture Principle

The system must be built as a strictly layered architecture.

Each layer:
- Depends only on the layer directly below it
- Must function correctly even if all higher layers are removed
- Must not access sideways or upward layers

The fixed dependency order is:

Price Module  
↓  
Technical Analysis (TA) Module  
↓  
Fundamental Analysis (FA) Module  
↓  
Market State Classification Module  
↓  
Forecast & Risk Interpretation Module  
↓  
Advisory Guidance Module  
↓  
Dashboard (Display Only)

Violation of this order is a critical system error.

---

### 3.2 Module Responsibility Rules

Each module must have exactly one responsibility.

#### Price Module
- Fetches current and historical prices
- Handles multiple data sources and fallback logic
- Caches and stores price data
- Is the only module allowed to interact with third-party price APIs

Forbidden:
- Indicators
- Analysis
- Interpretation
- Strategy logic

---

#### Technical Analysis (TA) Module
- Computes technical indicators from price data
- Measures trend, momentum, volatility, and structure
- Produces numerical measurements and descriptive labels

Forbidden:
- Trade signals
- Strategy recommendations
- Forecasts
- API calls

---

#### Fundamental Analysis (FA) Module
- Collects and categorizes news and macro information
- Scores contextual market pressure based on historical impact
- Accounts for news decay over time

Forbidden:
- Price prediction
- Direction enforcement
- Overriding TA results

---

#### Market State Classification Module
- Combines TA and FA outputs
- Classifies the current market environment
- Produces human-readable market state descriptions

Forbidden:
- Execution logic
- Liquidity math
- Capital allocation

---

#### Forecast & Risk Interpretation Module
- Uses current state and historical analogs
- Estimates probabilistic future behavior
- Assesses volatility expansion, range survival, and tail risk

Forbidden:
- Price targets
- Guarantees
- Absolute statements

---

#### Advisory Guidance Module
- Translates forecasts into behavioral guidance
- Suggests conservative, neutral, or aggressive posture
- Does not execute or automate actions

---

#### Dashboard Module
- Displays results only
- Explains evidence, confidence, and reasoning
- Contains no logic or calculations

---

### 3.3 Stability Rule

Before moving to the next layer:
- The current layer must be complete
- Fully testable in isolation
- Committed and frozen in Git

If a higher layer is deleted, all lower layers must still work perfectly.

This rule is non-negotiable.

---

## 4. PRICE MODULE – FOUNDATION LAYER

### 4.1 Purpose

The Price Module is the foundation of the entire system.

It exists to provide accurate, reliable, and consistent price data to all other modules.

---

### 4.2 Responsibilities

The Price Module is responsible for:
- Fetching current market prices
- Fetching historical price data
- Supporting multiple price data sources
- Automatically falling back if a data source fails
- Caching price data to prevent API overuse
- Providing a single, clean interface for price access

---

### 4.3 Access Control (Critical Rule)

The Price Module is the only module allowed to:
- Make external API calls for price data
- Communicate with third-party price providers

All other modules must consume price data exclusively through the Price Module.

---

### 4.4 Forbidden Actions

The Price Module must never:
- Compute indicators
- Perform technical analysis
- Interpret price movement
- Make forecasts or recommendations
- Contain strategy logic

---

## 5. TECHNICAL ANALYSIS (TA) MODULE

### 5.1 Purpose

The Technical Analysis module exists to measure observable price behavior.

It translates raw price data into objective, explainable measurements.

---

### 5.2 Allowed Indicators (v1.0 – Frozen)

Only the following indicators are permitted in version 1.0:

- Moving Average (MA) 20
- Moving Average (MA) 200
- Relative Strength Index (RSI)
- Volatility measure (ATR or Standard Deviation)
- Range / Chop efficiency metric

---

### 5.3 TA Outputs

The TA module may output:
- Short-term bias (measured)
- Long-term bias (measured)
- Volatility level
- Trend strength
- Indicator agreement or conflict score

The TA module provides measurements only, never conclusions.

---

## 6. FUNDAMENTAL ANALYSIS (FA) MODULE

### 6.1 Purpose

The Fundamental Analysis module provides contextual, non-price-based information that may influence market behavior.

---

### 6.2 FA Data Scope (v1.0 – Frozen)

The FA module may consider only the following categories:

- Geopolitical news and global macro events
- Bitcoin-related news and systemic crypto market developments
- General cryptocurrency market news
- Solana ecosystem–specific news and announcements
- Major protocol upgrades, outages, or regulatory actions

---

### 6.3 Evidence-Based News Handling Rules

- All news items must be timestamped
- News must be categorized by type and relevance
- News impact must be assessed using historical precedents
- News impact must decay over time

---

### 6.4 FA Outputs

The FA module may output:
- Fundamental bias score (contextual, not directional)
- Event risk level
- Macro or ecosystem pressure indicators

FA outputs provide context only.

---

## 7. MARKET STATE CLASSIFICATION MODULE

### 7.1 Purpose

The Market State Classification module exists to answer one question:

**What type of market environment exists right now?**

It converts TA and FA measurements into structured, human-readable market states.

---

### 7.2 Market State Definition Rules

Market states must be:
- Mutually exclusive
- Evidence-based
- Explainable in plain language
- Stable enough to be backtested historically

Market states must never be vague or overlapping.

---

### 7.3 Core Market State Dimensions

Each market state is defined using four dimensions:

1. **Direction**
   - Bullish
   - Bearish
   - Neutral

2. **Volatility Regime**
   - Low
   - Normal
   - High
   - Expanding / Contracting

3. **Structure**
   - Trending
   - Range-bound
   - Choppy / Transitional

4. **Contextual Risk**
   - Low
   - Elevated
   - High (event-driven)

---

### 7.4 Market State Outputs

The Market State module may output:
- A primary market state label
- A secondary risk modifier
- A confidence score based on indicator agreement

---

### 7.5 Forbidden Actions

The Market State Classification module must never:
- Suggest strategies
- Compute liquidity ranges
- Allocate capital
- Make forecasts or predictions

It classifies the present environment only.
