<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,100:1D4ED8&height=180&section=header&text=Doron%20Firman&fontSize=48&fontColor=FFFFFF&fontAlignY=38&desc=Distributed%20Systems%20%C2%B7%20Backend%20%C2%B7%20AI%20Developer%20Infrastructure&descAlignY=60&descSize=18" width="100%" />

<a href="https://doronf3.github.io"><img src="https://img.shields.io/badge/Architecture%20Dossier-doronf3.github.io-1D4ED8?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Architecture Dossier" /></a>
<a href="https://linkedin.com/in/doronf3"><img src="https://img.shields.io/badge/LinkedIn-Doron%20Firman-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="mailto:doronfi3@gmail.com"><img src="https://img.shields.io/badge/Email-Contact%20Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>

<br><br>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=20&duration=3000&pause=1000&color=3B82F6&center=true&vCenter=true&width=700&lines=Building+distributed+systems+at+scale;Engineering+zero-downtime+migrations;Building+deterministic+AI+developer+tooling;Reliability+%7C+Observability+%7C+Automation" alt="Typing SVG" />

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

## 🏛️ Featured Systems

### 📊 1. Multi-Channel Pipeline Observability

> **Building end-to-end visibility into distributed mobile and web delivery pipelines.**

```mermaid
flowchart LR
    subgraph Channels ["Delivery Channels"]
        direction TB
        iOS["iOS Delivery"]
        Android["Android Delivery"]
        Web["Web Delivery"]
    end

    subgraph Pipeline ["Unified Telemetry Pipeline"]
        Schema["Structured Event Schema"]
        Stream["Streaming Metrics & Aggregation"]
    end

    subgraph Ops ["Operations & Triage"]
        direction TB
        Dash["Centralized Dashboards"]
        Triage["Real-Time Incident Triage"]
    end

    iOS --> Schema
    Android --> Schema
    Web --> Schema
    Schema -->|"Correlation ID + Stage"| Stream
    Stream --> Dash
    Stream --> Triage

    classDef source fill:#1E293B,stroke:#64748B,color:#F8FAFC
    classDef core fill:#1D4ED8,stroke:#60A5FA,color:#FFFFFF
    classDef outcome fill:#065F46,stroke:#34D399,color:#FFFFFF

    class iOS,Android,Web source
    class Schema,Stream core
    class Dash,Triage outcome
```

* **Problem:** Distributed delivery across iOS, Android, and web created fragmented visibility, making it hard to pinpoint where notifications failed.
* **Architecture:** Standardized structured event schemas across every delivery stage, unified cross-platform telemetry, and aggregated streaming metrics into centralized triage dashboards with end-to-end correlation.
* **Impact:** **100% channel traceability** with substantially faster incident investigation.

<details>
<summary><b>🔍 Technical Deep Dive</b></summary>

<br>

The core design principle was treating observability as part of the **system contract** rather than an afterthought. Every delivery stage emits structured events with enough context to correlate a request across services and platforms, enabling:

* End-to-end request reconstruction
* Stage-level failure identification
* Real-time streaming aggregation
* Cross-platform delivery comparison
* Faster root-cause analysis

</details>

---

### 🔄 2. Zero-Downtime Service & Identity Migration

> **Migrating 100M+ active user and device records without interrupting production traffic.**

```mermaid
flowchart LR
    Traffic(["Production Traffic — 100M+ Records"]) --> Router["Traffic Router"]

    Router -->|"Primary Traffic"| Legacy["Legacy Identity Service"]
    Router -.->|"Shadow / Gradual Ramp"| Modern["Modern Identity Service"]

    Legacy --> Diff["Shadow Evaluator & Consistency Checks"]
    Modern --> Diff

    Diff -->|"100% Parity Verified"| Ramp["Ramp Controller — 1% → 10% → 50% → 100%"]
    Ramp -.->|"Promote Weight / Cutover"| Router

    classDef entry fill:#0F172A,stroke:#3B82F6,color:#F8FAFC
    classDef legacy fill:#334155,stroke:#94A3B8,color:#E2E8F0
    classDef modern fill:#1D4ED8,stroke:#60A5FA,color:#FFFFFF
    classDef gate fill:#065F46,stroke:#34D399,color:#FFFFFF

    class Traffic,Router entry
    class Legacy legacy
    class Modern,Diff modern
    class Ramp gate
```

