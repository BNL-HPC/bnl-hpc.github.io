---
title: "xGFabric: Coupling Sensor Networks and HPC Facilities with Advanced Wireless Networks for Near-Real-Time Simulation of Digital Agriculture"
summary: "A DOE ASCR project developing an end-to-end, adaptive platform that couples sensors, edge devices, programmable 5G/6G networks, and high-performance computing resources for near-real-time scientific workflows and AI-enabled decision support."
website_url: "https://sites.google.com/view/xgfabric"
github_url: "https://github.com/radical-collaboration/xGFabric"
docs_url: ""
is_active: true
---
# Coupling Sensor Networks and HPC Facilities with Advanced Wireless Networks for Near-Real-Time Simulation of Digital Agriculture (xGFabric)

## Description
xGFabric is a U.S. Department of Energy Office of Advanced Scientific Computing Research project that designs and evaluates an end-to-end, multiscale, and adaptive distributed system connecting scientific instruments, sensors, and actuators with high-performance computing (HPC) facilities. The project uses programmable 5G/6G networking to coordinate computing, storage, sensing, data movement, and actuation across the edge-to-HPC continuum.

The xGFabric software stack combines resilient event-driven communication, distributed dataflow programming, and adaptive workflow and resource management. CSPOT provides log-based communication and persistence across embedded devices and computing systems; Laminar expresses distributed dataflow programs; RADICAL-Pilot manages dynamically acquired HPC resources; and xGFabric controllers coordinate data staging, task execution, and resource allocation. SensorSlicer extends 5G/6G network slicing toward workflow-aware sensor virtualization, adaptive sampling, and quality-of-service control.

Digital agriculture is the primary science driver. The project uses environmental telemetry associated with the Citrus Under Protective Screens (CUPS) facility at the Lindcove Research Extension Center in California. Sensor data is transported through a private 5G network and used to trigger OpenFOAM computational fluid dynamics simulations that model airflow inside the screenhouse. The team has demonstrated an end-to-end workflow connecting a 5G-enabled sensor device at the University of Nebraska-Lincoln with computing resources at the University of California, Santa Barbara and the University of Notre Dame.

Current research extends the demonstrated sensor-to-HPC workflow with an online/offline architecture for AI-assisted decision support. High-fidelity simulations and model training execute asynchronously on HPC resources, while compact surrogate models can be delivered to edge systems for low-latency inference. The project also investigates adaptive scheduling, network slicing, resilient data transport, and portable deployment at DOE computing facilities.

BNL contributes to adaptive workflow and resource management, end-to-end system integration, and portable execution across edge and HPC resources. The broader collaboration includes Brookhaven National Laboratory, Princeton Plasma Physics Laboratory, Rutgers University, the University of California, Santa Barbara, the University of Notre Dame, and the University of Nebraska-Lincoln.

## References
- [Official Website](https://sites.google.com/view/xgfabric)
- [GitHub Repository](https://github.com/radical-collaboration/xGFabric)
- [MAYHEM-Lab GitHub Organization](https://github.com/MAYHEM-Lab)
- [RADICAL-Cybertools Website](https://radical-cybertools.github.io)

## Publications
- Kurafeeva, L., Subedi, A., Hartung, R., Fay, M., Biswas, A., Jha, S., Kilic, O. O., Krintz, C., Merzky, A., Thain, D., Vuran, M. C., & Wolski, R. (2025). *xGFabric: Coupling sensor networks and HPC facilities with private 5G wireless networks for real-time digital agriculture*. In 7th Annual Workshop on Extreme-scale Experiment-in-the-Loop Computing (XLOOP '25). ACM. [https://doi.org/10.1145/3731599.3767589](https://doi.org/10.1145/3731599.3767589)

## Artifacts
- [xGFabric integration and demonstration software](https://github.com/radical-collaboration/xGFabric)
- [CSPOT event-driven distributed runtime](https://github.com/MAYHEM-Lab/cspot)
- [Laminar distributed dataflow programming system](https://github.com/MAYHEM-Lab/laminar)
