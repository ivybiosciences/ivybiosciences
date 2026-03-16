<div align="center">

# Ivy Biosciences

**AI-Powered Drug Discovery Platform**

[![License](https://img.shields.io/badge/License-FSL--1.1--Apache--2.0-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active%20Development-blue.svg)](https://ivybiosciences.com)

*Democratizing computational biology through natural language*

</div>

---

## Overview

Ivy Biosciences is a comprehensive drug discovery platform integrating AI tools across a broad range of scientific domains — from protein structure prediction to clinical genomics. Researchers interact through natural language queries without managing scripts, infrastructure, or computational pipelines.

The platform spans three purpose-built applications: a web interface for interactive research, a serverless GPU backend powering the science, and a terminal client for automation and power users.

### Scientific Domains

| Domain | Capabilities |
|--------|-------------|
| **Protein Structure & Design** | Structure prediction, de novo design, inverse folding, sequence design |
| **Antibody Engineering** | Numbering & CDR extraction, humanization, developability, affinity optimization |
| **Molecular Docking & Binding** | Flexible docking, CNN-based scoring, binding affinity & free energy prediction |
| **Drug Design** | Generative molecular design, fragment-based design, scaffold decoration |
| **ADMET & Pharmacology** | Pharmacokinetics, toxicity assessment, drug-likeness, PK/PD modeling |
| **Synthesis Planning** | Retrosynthetic route analysis, compound sourcing, fragment library search |
| **Genomics & Clinical** | Variant calling & classification, pharmacogenomics, neoantigen prediction |
| **Omics & Systems Biology** | Transcriptomics, single-cell analysis, epigenomics, spatial omics, metabolomics |
| **Literature & Data Mining** | Biomedical NLP, publication analysis, database federation |

---

## Platform Architecture

```
┌──────────────────────────────────────────────────────┐
│                                                      │
│  ┌─────────────┐         ┌─────────────────┐        │
│  │ ivybloom-cli│         │ ivybiosciences- │        │
│  │    (Go)     │────────▶│      next       │        │
│  │  CLI + TUI  │         │  (Next.js Web)  │        │
│  └─────────────┘         └────────┬────────┘        │
│                                   │                  │
│                                   ▼                  │
│                     ┌─────────────────────────┐     │
│                     │  ivybiosciences-modal   │     │
│                     │   (Python + Serverless) │     │
│                     │    AI Models on GPU     │     │
│                     └─────────────────────────┘     │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## Repositories

### [ivybiosciences-next](https://github.com/ivybiosciences/ivybiosciences-next)
**Web Application & API Gateway**

The primary web interface featuring a natural language orchestration engine, 3D molecular visualization, real-time job monitoring, and comprehensive export and reporting capabilities.

| | |
|---|---|
| **Frontend** | Next.js, React, TypeScript, Tailwind CSS |
| **Database** | PostgreSQL with row-level security |
| **Auth** | SSO, MFA, session management |
| **Hosting** | Vercel |

**Key Systems:**

- **AI Orchestration Engine** — Natural language interface with multi-provider LLM routing, intent detection, and automatic tool selection
- **Passport Intelligence** — Multi-source entity reports aggregating compound, target, safety, literature, and therapeutic area data into unified dossiers
- **Harness Runtime** — Session persistence with state checkpointing, rollback capability, and multi-client synchronization
- **Fragment Management** — SAFE (Sequential Attachment-based Fragment Embedding) system with auto-ingestion from synthesis workflows
- **Export Pipeline** — Normalized job results exported to PDF, DOCX, XLSX, PPTX, JSON, CSV, and specialty scientific formats
- **3D Visualization** — Mol\* viewer for protein structures, docking poses, binding sites, and surface analysis
- **Canvas & Collaboration** — Shared workspace with annotations, activity feed, and team project isolation

---

### [ivybiosciences-modal](https://github.com/ivybiosciences/ivybiosciences-modal)
**Serverless GPU Compute Backend**

Python-based backend with auto-scaling GPU resources for computationally intensive scientific workflows. Scales to zero when idle.

| | |
|---|---|
| **Compute** | Serverless GPU infrastructure |
| **API** | FastAPI |
| **Database** | PostgreSQL |
| **Cache** | Redis |

**Key Systems:**

- **Unified Tool Registry** — Centralized definitions with parameter validation, tier-based access control, and dispatch routing
- **Harness Framework** — Unified tool execution with job dispatch, state management, webhook callbacks, crash recovery, and enterprise extension points
- **Enhanced Output Schemas** — Multiple analysis levels with confidence scoring, applicability domain assessment, and uncertainty quantification
- **Biologics Common** — Shared utilities for PDB validation, antibody numbering, CDR extraction, liability scanning, and cross-app structure exchange
- **Artifact Storage** — S3-compatible storage for PDB structures, SDF molecules, MD trajectories, and batch manifests

---

### [ivybloom-cli](https://github.com/ivybiosciences/ivybloom-cli)
**Terminal Interface**

Go CLI with an interactive TUI dashboard, MCP server for AI assistant integration, and offline-first sync for disconnected environments.

| | |
|---|---|
| **Language** | Go |
| **CLI** | Cobra |
| **TUI** | Charmbracelet (Bubbletea, Lipgloss) |
| **MCP** | Model Context Protocol server |
| **Auth** | OAuth, API keys, device flow |

**Key Systems:**

- **Result Viewer System** — Job types automatically routed to specialized TUI viewers (metrics, tables, molecule grids, passport reports, synthesis route trees, artifacts, exports)
- **MCP Server** — Full Model Context Protocol server for AI assistant integration
- **Agent & Script Modes** — JSON envelope output for CI/CD, streaming text for shell scripts, and headless operation for automation
- **Session Checkpointing** — Point-in-time snapshots with rollback capability
- **Offline-First Sync** — Change queue for disconnected environments with automatic reconciliation

---

## Key Features

- **Natural Language Interface** — Query scientific tools conversationally
- **Passport Intelligence** — Comprehensive entity dossiers for compounds, targets, safety profiles, literature, and therapeutic areas
- **3D Molecular Visualization** — Mol\* viewer for proteins, docking poses, and binding sites
- **Real-time Job Monitoring** — Live progress tracking
- **Multi-format Export** — PDF, DOCX, XLSX, PPTX, JSON, CSV, PDB, SDF, and specialty scientific formats
- **Guest Mode** — Try without an account (rate-limited)
- **CLI + TUI + MCP** — Terminal interface with batch processing, interactive dashboard, and AI assistant integration
- **Auto-scaling GPU** — Serverless compute that scales to zero when idle
- **Self-Hosting** — Deploy on your own infrastructure for data sovereignty

---

## Tech Stack

### Languages
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white)

### Frontend
![React](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Next.js](https://img.shields.io/badge/-Next.js-000000?style=flat-square&logo=next.js&logoColor=white)
![Tailwind](https://img.shields.io/badge/-Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)

### Backend & Infrastructure
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/-Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Vercel](https://img.shields.io/badge/-Vercel-000000?style=flat-square&logo=vercel&logoColor=white)

### Scientific Computing
![Mol*](https://img.shields.io/badge/-Mol*-4A90E2?style=flat-square)
![RDKit](https://img.shields.io/badge/-RDKit-FF6B6B?style=flat-square)
![D3](https://img.shields.io/badge/-D3.js-F9A03C?style=flat-square&logo=d3dotjs&logoColor=white)

---

## Security

- **Authentication** — SSO, MFA, session management, API key validation
- **Row-Level Security** — Database-level access policies per user and project
- **CSRF Protection** — Token validation on all state-changing requests
- **Rate Limiting** — Request throttling with tiered limits
- **Audit Logging** — Comprehensive activity tracking and compliance controls
- **API Protection** — Tiered access control with RBAC
- **HMAC Auth** — Machine-to-machine authentication for backend services

---

## License

All public repositories use **FSL-1.1-Apache-2.0** (Functional Source License).

- **Allowed:** Self-hosting, internal use, building integrations, CRO client work
- **Not Allowed:** Offering as competing SaaS (until Apache conversion in 2 years)

---

## Documentation & Resources

- **Documentation:** [ivybiosciences.com/docs](https://ivybiosciences.com/documentation)
- **Self-Hosting:** [Self-Hosting Guide](https://github.com/ivybiosciences/ivybiosciences-next/blob/main/docs/self-hosting/README.md)
- **API Reference:** Available in each repository
- **GitHub:** [github.com/ivybiosciences](https://github.com/ivybiosciences)

---

## Support

- **GitHub Issues:** Report bugs in respective repositories
- **Email:** support@ivybiosciences.com
- **Enterprise:** admin@ivybiosciences.com

---

<div align="center">

*Advancing biotechnology through innovative and disruptive approaches*

[![GitHub followers](https://img.shields.io/github/followers/ivybiosciences?style=social)](https://github.com/ivybiosciences)
[![Twitter Follow](https://img.shields.io/twitter/follow/ivybiosciences?style=social)](https://twitter.com/ivybiosciences)

</div>
