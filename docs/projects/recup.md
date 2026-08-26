---
title: "RECUP: Scalable Metadata and Provenance for Reproducible Hybrid Workflows"
summary: "RECUP develops scalable metadata and provenance methods for reproducible hybrid HPC workflows. It captures and aligns workflow, I/O, performance, environment, and scientific metadata so researchers can rerun and reuse workflows, compare executions, diagnose variability, and assess both performance and result reproducibility."
website_url: ""
github_url: "https://github.com/RECUP-DOE"
docs_url: ""
is_active: true
---
# Scalable Metadata and Provenance for Reproducible Hybrid Workflows (RECUP)

## Description
RECUP is a U.S. Department of Energy-funded research project developing methods and software to improve the reproducibility of scientific results and performance for hybrid workflows on high-performance computing (HPC) systems. These workflows combine numerical simulation, data-intensive analysis, machine learning, and other coupled components while executing across heterogeneous CPUs, GPUs, storage systems, software environments, and workflow runtimes.

Reproducing such executions requires more than preserving source code and input data. Researchers must also capture workflow structure and task dependencies, software and system configurations, data movement and file I/O, performance measurements, intermediate and final results, and the provenance relationships among these records. RECUP addresses this challenge by managing metadata across the workflow lifecycle and applying FAIR principles to make the resulting information findable, accessible, interoperable, and reusable.

The project develops a composable framework for collecting, curating, aligning, storing, and analyzing metadata from multiple sources. RECUP integrates workflow-level information from systems such as RADICAL-Cybertools and Dask with I/O characterization from Darshan, performance and anomaly information from tools such as Chimbuko, and scalable data services from the Mochi ecosystem. The resulting metadata supports workflow reruns and reuse, comparison of execution patterns, identification of performance deviations, and quantitative analysis of variability in performance and scientific results.

RECUP also develops representative workflow mini-applications and test environments that reproduce the computational, communication, data-movement, and I/O behavior of complex AI-coupled scientific workflows. One such mini-application models an asynchronous, multi-phase loop of simulation, machine-learning training, selection, and agent tasks. RADICAL runtime system coordinates changing CPU and GPU task mixes, while configurable kernels emulate matrix operations, accelerator data transfers, preprocessing, and file I/O. These controlled workloads enable systematic experiments on metadata capture, performance characterization, and run-to-run reproducibility at leadership-computing scale.

BNL contributes workflow technologies, mini-applications, instrumentation, and analysis methods that connect execution-level observations to workflow-level provenance. This work helps researchers determine not only whether two executions produced comparable results, but also where and why their behavior diverged. RECUP's broader objective is an interoperable metadata foundation for repeatable experiments, reusable workflows, and end-to-end performance and result reproducibility studies on heterogeneous HPC platforms.

## References
- [Project GitHub](https://github.com/RECUP-DOE)
- [RADICAL-Cybertools Website](https://radical-cybertools.github.io)

## Publications
- Nicolae, B., Islam, T. Z., Ross, R., Van Dam, H., Assogba, K., Shpilker, P., Titov, M., Turilli, M., Wang, T., Kilic, O. O., Jha, S., & Pouchard, L. C. (2023). *Building the I (Interoperability) of FAIR for Performance Reproducibility of Large-Scale Composable Workflows in RECUP*. In 2023 IEEE 19th International Conference on e-Science (e-Science) (pp. 1-7). IEEE. [https://doi.org/10.1109/e-Science58273.2023.10254808](https://doi.org/10.1109/e-Science58273.2023.10254808)
- Kilic, O. O., Wang, T., Turilli, M., Titov, M., Merzky, A., Pouchard, L. C., & Jha, S. (2024). *Workflow mini-apps: Portable, scalable, tunable & faithful representations of scientific workflows*. In 2024 IEEE 24th International Symposium on Cluster, Cloud and Internet Computing (CCGrid) (pp. 465–477). IEEE. [https://doi.org/10.1109/CCGrid59990.2024.00059](https://doi.org/10.1109/CCGrid59990.2024.00059)

## Talks and Tutorials
- Kilic, O. O., Wang, T., Turilli, M., Titov, M., Merzky, A., Pouchard, L. C., & Jha, S. (2025). *Workflow Mini-Apps: Evaluating Performance Reproducibility in Scientific Workflows*. ACM Conference on Reproducibility and Replicability ([ACM REP 2025](https://acm-rep.github.io/2025/)). [https://github.com/radical-cybertools/tutorials/wiki/ACM-REP-Tutorials-2025](https://github.com/radical-cybertools/tutorials/wiki/ACM-REP-Tutorials-2025)
- Kilic, O. O., & Wang, T. (2026). *Classification and Modeling the Performance and Scaling of Scientific Workflows with Resource-efficient Workflow Mini-apps*. In 28th Conference on Computing in High Energy and Nuclear Physics (CHEP 2026). [https://indico.cern.ch/event/1471803/contributions/6966773/](https://indico.cern.ch/event/1471803/contributions/6966773/)

## Artifacts
- [Workflow Mini-apps](https://github.com/RECUP-DOE/workflow-miniapps) - Tutorials and representative workloads for reproducibility and workflow-performance studies.
- [RECUP Software Development Kit](https://github.com/RECUP-DOE/SDK) - Integration, deployment, and testing recipes for RECUP tools.
- [RADICAL-EnTK Provenance](https://github.com/RECUP-DOE/radical.entk.provenance) - Workflow provenance experiments and analysis for RADICAL-EnTK executions.
