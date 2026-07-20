# 🔐 arXiv 每周追踪：量子密钥分发 (QKD)

> **生成日期:** 2026-07-20 | **本周更新:** 9 篇

---

### 1. Spectral Attack on Continuous-Variable Quantum Key Distribution Systems

- **👨‍🔬 作者:** Chen Gong, Mingxuan Guo, Peng Huang, Tao Wang, Guihua Zeng
- **📅 时间:** 2026-07-17 06:23:38 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.15668v1) | [PDF直达](https://arxiv.org/pdf/2607.15668v1)

**【中文摘要】**：
连续变量量子密钥分发（CVQKD）因其兼容性强和成本低廉而受到广泛关注。然而，发射端与接收端之间存在不同程度的带宽失配问题。这可能导致携带调制信息的频率分量无法被合法方完全感知。本文识别出一种由带宽失配引起的实际安全性漏洞，并提出了一种相应的光谱攻击方案。与以往利用安全性漏洞来隐藏截获-重发攻击所引入的额外噪声的方法不同，该方案能够在不引入额外干扰的情况下直接获取原始密钥信息。我们构建了一个针对带有滤波操作的CVQKD系统的原理验证攻击，以验证其可行性。实验结果表明，如果忽略这一实际安全性漏洞，窃听者Eve能够获取足够的信息，使系统变得不安全。基于所识别的安全性漏洞，本文还提出了相应的防御策略。这项工作有助于弥合理论模型与实际实现之间的差距，为实际量子通信系统中的防御设计提供参考。

**【核心创新点】**：
**本文首次识别并实验验证了由带宽失配引起的CVQKD系统安全性漏洞，并提出了一种无需引入额外噪声即可直接窃取原始密钥信息的光谱攻击方案。**

---

### 2. High-rate continuous-variable quantum key distribution coexisting with Tb/s coherent classical transmission in hollow-core fiber

- **👨‍🔬 作者:** Xitao Ji, Siyu Chen, Peng Li, Mingming Zhang, Yilun Chen, Jun Gao, Rui Lin, Bacco Davide, Siqi Yan, Ming Tang
- **📅 时间:** 2026-07-16 08:04:38 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.14704v1) | [PDF直达](https://arxiv.org/pdf/2607.14704v1)

**【中文摘要】**：  
量子密钥分发（QKD）能够提供安全性根植于量子力学的密钥，但在传统实芯光纤中，弱量子态对额外噪声预算的限制使得其与高容量经典通信的共存仍面临挑战。本文结合超低损耗反谐振空芯光纤与残余载波辅助的离散调制连续变量QKD（DM-CV-QKD），以同时解决传播诱导的共存噪声和低信噪比下的相位恢复问题。在一条24.3公里长、端到端损耗为3.3 dB的空芯链路上，一个双偏振15 Gbaud的DM-CV-QKD信道实现了153.22 Mb/s的平均渐近密钥率（SKR）和149.99 Mb/s的有限码长SKR，同时39个相干波分复用信道提供了7.6 Tb/s的总数据速率和7.2 Tb/s的净数据速率。该系统甚至能在高达15 dBm的经典发射功率下，无需光学带通滤波器（BPF）即可维持正SKR。针对集体攻击的有限码长分析进一步表明，在等效100公里条件下仍可预测出正的密钥率。这些结果表明，反谐振空芯光纤结合载波辅助相位恢复，能够显著扩展共享光纤量子安全相干链路的工作范围，为将高速CV-QKD与高容量光网络集成提供了一条有前景的路径。

**【核心创新点】**：  
**通过将超低损耗反谐振空芯光纤与残余载波辅助的离散调制连续变量QKD相结合，在无需光学带通滤波器的条件下实现了与7.6 Tb/s经典通信共存的153 Mb/s级密钥率，并证明在等效100公里条件下仍可维持正密钥率。**

---

### 3. Effects of coherent and incoherent measurement imperfections on multipartite quantum nonlocality and quantum key distribution

- **👨‍🔬 作者:** Qiong Wang, Wen-Long Qiao, Qing Chen, Liu-Jun Wang
- **📅 时间:** 2026-07-15 09:43:34 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.13645v1) | [PDF直达](https://arxiv.org/pdf/2607.13645v1)

**【中文摘要】**：  
多体贝尔非局域性是设备无关量子信息协议的核心资源，但其实际认证不可避免地受到非完美测量的影响。我们分析了相干角度失准与非相干结果翻转如何影响基于Mermin、Svetlichny及MABK不等式的$n$体GHZ态的贝尔值衰减与非局域性阈值。相干失准产生周期性的角度违规窗口，其单个窗口宽度随参与方数量增加而收缩。相反，非相干结果翻转产生单一临界结果翻转概率：对于MABK不等式和奇数$n$的Mermin不等式，该概率随$n$增大而增大；而对于Svetlichny不等式，该概率随$n$增大而减小。将退化的贝尔值与凸组合攻击模型下的渐近Devetak–Winter密钥率界相联系表明，密钥生成对测量非完美性施加了比非局域性认证更严格的约束。这些结果为在测量非完美条件下实现鲁棒的多体非局域性认证和密钥率估计提供了定量基准。

**【核心创新点】**：  
**通过分析相干角度失准与非相干结果翻转对多体GHZ态贝尔值的影响，揭示了密钥生成对测量非完美性的容忍度远低于非局域性认证，并给出了随参与方数量变化的定量阈值。**

---

### 4. End-to-End Quantum Key Distribution Across Hybrid Fiber and Free-Space Links with All-Optical Encoding Conversion

- **👨‍🔬 作者:** Khen Cohen, Tomer Nahum, Michael Tzukran, Paz Or, Yehuda Pilnyak, Nitzan Livneh, Hagai Eisenberg, Yaron Oz, Haim Suchowski
- **📅 时间:** 2026-07-14 14:53:53 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.12837v1) | [PDF直达](https://arxiv.org/pdf/2607.12837v1)

**【中文摘要】**：  
量子密钥分发（QKD）承诺提供信息论意义上安全的通信，但未来的网络必须桥接光纤和自由空间链路，这两种链路天然采用不同的光子编码方式，即光纤中的时间-比特编码和自由空间中的偏振编码。本文展示了一种完整的混合光纤与自由空间QKD链路，该链路在单一端到端协议内桥接两种介质，并完全在光学域完成两种编码之间的转换。我们采用工作在1550 nm的诱骗态BB84协议，在90米室外自由空间链路上实现了连续的安全密钥生成。该系统能够在折射率结构参数Cn²跨越两个数量级以上的大气条件下运行，从强日间湍流到平静的夜间条件，并进一步在750米自由空间扩展链路上验证了光子级操作。在整个过程中，链路保持会话平均量子比特误码率（QBER）为5.6%-6.8%，远低于BB84协议11%的安全阈值。编码转换完全在光学域内完成，无需测量或状态重构，从而保留了BB84协议的安全假设。因此，时间-比特到偏振（T2P）和偏振到时间-比特（P2T）转换器仍属于不可信的量子信道的一部分，而非可信中间节点。这些结果确立了安全的光子编码转换作为光纤与自由空间量子通信平台之间的实用接口，为未来量子网络应用提供了基础模块。

**【核心创新点】**：  
**本文首次在单一端到端协议中，通过完全光学域的编码转换（无需测量或状态重构），实现了光纤（时间-比特）与自由空间（偏振）混合QKD链路，并在强湍流等实际大气条件下验证了低于安全阈值的稳定密钥生成。**

---

### 5. A Scalable Cloud-Orchestrated and Service-Oriented Multi-Domain QKD Network with PQC Integration

- **👨‍🔬 作者:** Konstantinos Krilakis, Antonia Tsili, Aikaterini Mandilara, Dimitris Syvridis
- **📅 时间:** 2026-07-14 13:37:28 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.12765v1) | [PDF直达](https://arxiv.org/pdf/2607.12765v1)

**【中文摘要】**：  
量子密钥分发（QKD）可提供无条件安全性，但现有QKD网络因供应商特定接口、可信节点限制以及互操作性有限，难以在异构基础设施和管理域之间实现扩展。本文提出一种灵活的多域、多站点量子安全网络架构，集成了供应商无关的QKD、SDN编排和云管理信任服务。通信基于零信任网络访问协议，采用基于后量子密码（PQC）签名和密钥封装算法的多级认证机制。该系统部署于真实测试平台，包含来自3个供应商的QKD节点域以及无QKD基础设施元素的域。实验结果表明，即使在受限设备上，PQC和SDN开销也相对较低，主要瓶颈在于QKD密钥检索和供应商特定的密钥流限制。所提框架将量子安全密钥传输扩展至原生QKD边界之外，同时保持灵活性、互操作性以及与现有基础设施的兼容性。

**【核心创新点】**：  
**提出一种集成供应商无关QKD、SDN编排与零信任协议的多域量子安全网络架构，在真实异构测试平台上验证了其低开销与跨域兼容性，并突破了原生QKD的密钥传输边界。**

---

### 6. Deterministic Minimum-Leakage Continuous-Variable Quantum Key Distribution with Phase-Conjugated Twin Beams

- **👨‍🔬 作者:** Zhenlin Zhao, Dawei Wang
- **📅 时间:** 2026-07-14 07:03:32 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.12432v1) | [PDF直达](https://arxiv.org/pdf/2607.12432v1)

**【中文摘要】**：  
最小泄漏连续变量量子密钥分发通过在态制备阶段设计信号系综来抑制Eve的霍列沃信息。现有的对称最小泄漏协议通过“预示”方式实现：Alice干涉两个压缩系综，测量其中一个输出模式，并将另一个发送给Bob。本文提出一种确定性双模协议，去除了Alice侧的预示步骤。Alice将两个反向压缩的高斯系综在平衡分束器上合并，并传输两个输出模式，这些模式构成相位共轭孪生光束。我们证明该协议与预示协议通过一个共同的基于纠缠的源相关联，但对应不同的制备-测量分解。在极大压缩极限下，两种协议每个传输光学模式可获得相同的密钥率。然而，在有限压缩条件下，相位共轭孪生光束协议实现相同密钥率所需的压缩度比预示协议低约3 dB。我们进一步分析了关联双模高斯攻击，其中Eve注入具有优化模间关联的辅助模式。研究发现，关联攻击比独立攻击略有效，但在最小泄漏条件下其优势仍然有限。这些结果表明，相位共轭孪生光束为对称最小泄漏CV-QKD提供了一条确定性的、实验上更具吸引力的路径。

**【核心创新点】**：  
**提出一种无需预示步骤的确定性双模相位共轭孪生光束协议，在有限压缩条件下比传统预示协议节省约3 dB压缩度，且能有效抑制关联攻击下的信息泄漏。**

---

### 7. Noise Resilience of Quantum Key Distribution Protocols Secured Against Independent Attacks With One-Way Communication

- **👨‍🔬 作者:** Adam Bílek, Ryszard Kukulski, Paulina Lewandowska, Łukasz Pawela, Zbigniew Puchała
- **📅 时间:** 2026-07-13 17:42:52 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.11857v1) | [PDF直达](https://arxiv.org/pdf/2607.11857v1)

**【中文摘要】**：  
我们研究了单量子比特量子密钥分发（QKD）协议在独立窃听攻击和基于单向经典通信的密钥蒸馏场景下的抗噪声能力。为此，我们引入了一种基于噪声的度量标准，用于量化QKD协议的效率。在此框架下，我们分析了允许Alice和Bob渐进地建立安全密钥的最大噪声水平。基于这一假设，我们比较了通用单量子比特QKD协议（特别是BB84、B92、E91和六态协议）的噪声容忍度。我们的主要结果确定了允许蒸馏渐进安全密钥的QKD噪声水平阈值。此外，我们证明六态协议在抗噪声能力上优于其他被分析的单量子比特协议，同时具有更高的后选择效率，从而确认了其在所考虑的安全模型中的鲁棒性。最后，我们对所提出的基于噪声的度量标准与传统量子比特误码率（QBER）度量标准进行了分析。

**【核心创新点】**：  
**引入一种基于噪声的度量标准，首次确定了单量子比特QKD协议在独立窃听攻击下渐进安全密钥蒸馏的噪声水平阈值，并证明六态协议在抗噪声能力和后选择效率上均优于BB84、B92和E91协议。**

---

### 8. Deploying and validating a metropolitan QKD secure network: architecture and field performance

- **👨‍🔬 作者:** Claudia De Lazzari, Nicola Biagi, Damiano Giani, Marco Russo, Fernando Chirici, Francesco Stocco, Saverio Francesconi, Giacomo Ferranti, Alessandro Soureal, Antonella Sanguineti, Bartolomeo Montrucchio, Christian Laurenzi, Oliviero Testa, Guglielmo Morgari, Antonio Manzalini, Tommaso Occhipinti, Alessandro Zavatta, Davide Bacco
- **📅 时间:** 2026-07-13 15:51:26 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.11727v1) | [PDF直达](https://arxiv.org/pdf/2607.11727v1)

**【中文摘要】**：  
具有密码学相关能力的量子计算机的出现对经典公钥基础设施构成了根本性威胁。量子密钥分发（QKD）通过提供独立于任何计算复杂性假设的信息论安全性，解决了密钥建立过程中的这一挑战。本研究报告了在米兰数据中心之间部署并实验验证了一个城域规模的量子安全网络。该网络运行于现有光纤基础设施之上，采用分层架构，集成了QKD硬件、符合标准的密钥管理（KM）以及集中式软件定义网络（SDN）编排。通过主动光交换和可信节点路由实现的动态路径重配置，支持自动化故障切换方案。跨多种协议和工作负载的应用层验证确认了所有系统组件的无缝互操作性。这些结果证明了城域QKD网络在生产部署中的技术与运营就绪性，并为构建城域规模的量子安全通信基础设施提供了可复制的蓝图。

**【核心创新点】**：  
**通过集成QKD硬件、标准密钥管理与SDN编排的分层架构，在现有光纤网络上实现了城域量子安全网络的自动化运行与生产级验证。**

---

### 9. Deployment of Entanglement-Based QKD in Financial Infrastructure

- **👨‍🔬 作者:** Mirela Selimović, Roman Solar, Jonathan Gruner, Sebastian Mair, Mario Wenzl, Thomas Heine, Matej Pivoluska, Rupert Ursin, Sebastian Philipp Neumann
- **📅 时间:** 2026-07-13 08:34:58 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.11252v1) | [PDF直达](https://arxiv.org/pdf/2607.11252v1)

**【中文摘要】**：  
我们演示了基于纠缠的量子密钥分发（eQKD）在高安全性金融基础设施中的可行性，通过22公里光纤链路（两端数据中心间损耗为8 dB）并利用偏振纠缠实现。全自动化系统在四个月内以平均63.8 kb/s的速率持续生成安全密钥，这些密钥被存储于密钥管理系统中，并用于建立VPN隧道。该系统总运行时间达93.7%，且未因量子光学组件导致任何停机。主动偏振控制使得量子比特误码率在97.4%的时间内低于2%，而基于纠缠光子对固有时间关联的定时同步实现了亚300皮秒的精度。我们的独立系统既不需要偏振导引激光器，也不需要外部高精度时间参考。这些结果表明eQKD已能实际集成到运营中的金融基础设施中。

**【核心创新点】**：  
**首次在真实金融数据中心间22公里光纤链路上实现了全自动、长期稳定的纠缠量子密钥分发，无需外部偏振参考或高精度时钟，并成功集成到VPN密钥管理系统中。**

---

