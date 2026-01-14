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
