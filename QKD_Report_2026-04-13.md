# 🔐 arXiv 每周追踪：量子密钥分发 (QKD)

> **生成日期:** 2026-04-13 | **本周更新:** 4 篇

---

### 1. QuIKS: Near-Zero Latency Key Supply with Adaptive Buffering for Resource-Efficient Quantum Key Distribution Networks

- **👨‍🔬 作者:** Yuxin Chen, Zite Xia, Jian Li, Kaiping Xue, Zhonghui Li, Lutong Chen, Ruidong Li
- **📅 时间:** 2026-04-10 09:22:51 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2604.09144v1) | [PDF直达](https://arxiv.org/pdf/2604.09144v1)

**【中文摘要】**：
量子密钥分发（QKD）网络为远距离通信方提供信息论安全的密钥，正成为受量子计算威胁的经典密码基础设施的重要替代方案。在QKD网络中，密钥供给服务的即时性对应用的安全与性能至关重要，因为数据必须在传输前完成加密。虽然密钥缓冲能够实现即时密钥供给服务，但现有方案依赖于启发式方法，导致密钥资源消耗过高，从而严重阻碍了实际部署。为解决此问题，我们提出了QuIKS，一种基于自适应缓冲的即时密钥供给方案，其核心优势在于提供近乎零延迟的密钥供给，同时消耗极低的密钥资源（即极小的缓冲区容量）。具体而言，该方案建立在一个新颖的分析模型之上，该模型确定了保障近乎零延迟密钥供给性能所需的最小缓冲区容量。在此模型指导下，QuIKS引入了一种轻量级的两阶段控制算法，通过探测实时的应用模式和网络状况，动态决定密钥中继请求并调整缓冲区容量。在真实QKD网络测试平台上的实验表明，与现有先进方案相比，QuIKS在实现近乎零密钥供给延迟的同时，将密钥缓冲区容量降低了10倍以上。

**【核心创新点】**：
提出了一种基于自适应缓冲的即时密钥供给方案QuIKS，通过建立分析模型与动态控制算法，在保证近乎零延迟密钥供给的同时，实现了比现有方案低一个数量级的密钥缓冲区资源消耗。

---

### 2. Telecom C-band single-photon sources with a semiconductor-dielectric microresonator

- **👨‍🔬 作者:** Yuriy Serov, Aidar Galimov, Sergey Sorokin, Nikolai Maleev, Marina Kulagina, Yuriy Zadiranov, Grigorii Klimko, Maxim Rakhlin, Alexey Veretennikov, Gleb Veyshtort, Olga Lakuntsova, Yuliya Salii, Daria Berezina, Sergey Troshkov, Demid Kirilenko, Alexey Blokhin, Alexei Vasil'ev, Alexander Kuzmenkov, Mikhail Bobrov, Irina Sedova, Tatiana V. Shubina, Alexey A. Toropov
- **📅 时间:** 2026-04-08 09:31:15 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2604.06869v1) | [PDF直达](https://arxiv.org/pdf/2604.06869v1)

**【中文摘要】**：
基于光纤链路的量子密钥分发是实现安全通信的少数公认的量子物理应用之一，其工作于单量子层面——即单个C波段光子。目前，广泛使用的此类光子源是高度衰减的激光脉冲，其特点是单光子出现的概率较低。本文提出了一种高效的光子源，该源采用在微柱形微腔内的变质缓冲层上生长的InAs/GaAs量子点。其关键创新在于使用不同的半导体和介电材料来构成底部（GaAs/AlGaAs）和顶部（Si/SiO$_2$）布拉格反射镜。通过在分子束外延生长的相干异质结构制成的未完成微柱上沉积少量Si/SiO$_2$对，实现了这些材料在单片集成光源中的兼容性。该设计支持使用$π$脉冲进行共振激发，并能产生偏振光子，其端到端效率达到了破纪录的11%。

**【核心创新点】**：
**通过创新性地结合GaAs/AlGaAs与Si/SiO$_2$材料构建单片集成微柱微腔量子点光源，实现了11%的破纪录端到端效率，为高效量子密钥分发提供了关键器件。**

---

### 3. Towards National Quantum Communication in Europe: Planning and Sizing Terrestrial QKD Networks

- **👨‍🔬 作者:** Sebastian Raubitzek, Werner Strasser, Sebastian Ramacher, Thomas Lebeth, Andreas Neuhold, Christoph Pacher
- **📅 时间:** 2026-04-08 07:28:38 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2604.06764v1) | [PDF直达](https://arxiv.org/pdf/2604.06764v1)

**【中文摘要】**：
欧盟正在开发欧洲量子通信基础设施（EuroQCI），旨在构建一个泛欧网络，为各成员国（包括政府和关键基础设施领域）提供安全通信能力。尽管战略目标已在欧盟层面确定，但各国所需的量子密钥分发（QKD）网络的规模和结构在很大程度上仍未明确。本研究致力于解决如何规划和确定国家级地面QKD网络的规模，以支持关键基础设施和公共机构。我们提出了一种可复现的规划方法，该方法基于少量明确的假设，估算网络规模、总光纤长度以及所需QKD组件的数量。该方法以奥地利为例进行了演示，通过构建一个合成的结构化网络模型，并利用蒙特卡洛模拟进行评估。该模型聚焦于地面QKD基础设施，明确排除了天基部分。它在实际运行约束下，估算了端点数量、可信中继节点需求以及跳数长度分布。随后，以奥地利案例为基准，结合人口和地理范围，推导出适用于其他欧盟成员国的规模缩放规则。研究结果为整个欧洲各国的QKD骨干网规模提供了初步的规划估算。这些估算并非部署设计，而是作为规划层面的参考，以支持在EuroQCI框架下的早期成本评估和基础设施规模确定。

**【核心创新点】**：
**本研究提出了一种基于明确假设和蒙特卡洛模拟的可复现规划方法，首次为欧盟各国国家级地面QKD骨干网的规模估算提供了基准和可扩展的规划参考。**

---

### 4. PQC-Enhanced QKD Networks: A Layered Approach

- **👨‍🔬 作者:** Paul Spooren, Andreas Neuhold, Sebastian Ramacher, Thomas Hühn
- **📅 时间:** 2026-04-07 08:48:05 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2604.05599v1) | [PDF直达](https://arxiv.org/pdf/2604.05599v1)

**【中文摘要】**：
我们提出了一种分层、模块化的网络架构，该架构结合了量子密钥分发（QKD）和后量子密码学（PQC），旨在为长距离、多跳、可信节点的量子网络提供可扩展的端到端安全。为确保互操作性和高效的实际部署，物理安全节点之间的逐跳隧道通过WireGuard进行保护，其定期轮换的预共享密钥经由ETSI GS QKD 014接口提供。在此基础上，Rosenpass执行PQC密钥交换以建立端到端数据通道，而无需修改已部署的QKD设备或网络协议。这种双层架构在实际假设下实现了后量子前向安全性和认证性。我们使用开源组件实现了该设计，并在模拟和实验室测试平台上进行了验证与评估。实验表明，该架构可在多跳路径上不间断运行，具有低资源占用和故障安全机制。我们进一步讨论了该设计的组合安全性，即每个独立组件的安全性在其组合下得以保持，并概述了运营商在现有基础设施中集成QKD感知覆盖网络的迁移路径。

**【核心创新点】**：
**该研究通过结合量子密钥分发（QKD）与后量子密码学（PQC）的双层架构，在不改动现有QKD设备与协议的前提下，为多跳可信节点量子网络实现了兼具后量子前向安全性与认证性的可扩展端到端安全解决方案。**

---