* **Problem:** A deprecated identity service had to be replaced while preserving production availability and preventing user mis-targeting.
* **Strategy:** **Dark launch** → **Live shadow evaluation** → **Automated consistency verification** → **Incremental traffic ramp** → **Controlled cutover**.

| Metric              |                           Result |
| ------------------- | -------------------------------: |
| Records migrated    |                        **100M+** |
| Production downtime |                            **0** |
| Data consistency    |                **100% verified** |
| Deployment strategy | **Dark launch + shadow traffic** |

<details>
<summary><b>🔍 Why This Architecture</b></summary>

<br>

Offline validation alone cannot prove behavioral equivalence under real production load. Shadow evaluation turns a high-risk cutover into a controlled, reversible rollout:

```mermaid
flowchart LR
    P1["Offline Validation"] --> P2["Dark Launch"] --> P3["Shadow Traffic"] --> P4["Parity Checks"] --> P5["Gradual Ramp"] --> P6["Full Cutover"]

    classDef step fill:#1E293B,stroke:#3B82F6,color:#F8FAFC
    classDef final fill:#065F46,stroke:#34D399,color:#FFFFFF
    class P1,P2,P3,P4,P5 step
    class P6 final
```

</details>

---

### 🤖 3. Deterministic AI Developer Tooling

> **Making AI coding workflows behave like reliable software systems.**

```mermaid
flowchart LR
    subgraph Runtime ["Runtime Execution Path"]
        Agent["AI Coding Agent"] -->|"Tool Invocation"| Schema["Strict Schema Gate"]
        Schema -->|"Valid Payload"| CLI["Compiled Deterministic CLI"]
        Schema -.->|"Structured Error Feedback"| Agent
        CLI --> Result["Validated Output"]
    end

    subgraph Quality ["CI & Model-Upgrade Verification"]
        Hermetic["Hermetic Test Suite"] --> Evals["Golden Evals — 99.4%"] --> Reg["Regression Gate"]
    end

    CLI -.->|"Tested By"| Hermetic
    Reg -.->|"Protects Model Updates"| Agent

    classDef ai fill:#312E81,stroke:#818CF8,color:#FFFFFF
    classDef det fill:#1D4ED8,stroke:#60A5FA,color:#FFFFFF
    classDef guard fill:#065F46,stroke:#34D399,color:#FFFFFF
    classDef neutral fill:#1E293B,stroke:#64748B,color:#F8FAFC

    class Agent ai
    class Schema,CLI,Result det
    class Hermetic,Evals,Reg guard
```

* **Problem:** Raw natural-language prompt instructions are fragile—leading to hallucinated commands, invalid CLI syntax, context bloat, and silent regressions after model updates.
* **Approach:** Moved critical workflows out of prompts into compiled CLI interfaces with strict schemas, explicit validation gates, hermetic tests, and automated golden eval suites.
* **Impact:** **99.4% tool execution accuracy** with automated regression protection across model upgrades.

<details>
<summary><b>🔍 Engineering Principle</b></summary>

<br>

The goal is not to make an LLM deterministic—it is to make the **interface around the LLM deterministic**.

```mermaid
flowchart LR
    M1["Probabilistic Model"] --> M2["Structured Tool Contract"] --> M3["Deterministic Execution"] --> M4["Automated Verification"]

    classDef ai fill:#312E81,stroke:#818CF8,color:#FFFFFF
    classDef det fill:#1D4ED8,stroke:#60A5FA,color:#FFFFFF
    classDef ok fill:#065F46,stroke:#34D399,color:#FFFFFF
    class M1 ai
    class M2,M3 det
    class M4 ok
```

</details>

---

## 🧰 Technical Stack

### Languages
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=openjdk&logoColor=white" alt="Java" />
</p>

### Distributed Systems & Backend
<p>
  <img src="https://img.shields.io/badge/gRPC-244C5A?style=for-the-badge&logo=grpc&logoColor=white" alt="gRPC" />
  <img src="https://img.shields.io/badge/Protobuf-4285F4?style=for-the-badge" alt="Protobuf" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/SQL-336791?style=for-the-badge" alt="SQL" />
  <img src="https://img.shields.io/badge/NoSQL-47A248?style=for-the-badge" alt="NoSQL" />
</p>

`Distributed Messaging` · `Event-Driven Architecture` · `Microservices` · `APIs` · `RPC` · `Data Pipelines`

