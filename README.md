<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,100:1D4ED8&height=180&section=header&text=Doron%20Firman&fontSize=48&fontColor=FFFFFF&fontAlignY=38&desc=Distributed%20Systems%20%C2%B7%20Backend%20%C2%B7%20AI%20Developer%20Infrastructure&descAlignY=60&descSize=18" width="100%" />

<a href="https://doronf3.github.io">
  <img src="https://img.shields.io/badge/Architecture%20Dossier-doronf3.github.io-1D4ED8?style=for-the-badge&logo=google-chrome&logoColor=white" />
</a>
<a href="https://linkedin.com/in/doronf3">
  <img src="https://img.shields.io/badge/LinkedIn-Doron%20Firman-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
</a>
<a href="mailto:doronfi3@gmail.com">
  <img src="https://img.shields.io/badge/Email-Contact%20Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white" />
</a>

<br><br>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=20&duration=3000&pause=1000&color=3B82F6&center=true&vCenter=true&width=700&lines=Building+distributed+systems+at+scale;Engineering+zero-downtime+migrations;Building+deterministic+AI+developer+tooling;Reliability+%7C+Observability+%7C+Automation" />

</div>

---

## ⚡ Engineering at a Glance

<table>
<tr>
<td align="center" width="25%">

### 100M+

**Active Records**

Migrated across identity infrastructure

</td>
<td align="center" width="25%">

### 0

**Downtime**

During large-scale service migration

</td>
<td align="center" width="25%">

### 99.4%

**Tool Accuracy**

Deterministic AI developer tooling

</td>
<td align="center" width="25%">

### 100%

**Traceability**

Across delivery channels

</td>
</tr>
</table>

---

# 🏛️ Featured Systems

## 📊 Multi-Channel Pipeline Observability

> **Building visibility into distributed mobile and web delivery pipelines.**

```text
 ┌──────────────┐
 │     iOS      │
 └──────┬───────┘
        │
 ┌──────▼───────┐
 │   Android    │
 └──────┬───────┘
        │
 ┌──────▼───────┐
 │      Web     │
 └──────┬───────┘
        │
        ▼
 ┌─────────────────────┐
 │ Structured Events   │
 │ & Delivery Signals  │
 └──────────┬──────────┘
            │
            ▼
 ┌─────────────────────┐
 │ Streaming Metrics   │
 │ & Aggregation       │
 └──────────┬──────────┘
            │
            ▼
 ┌─────────────────────┐
 │ Real-Time Triage    │
 │ & Observability     │
 └─────────────────────┘
```

### The Problem

Distributed delivery across multiple platforms created fragmented visibility and made it difficult to determine where a notification failed.

### The Architecture

* Standardized structured event schemas across delivery stages
* Unified iOS, Android, and web delivery telemetry
* Aggregated streaming metrics into centralized dashboards
* Created end-to-end correlation across the delivery pipeline
* Enabled real-time incident triage

### Impact

**100% channel traceability** with substantially faster incident investigation.

<details>
<summary><b>🔍 Technical Deep Dive</b></summary>

<br>

The core design principle was to treat observability as part of the system contract rather than an afterthought.

Every delivery stage emits structured events with enough context to correlate a request across services and platforms.

This enables:

* End-to-end request reconstruction
* Stage-level failure identification
* Real-time aggregation
* Cross-platform comparison
* Faster root-cause analysis

</details>

---

## 🔄 Zero-Downtime Service & Identity Migration

> **Migrating 100M+ active user and device records without interrupting production traffic.**

```text
                         Production Traffic
                                │
                                ▼
                       ┌─────────────────┐
                       │ Traffic Router  │
                       └────────┬────────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
                    ▼                       ▼
             ┌─────────────┐        ┌─────────────┐
             │   Legacy    │        │    Modern   │
             │   Service   │        │   Service   │
             └──────┬──────┘        └──────┬──────┘
                    │                       │
                    │      Shadow Read      │
                    └───────────┬───────────┘
                                ▼
                     ┌────────────────────┐
                     │ Consistency &      │
                     │ Behavioral Checks  │
                     └─────────┬──────────┘
                               │
                               ▼
                     ┌────────────────────┐
                     │ Gradual Traffic    │
                     │ Ramp               │
                     │ 1% → 10% → 50%...  │
                     └─────────┬──────────┘
                               │
                               ▼
                         ┌───────────┐
                         │ Cutover   │
                         └───────────┘
```

### The Problem

A deprecated identity service needed to be replaced while maintaining production availability and ensuring that migrated users and devices remained correctly targeted.

### The Strategy

**1. Dark Launch**

Deploy the new infrastructure without immediately serving production traffic.

**2. Shadow Evaluation**

Run the new system alongside the existing implementation and compare behavior on live traffic.

**3. Consistency Verification**

Validate records and behavioral results before allowing the new system to become authoritative.

**4. Gradual Traffic Ramp**

Move traffic incrementally while continuously monitoring correctness and system health.

**5. Controlled Cutover**

Complete the migration only after the new path demonstrated production consistency.

### Impact

| Metric              |                           Result |
| ------------------- | -------------------------------: |
| Records migrated    |                        **100M+** |
| Production downtime |                            **0** |
| Data consistency    |                **100% verified** |
| Deployment strategy | **Dark launch + shadow traffic** |

<details>
<summary><b>🔍 Why This Architecture</b></summary>

<br>

The migration was designed around the assumption that correctness cannot be established solely through offline validation.

Shadow evaluation allows the replacement system to be tested against real production behavior before it becomes authoritative.

The migration therefore becomes a controlled experiment:

