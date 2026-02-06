<div align="center">

# Ivy Biosciences

**AI-Powered Drug Discovery Platform**

[![License](https://img.shields.io/badge/License-FSL--1.1--Apache--2.0-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Public%20Beta-blue.svg)](https://ivybiosciences.com)
[![Node.js](https://img.shields.io/badge/Node.js-%3E%3D20-brightgreen.svg)](https://nodejs.org/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org/)
[![Go](https://img.shields.io/badge/Go-1.24+-00ADD8.svg)](https://golang.org/)

*Democratizing computational biology through natural language*

</div>

---

## Overview

Ivy Biosciences is a comprehensive drug discovery platform integrating **36+ AI models** for molecular design, protein analysis, and biomedical research. Researchers can interact through natural language queries like *"Fold this protein and dock it with aspirin"* without requiring deep computational expertise.

### Core Capabilities

| Category | Models & Tools |
|----------|---------------|
| **Protein Analysis** | ESMFold, binding site detection, BLAST, HMMER |
| **Molecular Docking** | DiffDock, AutoDock Vina, scoring functions |
| **Drug Design** | REINVENT4, fragment libraries, scaffold hopping |
| **ADMET Profiling** | ADMETLab3, ProTox3, drug-likeness |
| **Synthesis Planning** | AiZynthFinder, retrosynthetic routes |
| **Literature Mining** | BioBERT, PubMed analysis |
| **Genomics** | Scanpy, scVI for single-cell analysis |

---

## Platform Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  ┌─────────────┐         ┌─────────────────┐         ┌───────────┐ │
│  │ ivybloom-cli│         │ ivybiosciences- │         │ ivylaunch │ │
│  │    (Go)     │────────▶│      next       │         │ (Remotion)│ │
│  │  CLI + TUI  │         │  (Next.js Web)  │         │  Videos   │ │
│  └─────────────┘         └────────┬────────┘         └───────────┘ │
│                                   │                                 │
│                                   ▼                                 │
│                     ┌─────────────────────────┐                    │
│                     │  ivybiosciences-modal   │                    │
│                     │   (Python + Modal.com)  │                    │
│                     │   36+ AI Models on GPU  │                    │
│                     └─────────────────────────┘                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Repositories

### [ivybiosciences-next](https://github.com/ivybiosciences/ivybiosciences-next)
**Next.js Web Application & API Gateway**

The primary web interface featuring natural language orchestration, 3D molecular visualization (Mol*), real-time job monitoring, and comprehensive export capabilities.

| Stack | |
|-------|---|
| Frontend | Next.js 14, React 18, TypeScript 5.9+, Tailwind CSS v4, MUI v7 |
| Database | Supabase (PostgreSQL + RLS) |
| Auth | Clerk (SSO, MFA) |
| State | Zustand + React Query v5 |
| Hosting | Vercel |

```bash
cd ~/ivybiosciences-next
npm run dev    # Start development server
```

---

### [ivybiosciences-modal](https://github.com/ivybiosciences/ivybiosciences-modal)
**Serverless GPU Compute Backend**

Python-based backend running on Modal.com infrastructure with auto-scaling GPU resources (A100, A10G, T4) for computationally intensive scientific workflows.

| Stack | |
|-------|---|
| Compute | Modal.com (serverless GPU) |
| API | FastAPI |
| Database | PostgreSQL (async SQLAlchemy) |
| Cache | Upstash Redis |

```bash
cd ~/ivybiosciences-modal
modal deploy ivyai/server_app_modal_refactor/main.py
```

---

### [ivybloom-cli](https://github.com/ivybiosciences/ivybloom-cli)
**Terminal Interface**

Production-ready Go CLI with an interactive TUI dashboard for power users, batch processing, and CI/CD integration.

| Stack | |
|-------|---|
| Language | Go 1.24+ |
| CLI | Cobra |
| TUI | Charmbracelet (Bubbletea, Lipgloss) |
| Auth | Browser OAuth, API keys, device flow |

```bash
# Installation
brew install ivybiosciences/tap/ivybloom
# or
npm install -g ivybloom
# or
curl -fsSL https://raw.githubusercontent.com/ivybiosciences/ivybloom-cli/main/install.sh | bash

# Usage
ivybloom auth login
ivybloom run esmfold protein_sequence=MKLLVLGLVGFGVG
ivybloom tui  # Interactive dashboard
```

---

### [ivylaunch](https://github.com/ivybiosciences/ivylaunch)
**Video Generation**

Remotion-based video generation for marketing and launch campaigns. Produces multiple compositions from 45s teasers to 2.5min showcases.

| Stack | |
|-------|---|
| Framework | Remotion 4.0 |
| Frontend | React 19, TypeScript |
| Output | 1920x1080 @ 30fps MP4 |

```bash
cd ~/ivylaunch
npm start           # Remotion Studio
npm run build:all   # Render all compositions
```

---

## Tech Stack Overview

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
![Supabase](https://img.shields.io/badge/-Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)
![Redis](https://img.shields.io/badge/-Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Modal](https://img.shields.io/badge/-Modal.com-000000?style=flat-square)
![Vercel](https://img.shields.io/badge/-Vercel-000000?style=flat-square&logo=vercel&logoColor=white)

### Scientific Computing
![Mol*](https://img.shields.io/badge/-Mol*-4A90E2?style=flat-square)
![RDKit](https://img.shields.io/badge/-RDKit-FF6B6B?style=flat-square)
![BioBERT](https://img.shields.io/badge/-BioBERT-9B59B6?style=flat-square)

---

## Key Features

- **Natural Language Interface** - Query AI models conversationally
- **36+ Integrated AI Models** - ESMFold, DiffDock, REINVENT4, ADMET, and more
- **3D Molecular Visualization** - Mol* viewer for proteins and molecules
- **Real-time Job Monitoring** - WebSocket-based progress tracking
- **Multi-format Export** - PDF, XLSX, PPTX, SVG, PDB, SDF
- **Guest Mode** - Try without account (rate-limited)
- **CLI + TUI** - Full terminal interface with batch processing
- **Auto-scaling GPU** - A100, A10G, T4 via Modal.com

---

## Security

- **Clerk Authentication** - SSO, MFA, session management
- **Row-Level Security** - Supabase RLS policies
- **CSRF Protection** - Token validation
- **Rate Limiting** - Upstash-based throttling
- **Audit Logging** - Comprehensive activity tracking
- **API Protection** - Tiered access control

---

## License

All public repositories use **FSL-1.1-Apache-2.0** (Functional Source License).

- **Allowed:** Self-hosting, internal use, building integrations
- **Not Allowed:** Offering as competing SaaS (until Apache conversion in 2 years)

---

## Documentation & Resources

- **Documentation:** [ivybiosciences.com/docs](https://ivybiosciences.com/documentation)
- **API Reference:** Available in each repository's docs
- **GitHub:** [github.com/ivybiosciences](https://github.com/ivybiosciences)

---

## Support

- **GitHub Issues:** Report bugs in respective repositories
- **Email:** support@ivybiosciences.com
- **Enterprise:** admin@ivybiosciences.com

---

<div align="center">

*Advancing biotechnology through innovative and accessible computational tools*

[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.19.5-brightgreen.svg)](https://nodejs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.9+-blue.svg)](https://www.typescriptlang.org/)
[![Next.js](https://img.shields.io/badge/Next.js-14.2+-black.svg)](https://nextjs.org/)
[![GitHub followers](https://img.shields.io/github/followers/ivybiosciences?style=social)](https://github.com/ivybiosciences)
[![Twitter Follow](https://img.shields.io/twitter/follow/ivybiosciences?style=social)](https://twitter.com/ivybiosciences)

</div>
