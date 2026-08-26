---
title: "DataVault: Multi-Modal ML System to Enhance Brassica napus Fatty Acid and Lipid Metabolism for Optimized Biofuel/Biodiesel Production"
summary: "A compartment-aware VAE + constraint-based metabolic modeling (COBRA) framework that integrates multi-scale biological data (genomics, transcriptomics, metabolic flux) to predict fatty acid engineering targets in *Arabidopsis thaliana*, with transferability to *Brassica napus* for biofuel/biodiesel oil optimization."
website_url: ""
github_url: ""
docs_url: ""
is_active: false
---
# Multi-Modal ML System to Enhance *Brassica napus* Fatty Acid and Lipid Metabolism for Optimized Biofuel/Biodiesel Production (DataVault)

## Description
Developed at Brookhaven National Laboratory for DataVault Holdings through a **Strategic Partnership Project**.

The framework addresses the challenge that cellular metabolism spans multiple scales (gene regulation, enzyme kinetics, pathway flux) while experimental data typically captures only one scale at a time. It combines a compartment-aware variational autoencoder (VAE) for representation learning with [COBRApy](https://opencobra.github.io/cobrapy/)-based constraint modeling, integrating multi-modal biological data during the learning process rather than through post-hoc reconciliation. The pipeline supports ortholog and homolog detection (BLAST, HMMER) and phylogenetic analysis across plant proteomes, transcriptomics integration with subcellular-compartment-aware modeling, and COBRA-based perturbation analysis to prioritize and rank single- and multi-gene metabolic engineering targets, including detection of synergistic gene combinations. Built on *Arabidopsis thaliana* as a model system, the framework is designed for transferability to *Brassica napus* and, more broadly, for generalization beyond fatty acid metabolism to other metabolic engineering questions where multi-scale data integration is needed.

## References
- [DataVault AI Website](https://dvlt.ai)

## Talks
- Bradley, N. (2024, September). *Agriculture Digital Twin Production of Renewable BioEnergy Crops*. Presented at New York Scientific Data Summit 2024: Addressing Data Challenges in Digital Twins (NYSDS 2024), New York, NY, USA. [Materials](https://indico.bnl.gov/event/23999/?view=standard#42-data-vault-holdings)