### AI & Developer Infrastructure
<p>
  <img src="https://img.shields.io/badge/AI_Agents-111827?style=for-the-badge" alt="AI Agents" />
  <img src="https://img.shields.io/badge/Tool_Calling-374151?style=for-the-badge" alt="Tool Calling" />
  <img src="https://img.shields.io/badge/LLM_Evaluation-7B1FA2?style=for-the-badge" alt="LLM Evaluation" />
  <img src="https://img.shields.io/badge/Golden_Tests-FF6F00?style=for-the-badge" alt="Golden Tests" />
  <img src="https://img.shields.io/badge/Automation-059669?style=for-the-badge" alt="Automation" />
</p>

`Agent Harnesses` · `Evaluation Pipelines` · `Deterministic Tooling` · `Regression Testing` · `Developer Experience`

---

## 🧠 Engineering Principles

<table>
<tr>
<td width="50%" valign="top">

### Reliability
Design systems around failure rather than assuming success.

</td>
<td width="50%" valign="top">

### Determinism
Move critical behavior from implicit assumptions into explicit contracts.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### Observability
If a system cannot explain what happened, it is difficult to operate.

</td>
<td width="50%" valign="top">

### Automation
Anything repeatedly verified manually should eventually become a test.

</td>
</tr>
</table>

---

## 🔬 Areas of Interest

```text
Distributed Systems                 AI Developer Infrastructure       Developer Infrastructure
├── High-scale backend services     ├── AI agents                     ├── CLI tooling
├── Event-driven architectures      ├── Tool execution                ├── Automation
├── Messaging & streaming           ├── Agent harnesses               ├── CI/CD
├── Service reliability             ├── Evaluation systems            ├── Observability
└── Zero-downtime migrations        └── Regression testing            └── Developer experience
```

---

## 📈 GitHub Activity

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=doronf3&show_icons=true&hide_border=true&count_private=true&include_all_commits=true&bg_color=0D1117&title_color=60A5FA&icon_color=3B82F6&text_color=E2E8F0">
  <img height="170" alt="GitHub Stats" src="https://github-readme-stats.vercel.app/api?username=doronf3&show_icons=true&hide_border=true&count_private=true&include_all_commits=true&bg_color=FFFFFF&title_color=1D4ED8&icon_color=1D4ED8&text_color=0F172A">
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=doronf3&layout=compact&hide_border=true&langs_count=8&bg_color=0D1117&title_color=60A5FA&text_color=E2E8F0">
  <img height="170" alt="Top Languages" src="https://github-readme-stats.vercel.app/api/top-langs/?username=doronf3&layout=compact&hide_border=true&langs_count=8&bg_color=FFFFFF&title_color=1D4ED8&text_color=0F172A">
</picture>

<br><br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-streak-stats.herokuapp.com/?user=doronf3&hide_border=true&background=0D1117&ring=3B82F6&fire=60A5FA&currStreakLabel=60A5FA&sideLabels=E2E8F0&currStreakNum=FFFFFF&sideNums=FFFFFF&dates=94A3B8">
  <img alt="GitHub Streak" src="https://github-readme-streak-stats.herokuapp.com/?user=doronf3&hide_border=true&background=FFFFFF&ring=1D4ED8&fire=1D4ED8&currStreakLabel=1D4ED8&sideLabels=0F172A&currStreakNum=0F172A&sideNums=0F172A&dates=475569">
</picture>

<br><br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/doronf3/doronf3/output/github-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/doronf3/doronf3/output/github-snake.svg">
  <img alt="GitHub contribution snake" src="https://raw.githubusercontent.com/doronf3/doronf3/output/github-snake.svg">
</picture>

</div>

---

## 🏗️ Architecture Dossier

<div align="center">

I write detailed technical breakdowns of systems, architecture decisions, migrations, and engineering trade-offs.

<br>

<a href="https://doronf3.github.io"><img src="https://img.shields.io/badge/Explore%20the%20Architecture%20Dossier-1D4ED8?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Explore the Architecture Dossier" /></a>

<br><br>

**System Designs · Architecture Case Studies · Engineering Writeups**

---

### Building systems that scale.
### Building tools that make them easier to build.

<br>

<a href="https://doronf3.github.io">Website</a> •
<a href="https://linkedin.com/in/doronf3">LinkedIn</a> •
<a href="mailto:doronfi3@gmail.com">Email</a>

<br><br>

<img src="https://komarev.com/ghpvc/?username=doronf3&style=flat-square&color=1D4ED8" alt="Profile views" />

</div>
