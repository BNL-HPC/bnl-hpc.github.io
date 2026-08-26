---
title: "Quantum Imaging"
summary: "Building on the first demonstration of X-ray quantum correlation imaging via spontaneous parametric down-conversion (SPDC/XPDC) at the CHX beamline (NSLS-II), this project develops the computational infrastructure to turn that technique into a practical imaging tool - covering both image reconstruction (inverse problems) and the underlying photon-pair data processing pipeline."
website_url: ""
github_url: ""
docs_url: ""
is_active: true
---
# Quantum Imaging

## Description
This project develops the computational methods needed to move X-ray quantum correlation imaging - first demonstrated at NSLS-II's CHX beamline using spontaneous parametric down-conversion (SPDC/XPDC) to image test objects including an E. cardamomum seed - from a proof-of-concept technique toward a practical, scalable imaging tool. Two active threads make up the current work, both grounded in the data and detector methodology from that demonstration:
1. **Inverse problems for bucket-detector reconstruction:** Image reconstruction from the coincidence-imaging data using representations of both reduced 1D or full 2D data from the bucket detector, and evaluating regularization schemes for the inverse reconstruction problem - including total-variation (TV) denoising and DruNet-based priors.
2. **XPDC data analysis:** this thread focuses on scaling and speeding up the photon-pair identification pipeline underlying the SPDC/XPDC technique - the same time-of-arrival (ToA), time-over-threshold (ToT), and energy/momentum-conservation-based coincidence filtering described in the published methodology. Work includes evaluating Dask to remove processing bottlenecks and AwkwardArray for managing the data's irregular/jagged structure, and exploring metric-based pair-finding methods as an alternative or complement to the current cut-based filtering.

## Publications
- Goodrich, J. C., Mahon, R., Hanrahan, J., Bollweg, D., Dziubelski, M., Abrahao, R. A., Karmakar, S., Gofron, K. J., Caswell, T. A., Allan, D., Berman, L., Nomerotski, A., Fluerasu, A., DaVià, C., & McSweeney, S. (2025). *Quantum imaging with X-rays*. Optica Open. [https://doi.org/10.1364/opticaopen.30223492](https://doi.org/10.1364/opticaopen.30223492)
- Goodrich, J. C., Mahon, R., Hanrahan, J., Bollweg, D., Dziubelski, M., Abrahao, R. A., Karmakar, S., Gofron, K. J., Caswell, T. A., Allan, D., Berman, L., Nomerotski, A., Fluerasu, A., DaVià, C., & McSweeney, S. (2026). *Quantum correlation imaging via X-ray parametric down-conversion*. *Optica*, *13*(1), 135–142. [https://doi.org/10.1364/OPTICA.574747](https://doi.org/10.1364/OPTICA.574747)

## Artifacts
- [Timepix3 SPDC](https://github.com/JGoodrichBNL/tpxspdc) - Data analysis pipeline for Timepix3 detectors and X-ray parametric down-conversion coincidence filtering. (**work in progress**, *private repo*)
- [GIRecon](https://github.com/kchopra04/GIRecon) - Ghost imaging reconstruction framework using ADMM and DruNet models for inverse problems. (**work in progress**, *private repo*)
