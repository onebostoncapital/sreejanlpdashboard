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

---

## 4. PRICE MODULE – FOUNDATION LAYER

The Price Module provides accurate, reliable, and consistent price data and is the only layer allowed to interact with third-party price APIs.

It provides **facts only**, never interpretation.

---

## 5. TECHNICAL ANALYSIS (TA) MODULE

The TA module measures observable price behavior using a frozen indicator set (MA-20, MA-200, RSI, volatility, range efficiency).

It produces **measurements only**, never signals or forecasts.

---

## 6. FUNDAMENTAL ANALYSIS (FA) MODULE

The FA module provides contextual, non-price-based evidence derived from macro, crypto, Bitcoin, and Solana-specific news.

It provides **context only**, never predictions.

---

## 7. MARKET STATE CLASSIFICATION MODULE

The Market State module classifies the current environment using direction, volatility, structure, and contextual risk.

It describes **what is**, not what to do.

---

## 8. FORECAST & RISK INTERPRETATION MODULE

The Forecast module estimates **probable future behavior** based on historical outcomes under similar market states.

It expresses uncertainty explicitly and never produces price targets.

---

## 9. ADVISORY GUIDANCE & LIQUIDITY FRAMING MODULE

### 9.1 Purpose

The Advisory Guidance module translates forecasts and risk interpretations into **behavioral guidance** for liquidity providers.

It exists to help avoid applying the wrong liquidity posture to the wrong market environment.

---

### 9.2 Guidance Scope

The module may suggest:
- Conservative posture
- Neutral posture
- Aggressive posture

Guidance is **advisory only** and never mandatory.

---

### 9.3 Liquidity Framing Rules

Liquidity framing may include:
- Directional bias (Long / Short / Neutral)
- Suggested range width (relative, not exact)
- Liquidity floor awareness based on risk and leverage
- Explicit liquidation-risk warnings

All liquidity framing must be:
- Derived from forecast and risk interpretation
- Expressed probabilistically
- Accompanied by confidence levels

---

### 9.4 Liquidity Floor Definition (Critical)

A liquidity floor is a **risk boundary**, not a prediction.

It is derived from:
- Current volatility
- Historical adverse move distributions
- Leverage mechanics (e.g., DeFiTuna constraints)

The system must never state that price *will not* cross a liquidity floor.

---

### 9.5 Forbidden Actions

The Advisory Guidance module must never:
- Execute trades
- Place or manage liquidity
- Optimize ranges for profit
- Override lower-layer evidence

It advises behavior only.

---

## 10. VERSION GOVERNANCE

- This document is frozen as **MASTER RULE BOOK v1.0**
- Any change requires a new version (v1.1, v2.0, etc.)
- Code must always conform to the active Rule Book

---

## FINAL STATEMENT

This system exists to replace assumption with evidence, reaction with understanding, and guesswork with structured thinking.

If evidence is weak, the system must be humble.  
If evidence is strong, the system must explain why.