```text
Offline Validation
       ↓
Dark Launch
       ↓
Shadow Traffic
       ↓
Behavior Comparison
       ↓
Small Traffic Percentage
       ↓
Continuous Verification
       ↓
Gradual Ramp
       ↓
Full Cutover
```

</details>

---

## 🤖 Deterministic AI Developer Tooling

> **Making AI coding workflows behave more like reliable software systems.**

```text
                 ┌──────────────┐
                 │   AI Agent   │
                 └──────┬───────┘
                        │
                        ▼
               ┌─────────────────┐
               │ Structured Tool │
               │     Schema      │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │ Deterministic   │
               │      CLI        │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │ Validation      │
               │     Gates       │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │ Hermetic Tests  │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │ Golden Evals    │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │ Regression      │
               │ Protection      │
               └─────────────────┘
```

### The Problem

Natural-language instructions alone are a fragile interface for AI agents.

Common failure modes include:

* Hallucinated commands
* Invalid parameters
* Incorrect CLI syntax
* Ambiguous tool behavior
* Context bloat
* Regressions caused by model updates

### The Approach

Instead of relying exclusively on prompts, move critical behavior into deterministic software:

* Compiled CLI interfaces
* Strict schemas
* Explicit validation
* Hermetic execution
* Golden test suites
* Automated evaluation
* Regression detection across model versions

### Impact

**99.4% tool execution accuracy** with automated regression protection against model changes.

<details>
<summary><b>🔍 Engineering Principle</b></summary>

<br>

The goal is not to make an LLM deterministic.

The goal is to make the **interface around the LLM deterministic**.

```text
          Probabilistic Model
                  │
                  ▼
        ┌──────────────────┐
        │ Structured Tool  │
        │ Interface        │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Deterministic    │
        │ Execution        │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Automated        │
        │ Verification     │
        └──────────────────┘
```

</details>

---

# 🧰 Technical Stack

### Languages

<p>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=openjdk&logoColor=white" />
</p>

### Distributed Systems & Backend

<p>
<img src="https://img.shields.io/badge/gRPC-244C5A?style=for-the-badge&logo=grpc&logoColor=white" />
<img src="https://img.shields.io/badge/Protobuf-4285F4?style=for-the-badge" />
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/SQL-336791?style=for-the-badge" />
<img src="https://img.shields.io/badge/NoSQL-47A248?style=for-the-badge" />
</p>

`Distributed Messaging` · `Event-Driven Architecture` · `Microservices` · `APIs` · `RPC` · `Data Pipelines`

### AI & Developer Infrastructure

<p>
<img src="https://img.shields.io/badge/AI_Agents-111827?style=for-the-badge" />
<img src="https://img.shields.io/badge/Tool_Calling-374151?style=for-the-badge" />
<img src="https://img.shields.io/badge/LLM_Evaluation-7B1FA2?style=for-the-badge" />
<img src="https://img.shields.io/badge/Golden_Tests-FF6F00?style=for-the-badge" />
<img src="https://img.shields.io/badge/Automation-059669?style=for-the-badge" />
</p>

`Agent Harnesses` · `Evaluation Pipelines` · `Deterministic Tooling` · `Regression Testing` · `Developer Experience`

---

# 🧠 Engineering Principles

<table>
<tr>
<td width="50%">

### Reliability

Design systems around failure rather than assuming success.

</td>
<td width="50%">

### Determinism

Move critical behavior from implicit assumptions into explicit contracts.

</td>
</tr>
<tr>
<td width="50%">

### Observability

If a system cannot explain what happened, it is difficult to operate.

</td>
<td width="50%">

### Automation

Anything repeatedly verified manually should eventually become a test.

</td>
</tr>
</table>

---

# 🔬 Areas of Interest

```text
Distributed Systems
├── High-scale backend services
├── Event-driven architectures
├── Messaging & streaming
├── Service reliability
└── Zero-downtime migrations

AI Developer Infrastructure
├── AI agents
├── Tool execution
├── Agent harnesses
├── Evaluation systems
└── Regression testing

Developer Infrastructure
├── CLI tooling
├── Automation
├── CI/CD
├── Observability
└── Developer experience
```

---

# 📈 GitHub

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=doronf3&show_icons=true&hide_border=true&count_private=true&include_all_commits=true" height="170" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=doronf3&layout=compact&hide_border=true&langs_count=8" height="170" />

<br><br>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=doronf3&hide_border=true" />

</div>

---

# 🐍 Contribution Activity

<div align="center">

<img src="https://raw.githubusercontent.com/doronf3/doronf3/output/github-contribution-grid-snake.svg" alt="GitHub Contribution Snake" />

</div>

---

# 🏗️ Architecture Dossier

I write detailed technical breakdowns of systems, architecture decisions, migrations, and engineering problems.

<div align="center">

<a href="https://doronf3.github.io">

<img src="https://img.shields.io/badge/Explore%20the%20Architecture%20Dossier-1D4ED8?style=for-the-badge&logo=google-chrome&logoColor=white" />

</a>

<br><br>

**System Designs · Architecture Case Studies · Engineering Writeups**

</div>

---

<div align="center">

### Building systems that scale.

### Building tools that make them easier to build.

<br>

<a href="https://doronf3.github.io">Website</a>
 •  <a href="https://linkedin.com/in/doronf3">LinkedIn</a>
 •  <a href="mailto:doronfi3@gmail.com">Email</a>

<br><br>

<img src="https://komarev.com/ghpvc/?username=doronf3&style=flat-square&color=1D4ED8" alt="Profile views" />

</div>
