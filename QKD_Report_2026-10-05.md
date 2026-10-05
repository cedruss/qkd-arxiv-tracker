# 🔐 arXiv 每周追踪：量子密钥分发 (QKD)

> **生成日期:** 2026-10-05 | **本周更新:** 12 篇

---

### 1. Quantum utility routing in continuous-variable QKD networks with trusted and untrusted relays

- **👨‍🔬 作者:** Farsad Ahmad, Aeysha Khalique
- **📅 时间:** 2026-10-02 14:35:42 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2610.03382v1) | [PDF直达](https://arxiv.org/pdf/2610.03382v1)

**【中文摘要】**：
连续变量量子密钥分发（CV-QKD）网络需要同时考虑密钥生成、中继信任和有限网络资源的路由策略。我们提出了量子效用路由（QUR），这是一种用于网络的加权路由框架，该网络将可信点对点链路与不可信CV贝尔测量中继相结合。过渡级可组合有限码长密钥率（SKR）被直接纳入路由搜索，使QUR能够在瓶颈SKR与路由几何结构和资源使用之间取得平衡。我们考虑了图优化QUR（QUR$_{\mathrm{go}}$）和使用机器学习以避免重复进行图特定权重优化的固定权重实现（QUR$_{\mathrm{fw}}$），并将两者与A*和最大—最小路由进行基准比较。在默认网络配置下，QUR$_{\mathrm{go}}$和QUR$_{\mathrm{fw}}$相对于A*提高了平均路径SKR，同时所需的网络资源显著少于最大—最小路由。该框架还通过利用不可信基础设施作为测量中继，在广泛的可信节点可用性范围内保持安全连接。这些结果表明，CV-QKD网络中的路由可以被视为密码性能与网络资源消耗之间的一种可配置权衡。

**【核心创新点】**：
**本文提出量子效用路由（QUR）框架，将有限码长密钥率直接纳入路由搜索，实现了CV-QKD网络中密码性能与资源消耗的可配置权衡，并在提高密钥率的同时显著降低资源占用。**

---

### 2. Quantum Key Distribution with Entanglement-Swapped Photons from a Quantum Emitter

- **👨‍🔬 作者:** Michele B. Rota, Francesco Basso Basset, Alessandro Laneve, Francesco Salusti, Nicolas Claro-Rodriguez, Giuseppe Ronco, Mattia Beccaceci, Tobias M. Krieger, Quirin Buchinger, Saimon F. Covre da Silva, Sandra Stroj, Mariia Gumberidze, Vladyslav Usenko, Sven Höfling, Tobias Huber-Loyola, Mario A. Usuga Castaneda, Armando Rastelli, Klaus D. Jöns, Rinaldo Trotta
- **📅 时间:** 2026-10-02 14:18:36 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2610.03351v1) | [PDF直达](https://arxiv.org/pdf/2610.03351v1)

**【中文摘要】**：
量子密钥分发（QKD）是量子网络的一项基本功能。扩展其传输距离需要量子中继器，而该技术仍处于研发阶段，尚未实现与量子密码协议的结合演示。在此，我们通过评估经由纠缠交换分布的相关光子能否支持密钥分发，来研究一种可行的量子中继器方案的基本操作。我们采用基于嵌入光子腔中的应变调谐GaAs量子点的先进确定性光子源，并在两个节点之间利用纠缠交换光子实现了与源无关的QKD协议。我们对系统进行了基准测试，并展示了高分辨率时间后选择如何实现安全密钥交换，同时预计通过现实的器件和协议优化还可进一步提升密钥率。由于该方案与多种量子存储平台兼容，我们的方法代表着向长距离量子安全通信迈出的重要一步。

**【核心创新点】**：
**本文首次利用基于应变调谐GaAs量子点的确定性光子源，通过纠缠交换在两端点间实现了与源无关的量子密钥分发，验证了纠缠交换光子支持安全密钥交换的可行性，为量子中继器与量子密码协议的结合迈出了关键一步。**

---

### 3. Learnt Attacks on Quantum Key Distribution under Channel Noise and Device Drift

- **👨‍🔬 作者:** Marcel Mordarski, Benjamin Gras, Abdelrahman Shehata, Daniel Budina, Roberto Bondesan
- **📅 时间:** 2026-10-01 14:36:30 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2610.01792v1) | [PDF直达](https://arxiv.org/pdf/2610.01792v1)

**【中文摘要】**：
量子密钥分发（QKD）链路的参数配置基于对平稳信道的安全性分析，而决定信道漂移的设备则在两次校准之间运行。对于无法改变信道自身噪声的窃听者而言，其能否通过跟随这种漂移而获利，尚未得到量化。本文将自适应窃听建模为一个受约束的马尔可夫决策过程：攻击者在每一轮中选择一个电路，噪声水平遵循Ornstein–Uhlenbeck过程，而中止条件是对每个轮次块的预算约束。自适应策略的价值由最佳固定电路和动态规划上界所界定。这些动作是学习得到的攻击。Decker等人针对固定信道在固定门模板上训练参数化电路，而本文则联合搜索门结构和旋转角度。这使得电路足够紧凑，从而能够构成离散动作集，并将该构造推广到缺乏已知模板的噪声模型，包括振幅阻尼信道。在双边退极化噪声下的设备无关E91协议中，一个强化学习攻击者将其Holevo信息量从最佳固定电路的$0.135$提升至零探测时的$0.348$，达到上界的$98\%$。在漂移比特翻转信道下的BB84协议中，她在保真度上超过保守的噪声索引规则$0.024$，达到上界的$99\%$。在平稳噪声下，攻击者从基不对称性中获得的增益在平均误差率约束与逐基误差率约束之间发生符号变化。该搜索从随机门序列出发，能够恢复解析克隆器和集体攻击密钥率，并从上方满足Winick–Lütkenhaus–Coles目标的下界。

**【核心创新点】**：
本文将自适应窃听形式化为受约束马尔可夫决策过程，通过联合搜索门结构与旋转角度学习紧凑攻击电路，在E91和BB84协议下分别达到理论上界的98%和99%，并推广至无已知模板的噪声模型。

---

### 4. Electromagnetic Side-Channel Vulnerability in QKD Equipment

- **👨‍🔬 作者:** Mikio Fujiwara, Katsumi Fujii, Fumie Ono, Masakazu Ono, Akihisa Tomita
- **📅 时间:** 2026-10-01 12:50:58 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2610.01609v1) | [PDF直达](https://arxiv.org/pdf/2610.01609v1)

**【中文摘要】**：
实际的量子密钥分发网络节点可能容易受到电磁泄漏等侧信道攻击。在本研究中，我们测量了一台原型量子密钥分发设备的电磁辐射，该设备实现了基于时间仓诱骗态的BB84协议，并使用Y基和Z基。我们在消声室内分别测量了距离发射端和接收端0米和3米处的电磁频谱和波形。结果表明，发射端是电磁泄漏的主要来源，并且在1241.6 MHz时钟的三次谐波处生成的量子态之间观察到了明显差异。

**【核心创新点】**：
实验揭示了基于时间仓诱骗态BB84协议的QKD原型设备中，发射端是电磁泄漏的主要来源，且其三次谐波处的电磁辐射可区分不同量子态，从而构成潜在的侧信道漏洞。

---

### 5. Inherent Turbulence Immunity of Vector Vortex Beams in Free Space Quantum Key Distribution

- **👨‍🔬 作者:** Behnam Talari, Rouhollah Karimzadeh
- **📅 时间:** 2026-10-01 11:57:08 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2610.01523v1) | [PDF直达](https://arxiv.org/pdf/2610.01523v1)

**【中文摘要】**：
轨道角动量（OAM）复用提供了一个无限维离散希尔伯特空间，非常适合用于高容量自由空间量子密钥分发（QKD）。然而，携带拓扑荷（$|\ell| \ge 1$）的纯标量空间模式在通过地面大气湍流传输时会发生严重退相干。湍流折射率涡旋会分裂高阶涡旋奇点，在相邻拓扑信道之间引起灾难性的模间串扰，并迅速将量子比特误码率（QBER）推高至远高于与个体克隆攻击相关的无条件11%安全阈值。在此，我们证明了一种被称为矢量涡旋光束（VVB）的混合偏振-OAM纠缠态，能够提供内在的、无需硬件的抗湍流扰动能力。由于地面空气的光学各向异性极小（$Δn < 10^{-9}$），折射率涨落会以相同的共模标量相位屏形式对称地耦合到正交圆偏振模式上，并在相对偏振-相位自由度中相互抵消。通过在湍流强度从$D/r_0 = 0$到$3.0$的范围内，利用改进的功率谱相位屏对模场进行数值传播，我们表明VVB编码协议将渐近QBER从42.0%抑制至4.8%，实现了约11.6倍的误差抑制因子，且无需主动自适应光学或变形镜。

**【核心创新点】**：
**本文提出并验证了基于混合偏振-OAM纠缠的矢量涡旋光束编码协议，利用大气极弱光学各向异性导致的共模相位抵消机制，在无需自适应光学硬件的条件下将湍流环境下的QBER从42.0%降至4.8%，实现了约11.6倍的误差抑制。**

---

### 6. Experimental quantification of quantum coherence for a set of quantum states

- **👨‍🔬 作者:** Tianle Zheng, Liangsheng Li, Wenting Zhou, Chengjie Zhang
- **📅 时间:** 2026-10-01 07:31:01 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2610.01227v1) | [PDF直达](https://arxiv.org/pdf/2610.01227v1)

**【中文摘要】**：
我们提出了一种以基无关的方式对一组量子态的量子相干性进行直接实验验证的方法。我们发现，一组量子态的量子相干性理论与我们的实验结果完美吻合，并可应用于BB84协议和量子安全直接通信等协议。利用萨格纳克干涉仪，我们实验量化了两组实验态的量子相干性。此外，我们引入了集合相干性的一种新应用，表明BB84协议中所使用的态展现出最大集合相干性。我们的结果为量子相干性在一组量子态中的更广泛应用铺平了道路，包括量子密钥分发协议和概率量子克隆。

**【核心创新点】**：
以基无关方式实验验证了一组量子态的量子相干性理论，并证明BB84协议所用态具有最大集合相干性。

---

### 7. Device-Independent Conference Keys from Parity-Extended Games

- **👨‍🔬 作者:** Suvradip Chakraborty, Ronak Ramachandran, Aniruddha Sen
- **📅 时间:** 2026-10-01 04:15:37 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2610.01025v1) | [PDF直达](https://arxiv.org/pdf/2610.01025v1)

**【中文摘要】**：
设备无关会议密钥协商（DI-CKA）使一组参与方能够从不信任的量子设备中建立共享密钥，其安全性由非局域性认证。现有的DI-CKA协议均围绕单一贝尔不等式构建，通常是CHSH博弈的多方变体。相比之下，DI-QKD协议建立在更为丰富的非局域博弈体系之上，而如何将这一体系推广到会议场景仍不明确。我们引入了$\textit{Parity-$G$博弈}$，它将任意双人博弈$G$扩展到$N$个参与方，对任意$N$均适用，前提是$G$存在一种最优策略，其中某一参与方测量Pauli可观测量。该扩展保持了$G$的量子值和经典值不变，且由此得到的$N$方协议的安全性仅需对双人博弈进行分析即可保证。我们的框架将Ribeiro、Murta和Wehner（Phys. Rev. A, 2018）提出的Parity-CHSH博弈作为特例纳入其中。将其应用于Mermin--Peres魔方博弈，可得到一种新的$N$方伪心灵感应博弈——$\textit{Parity魔方博弈}$，理想设备在每一轮中均能获胜。我们利用它构建了$\textit{首个}$基于伪心灵感应博弈的DI-CKA协议。我们证明了该协议在相干攻击下的安全性。该协议每轮可产生最多两个密钥比特，且在低噪声条件下其密钥率超过基于Parity-CHSH博弈的DI-CKA协议。

**【核心创新点】**：
提出了Parity-$G$博弈框架，将任意满足特定条件的双人非局域博弈扩展为多方博弈，并基于Mermin--Peres魔方博弈构建了首个基于伪心灵感应博弈的设备无关会议密钥协商协议，在低噪声下密钥率优于现有方案。

---

### 8. Quantum key distribution using generalized contextuality against post-quantum eavesdroppers

- **👨‍🔬 作者:** Daniel Centeno, Roberto D. Baldijão, Maria Ciudad Alañón, Yujie Zhang, Pedro Lauand, Elie Wolfe
- **📅 时间:** 2026-09-30 18:59:45 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2610.00595v1) | [PDF直达](https://arxiv.org/pdf/2610.00595v1)

**【中文摘要】**：
贝尔非局域性允许在无需信任设备内部操作的情况下认证密钥，甚至可以抵御仅受无信号原理约束的窃听者。我们追问：广义上下文性——一种在单系统制备-测量实验中可用的非经典性概念——能否发挥类似的作用。在我们的方法中，Alice和Bob首先在他们的本地制备和测量程序之间建立操作等价关系，这些等价关系随后被视为与理论无关的约束，任何对通信信道的物理干预（包括对手的干预）都必须遵守这些约束。Eve在其他方面不受限制，即不假设她对传输系统的干预可以用量子理论来描述。在这个对抗模型中，我们证明Eve针对个体攻击的最优猜测概率是一个有限线性规划的解，因此最坏情况下的渐近密钥率仅由观测统计量和操作等价关系即可确定。我们证明上下文性对于正密钥率是必要的。然而，我们也证明它并不充分。具体而言，(3,2)-奇偶不经意随机存取码已知可以对量子窃听者产生秘密密钥，但对后量子窃听者则不能产生任何可认证的密钥率。反过来，在没有无信号约束类比的操作等价关系可以严格提高渐近密钥率。我们用标准CHSH协议的制备-测量版本（带有对齐的密钥生成设置）来说明这一点。

**【核心创新点】**：
本文证明了广义上下文性是在不信任设备且不假设窃听者受量子理论约束的对抗模型下认证密钥的必要条件，但并非充分条件，且操作等价关系可严格提升渐近密钥率。

---

### 9. Making the most of leftovers: Improved privacy amplification for quantum key distribution

- **👨‍🔬 作者:** Matthew Simon Tan, Bartosz Regula, Marco Tomamichel
- **📅 时间:** 2026-09-29 18:00:01 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2609.38306v1) | [PDF直达](https://arxiv.org/pdf/2609.38306v1)

**【中文摘要】**：
量子密钥分发运行所能获得的密钥量，取决于物理上观测到的错误率以及用于认证安全性的数学界。对于有限数据集，保守的界迫使用户丢弃相当大一部分潜在可用的密钥。在此，我们进一步改进并扩展了通过Regula和Tomamichel近期提出的剩余哈希引理（arXiv:2603.04493）所能达到的隐私放大界，并将其纳入基于熵不确定性关系的量子密钥分发安全性分析中。这在有限块长情形下改进了当前最先进的密钥率，在不改变协议的情况下从相同实验数据中认证出更多密钥，并优于基于熵累积的技术。这些结果说明了更精确的数学估计如何能够直接提升量子通信系统的可用输出。

**【核心创新点】**：
通过改进基于Regula-Tomamichel剩余哈希引理的隐私放大界并将其融入熵不确定性关系的QKD安全分析，在不改变协议的前提下显著提升了有限块长下的密钥率。

---

### 10. Integrated balanced homodyne detector using CMOS capacitive-feedback TIA for quantum measurements

- **👨‍🔬 作者:** Sarah Bastiaens, Cedric Bruynsteen, Simone Cammarata, Axl Bomhals, Leandro da Silva, Michiel Van Osta, Johan Bauwelinck, Xin Yin
- **📅 时间:** 2026-09-29 14:25:54 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2609.37671v1) | [PDF直达](https://arxiv.org/pdf/2609.37671v1)

**【中文摘要】**：
本文展示了一种低噪声、高速平衡零差探测器，该探测器将基于28 nm CMOS工艺实现的电容反馈跨阻放大器与在imec的iSiPP200硅光子平台上制造的定制光子集成电路相结合。该接收机实现了7.6 GHz的3 dB带宽、27 dB的最大散粒噪声清除度、13.7 GHz的散粒噪声受限带宽以及高达54.8 dB的共模抑制比。这些结果证明了CMOS电容反馈跨阻放大器适用于要求严苛的量子与相干传感光学应用，包括连续变量量子密钥分发、量子随机数生成和光学相干断层扫描。

**【核心创新点】**：
**本文通过将28 nm CMOS电容反馈跨阻放大器与硅光子集成电路混合集成，实现了7.6 GHz带宽、27 dB散粒噪声清除度和54.8 dB共模抑制比的高速低噪声平衡零差探测器，验证了CMOS电容反馈跨阻放大器在连续变量量子密钥分发等量子光学应用中的适用性。**

---

### 11. Temporal trade-offs in high-dimensional entanglement: a comprehensive noise model for optimal time-bin QKD protocols

- **👨‍🔬 作者:** Alexandra E. Bergmayr-Mann, Gláucia Murta, Marcus Huber
- **📅 时间:** 2026-09-28 16:00:28 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2609.35488v1) | [PDF直达](https://arxiv.org/pdf/2609.35488v1)

**【中文摘要】**：
高维时间-bin纠缠因其在量子密钥分发（QKD）应用中具有巨大潜力而闻名，它易于实现、鲁棒性强，并且可能比简单的量子比特协议提供更好的密钥率。然而，时间编码与有限的时钟分辨率相结合，意味着一种权衡：是发送更多低维编码的光子更好，还是发送少量高维编码的光子更好？回答这个问题是一项艰巨的挑战，因为它取决于协议的整体背景，包括产生率、损耗、暗计数、时间抖动以及许多其他因素。我们针对单个基于Franson的干涉仪，以渐近密钥率和共享纠缠作为主要性能指标，回答了这个问题。我们提出了一个灵活的噪声模型，纳入了所有相关参数，并发现确实存在某些区域，当光子对到达率受限时（例如由于损耗或泵浦功率有限），高维编码仍然优于任何基于量子比特的方案。

**【核心创新点】**：
**该工作通过建立包含所有相关参数的灵活噪声模型，证明了在光子对到达率受限（如损耗或泵浦功率有限）的条件下，高维时间-bin编码在基于Franson干涉仪的QKD中仍能超越任何量子比特方案。**

---

### 12. Hybrid QKD-PQC Network Emulation through Automated and Scalable Cloud-Native Orchestration

- **👨‍🔬 作者:** Iván Melijosa, Javier Pérez, Borja Nogales, Iván Vidal, Francisco Valera
- **📅 时间:** 2026-09-28 15:06:03 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2609.35358v1) | [PDF直达](https://arxiv.org/pdf/2609.35358v1)

**【中文摘要】**：
面向量子安全网络的持续转型，推动了融合量子密钥分发（QKD）与后量子密码学（PQC）的混合网络架构的发展。然而，混合QKD-PQC网络架构的实验评估仍受限于量子硬件的高成本和有限可及性，以及现有仿真平台对混合QKD-PQC网络支持不足。Quditto是一个最初为QKD网络设计的开源仿真平台，能够在无需专用物理量子基础设施的情况下，实现低成本且可复现的实验。在此基础之上，本工作将Quditto呈现为一个混合QKD-PQC网络仿真平台，具备自动化且可扩展的云原生编排能力。所提出的平台引入了四项主要贡献：一个云原生编排器，支持跨云和多集群环境的全自动化基础设施部署；一个优化的资源调配工作流，支持大规模量子安全网络仿真；后量子节点的原生集成，支持混合QKD-PQC网络的统一仿真；以及一个安全密钥管理模块，提供加密材料的持久化且受访问控制的存储。实验验证表明，编排时间随网络规模呈亚线性扩展，并在一个具有代表性的脊叶（spine-leaf）部署中成功实现了端到端混合QKD-PQC密钥建立，从而使得在大规模异构网络环境中对量子安全网络机制进行系统性评估成为可能。

**【核心创新点】**：
本文将Quditto扩展为具备云原生自动化编排、后量子节点原生集成和安全密钥管理能力的混合QKD-PQC网络仿真平台，实现了大规模异构环境下量子安全网络机制的低成本、可复现系统性评估。

---

