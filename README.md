# ⚡ BXB AI Studio

<div align="center">

![BXB AI Studio Banner](https://img.shields.io/badge/BXB--AI--Studio-v1.0.0-6C5CE7?style=for-the-badge&logo=openai&logoColor=white)
![Build Status](https://img.shields.io/badge/Build-Passing-00B894?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-0984E3?style=for-the-badge)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-00CEC9?style=for-the-badge)

**Next-Generation Multi-Model AI Collaboration Suite & Studio**

An all-in-one platform for interacting with LLMs, generating multimedia assets, running automated workflows, and managing AI agents in a unified dark-themed visual workspace.

</div>

---

## 📌 Architecture Overview

```svg
<svg xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)" viewBox="0 0 680 240" width="100%" role="img" aria-label="BXB AI Studio Architecture Overview">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor" opacity="0.6"/>
    </marker>
  </defs>

  <!-- Client Layer -->
  <rect x="20" y="30" width="160" height="180" rx="12" fill="none" stroke="currentColor" stroke-dasharray="4,4" opacity="0.4"/>
  <text x="100" y="52" fill="currentColor" font-size="13" font-weight="bold" text-anchor="middle">Client Layer</text>
  
  <rect x="35" y="70" width="130" height="40" rx="8" fill="currentColor" fill-opacity="0.1" stroke="currentColor"/>
  <text x="100" y="95" fill="currentColor" font-size="12" text-anchor="middle">Web Dashboard UI</text>
  
  <rect x="35" y="125" width="130" height="40" rx="8" fill="currentColor" fill-opacity="0.1" stroke="currentColor"/>
  <text x="100" y="150" fill="currentColor" font-size="12" text-anchor="middle">Agent Canvas & Studio</text>

  <!-- Connectors Client to API -->
  <path d="M 180 90 L 230 90" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <path d="M 180 145 L 230 145" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Core API Gateway -->
  <rect x="235" y="55" width="180" height="130" rx="12" fill="currentColor" fill-opacity="0.08" stroke="currentColor" stroke-width="2"/>
  <text x="325" y="82" fill="currentColor" font-size="14" font-weight="bold" text-anchor="middle">BXB Core Engine</text>
  
  <rect x="250" y="100" width="150" height="30" rx="6" fill="currentColor" fill-opacity="0.12" stroke="currentColor"/>
  <text x="325" y="120" fill="currentColor" font-size="11" text-anchor="middle">Model Router & Orchestrator</text>
  
  <rect x="250" y="140" width="150" height="30" rx="6" fill="currentColor" fill-opacity="0.12" stroke="currentColor"/>
  <text x="325" y="160" fill="currentColor" font-size="11" text-anchor="middle">Prompt & Memory Manager</text>

  <!-- Connectors Core to Providers -->
  <path d="M 415 100 L 465 75" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <path d="M 415 120 L 465 120" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <path d="M 415 140 L 465 165" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- AI Models Layer -->
  <rect x="470" y="30" width="190" height="180" rx="12" fill="none" stroke="currentColor" stroke-dasharray="4,4" opacity="0.4"/>
  <text x="565" y="52" fill="currentColor" font-size="13" font-weight="bold" text-anchor="middle">AI Provider Integrations</text>
  
  <rect x="485" y="60" width="160" height="32" rx="6" fill="currentColor" fill-opacity="0.1" stroke="currentColor"/>
  <text x="565" y="81" fill="currentColor" font-size="11" text-anchor="middle">OpenAI / Claude / Gemini</text>
  
  <rect x="485" y="104" width="160" height="32" rx="6" fill="currentColor" fill-opacity="0.1" stroke="currentColor"/>
  <text x="565" y="125" fill="currentColor" font-size="11" text-anchor="middle">Local LLMs (Ollama/LM Studio)</text>
  
  <rect x="485" y="148" width="160" height="32" rx="6" fill="currentColor" fill-opacity="0.1" stroke="currentColor"/>
  <text x="565" y="169" fill="currentColor" font-size="11" text-anchor="middle">Image / Audio Models</text>
</svg>
