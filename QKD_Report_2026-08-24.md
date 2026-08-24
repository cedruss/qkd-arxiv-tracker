# 🔐 arXiv 每周追踪：量子密钥分发 (QKD)

> **生成日期:** 2026-08-24 | **本周更新:** 4 篇

---

### 1. Squeezed- and coherent-state quantum key distribution over a deployed hybrid fibre-free-space channel

- **👨‍🔬 作者:** Dnan A. E. Hajomer, Huy Q. Nguyen, Ivan Derkach, Andreas B. Kidmose, Edoardo Rossi, Mattia Sabatini, Yoann Pietri, Marco Avesani, Francesco Vedovato, Michael Hentschel, Radim Filip, Giuseppe Vallone, Vladyslav Usenko, Tobias Gehring, Soren Forchhammer, Paolo Villoresi, Ulrik L. Andersen
- **📅 时间:** 2026-08-20 14:21:14 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2608.20088v1) | [PDF直达](https://arxiv.org/pdf/2608.20088v1)

**【中文摘要】**：  
量子网络将结合光纤与自由空间链路，然而连续变量量子密钥分发（CV-QKD）主要针对单一介质开发，跨光纤-自由空间级联信道的运行仍 largely 未被探索。这两种介质对系统提出截然不同的要求：光纤传输稳定且允许较长的处理间隔，而大气传播引入透射率波动，会降低安全性，且必须在短时间内予以解决。本文展示了一种采用本地本振光的CV-QKD方案，支持高斯调制相干态和压缩态，在包含620米自由空间链路和2公里已部署光纤的混合信道上运行，总损耗高达20 dB。我们并非针对每种介质调整光学系统，而是将信道适配移至后处理阶段，通过一个统一的自适应后处理框架实现，该框架结合了基于透射率的聚类、通过协方差矩阵平均或去衰落进行残余衰落抑制，以及速率自适应的盲逆向协商，仅此一项即可额外恢复高达19%的密钥。相同的自适应处理原则被应用于两种协议，同时考虑其不同的安全性分析和统计要求，在相应信道条件下，相干态协议和压缩态协议的渐近密钥率分别为0.42 Mbit/s和0.93 Mbit/s，并首次在已部署大气信道上实现了压缩态CV-QKD。这些结果表明，对传输介质的适配可在很大程度上转移到数据处理层，为构建涵盖光纤、地面自由空间和卫星链路的异构量子网络提供了可行路径。

**【核心创新点】**：  
本文提出将信道适配从光学层转移到统一的自适应后处理框架，首次在已部署的混合光纤-自由空间信道上实现了压缩态CV-QKD，并显著提升了密钥率。

---

### 2. Multiplexing of Continuous-Variable and Discrete-Variable Quantum Key Distribution Systems over Fibered and Free-Space Channels

- **👨‍🔬 作者:** Mattia Sabatini, Edoardo Rossi, Matías R. Bolaños, Francesco Vedovato, Thomas Liege, Eleni Diamanti, Giuseppe Vallone, Paolo Villoresi, Yoann Piétri, Marco Avesani
- **📅 时间:** 2026-08-20 07:43:56 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2608.19745v1) | [PDF直达](https://arxiv.org/pdf/2608.19745v1)

**【中文摘要】**：  
未来的量子通信基础设施将需要在共享物理信道上服务异构用户：短距离、高吞吐量链路倾向于采用连续变量量子密钥分发（CV-QKD），而长距离、高损耗链路仍是离散变量QKD（DV-QKD）的应用领域。将两种协议通过波分复用（WDM）在同一信道上共存，可同时满足两种场景需求，但二者对噪声的敏感性差异显著，使得共存并非易事，且迄今尚无实验验证。本文首次报道了两个独立的CV-QKD与DV-QKD系统在共用光信道上的同时运行，采用标准C波段DWDM滤波器，工作波长为1550.12 nm（CV）和1545.32 nm（DV）。我们在光纤链路以及620米城市白天自由空间链路上均实现了联合运行。在光纤上，两系统表现出预期的互补特性，在7.56 dB信道损耗处交叉，二者均达到约1.43 Mbit/s的密钥率；在白天自由空间条件下，二者在时变大气衰减中均维持Mbit/s级密钥率。在所有配置中，我们未观察到由复用引起的QBER或额外噪声的可测量劣化。这些结果表明，混合CV-DV WDM可作为异构量子通信网络的实用构建模块，使城域高吞吐量用户与长距离骨干链路可在单一物理基础设施上同时获得服务。

**【核心创新点】**：  
首次实验验证了CV-QKD与DV-QKD在同一光信道上通过WDM实现无性能劣化的同时运行，确立了混合CV-DV WDM作为异构量子网络实用构建模块的可行性。

---

### 3. Secure Medical Data Transmission Using Quantum Key Distribution and Post-Quantum Cryptography in Real-World Fiber Networks

- **👨‍🔬 作者:** Vasile-Laurentiu Dosan, Paul Spooren, Sebastian Moeckel, Alessandro Zannotti, Alek Lagarrigue, Pablo Vazquez, Marc Bodenstein, Jonas Jelonek, Jansen Dwan, Fabian Steinlechner, Kevin Füchsel, Thomas Hühn, Oliver de Vries
- **📅 时间:** 2026-08-19 12:46:33 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2608.18869v1) | [PDF直达](https://arxiv.org/pdf/2608.18869v1)

**【中文摘要】**：  
量子计算机对经典公钥密码学构成的威胁，推动了在医疗、金融和能源等关键基础设施中部署量子安全通信的需求。量子密钥分发（QKD）和后量子密码学（PQC）提供了互补的安全保障——前者实现信息论安全的密钥交换，后者提供抗量子攻击的端到端认证，二者可结合为分层架构。本文展示了一个实地部署的量子安全网络，该网络在德国图林根州140公里已铺设光纤上集成了基于纠缠的QKD与端到端PQC，通过包含异构地下与架空光纤链路的可信中继架构，将乡村健康服务站连接至大学医院。与依赖专用密钥管理系统向应用转发密钥的传统部署不同，我们的架构将QKD密钥直接注入相邻节点间基于标准Linux的VPN隧道中，同时由PQC保障端到端通信安全，与现有基础设施和软件完全兼容。偏振纠缠光子对在810 nm和1550 nm波长处产生，其中电信波段光子经已部署光纤传输。主动偏振稳定与色散补偿维持了纠缠质量，实现了22天连续、全自主运行，进一步彰显了基于纠缠的QKD方法在真实光纤环境中的技术成熟度。尽管两条部署链路分别在非重叠时段运行，但以架空光纤为主的链路表现出明显更高的不稳定性，其量子比特误码率（QBER）变化与风速相关性最强。所生成的密钥在不修改现有医疗系统的前提下保障了一个远程医疗概念验证应用，展示了量子安全关键基础设施的实用框架。

**【核心创新点】**：  
提出并实地验证了一种将纠缠QKD密钥直接注入标准Linux VPN隧道、并以PQC实现端到端安全的分层量子安全网络架构，在140公里已部署光纤上实现22天全自主稳定运行，且无需改动现有医疗应用系统。

---

### 4. Software Defined Networks Key Relay for Large-Scale Quantum Key Distribution Networks

- **👨‍🔬 作者:** Stephan Laschet, Gergely Lendvay, Thomas Lorünser, Paul James, Luca Torresetti, Alessandro Colombo
- **📅 时间:** 2026-08-18 09:01:32 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2608.17539v1) | [PDF直达](https://arxiv.org/pdf/2608.17539v1)

**【中文摘要】**：  
本研究探讨了利用软件定义网络（SDN）对大规模量子密钥分发网络（QKDN）进行编排管理的问题。基于ETSI和ITU规范，概述了通用最佳实践与架构。SDN控制器的主要任务是聚合网络中的关键技术性能指标（KPI），并据此选择最优路径。本文提出了多种基于Dijkstra或最大-最小容量算法并内置负载均衡的路径选择算法，并通过仿真测试评估了其性能与权衡。此外，还讨论了与SDN控制的QKDN相关的其他关键问题，如查询批处理、多路径选择及组密钥能力。针对多域场景下的中继路径选择，提出了一种 oblivious 多方协议，使各提供商无需披露其QKDN的敏感信息即可完成路径协商。这些贡献旨在增强量子安全网络基础设施的可扩展性、韧性与互操作性。

**【核心创新点】**：  
提出了一种基于SDN的QKDN编排框架，并引入不泄露隐私的多方中继路径选择协议，在提升网络可扩展性与负载均衡的同时，保障多域间的敏感信息隐私。

---

