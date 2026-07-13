# 🔐 arXiv 每周追踪：量子密钥分发 (QKD)

> **生成日期:** 2026-07-13 | **本周更新:** 10 篇

---

### 1. GHz-rate all-fiber active polarization state analyzer for quantum protocols

- **👨‍🔬 作者:** Andrea Pompermaier, Kannan Vijayadharan, Costantino Agnesi, Marco Avesani, Giuseppe Vallone, Paolo Villoresi
- **📅 时间:** 2026-07-10 16:54:11 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.09597v1) | [PDF直达](https://arxiv.org/pdf/2607.09597v1)

**【中文摘要】**：  
主动选择测量基是量子协议（包括设备无关量子密钥分发、带主动前馈的量子隐形传态以及贝尔测试）的基础。高速运行对于最小化连续测量选择之间的延迟至关重要，从而能够实现更快的协议执行和更高的可达通信速率。在此，我们展示了一种千兆赫兹速率全光纤偏振态分析器，能够实现测量基的主动、逐次重构，并通过执行CHSH贝尔测试对其进行了验证。该分析器基于一个包含铌酸锂电光相位调制器的光纤萨格纳克干涉仪，完全采用商用现成光纤元件构建。系统在1 GHz标称重复频率下运行，为CHSH贝尔测试执行动态偏振测量，实现了高达99%的偏振对比度，并得到S = 2.6975 ± 0.0005的贝尔不等式违背，以前所未有的速率认证了纠缠。此外，该系统展现出优异的长期稳定性，可在无需重新对准的情况下保持贝尔不等式违背超过6小时。这些结果确立了所提出的分析器作为一种多功能、可扩展的平台，适用于需要快速、可重构偏振态测量的量子通信协议。

**【核心创新点】**：  
**基于1 GHz全光纤萨格纳克干涉仪与铌酸锂电光调制器，实现了测量基的逐次主动重构，并在CHSH贝尔测试中以99%偏振对比度和持续6小时以上的稳定性，以前所未有的速率认证了纠缠。**

---

### 2. Orthogonal Quantum Krylov Diagonalisation

- **👨‍🔬 作者:** Hadi Rammal, Alexandre Perrin, Oumaya Ladhari, Clément Dutreix, Jérémie Messud, Matthieu Saubanere
- **📅 时间:** 2026-07-10 14:49:53 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.09476v1) | [PDF直达](https://arxiv.org/pdf/2607.09476v1)

**【中文摘要】**：  
量子子空间对角化方法，特别是量子Krylov对角化（QKD），为计算量子多体哈密顿量的低能谱提供了一条有前景的路径。然而，现有的量子Krylov方法依赖于非正交的Krylov基，需要重叠矩阵正则化，这限制了数值稳定性与精度。在本工作中，我们提出了一种正交量子Krylov对角化（OQKD）框架，该框架在算符层面重新表述了经典的Lanczos递归，从而实现了Krylov子空间对角化的正交量子实现。通过将Lanczos向量表示为哈密顿量的多项式变换，OQKD再现了经典Lanczos算法的正交性、三对角结构以及收敛行为，从而消除了对重叠矩阵正则化的需求。我们进一步证明，所需的Lanczos多项式可以通过块编码和广义量子信号处理实现，其渐近查询复杂度与基于切比雪夫的QKD方法相同。对$J_1$–$J_2$海森堡模型的数值模拟证实了所提方法具有经典Lanczos的收敛性和数值稳定性，同时从解析上建立了测量复杂度的标度。基于OQKD框架，我们进一步引入了一种重启态制备协议，该协议将单个高次多项式变换替换为一系列固定低次变换，在保持可负担的块编码成功概率的同时，保留了可比的收敛性。这些结果确立了OQKD作为经典Lanczos算法的正交量子类比，并指出重启协议是量子相位估计中一种有前景的态制备策略。

**【核心创新点】**：  
**提出正交量子Krylov对角化（OQKD）框架，通过算符层面的Lanczos递归实现正交Krylov子空间，消除了传统QKD方法中重叠矩阵正则化带来的数值不稳定性，并引入重启态制备协议以降低多项式变换的复杂度。**

---

### 3. Robust One-Sided Device-Independent Quantum Key Distribution via High-Dimensional Steering

- **👨‍🔬 作者:** Monika Mothsara, Suraj Goel, Bohnishikha Ghosh, Vatshal Srivastav, Will McCutcheon, Mehul Malik, Gláucia Murta
- **📅 时间:** 2026-07-09 17:18:46 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.08709v1) | [PDF直达](https://arxiv.org/pdf/2607.08709v1)

**【中文摘要】**：  
量子密钥分发（QKD）有望实现信息论安全性的通信，但在实际应用中因易受噪声、损耗和器件不完美的影响而受到限制。为应对这些挑战，我们提出了一种鲁棒的高维（HD）单边设备无关QKD（1sDI-QKD）协议，并展示了利用横向空间自由度纠缠光子的原理验证实验。我们开发了HD 1sDI-QKD协议的系统性安全分析，利用量子导引来认证安全性，并通过反向协调评估了不同测量配置和系统维度下的可达密钥率。分析表明，增加维度可增强对噪声和损耗的鲁棒性。随后，我们演示了实现该协议所需的关键实验模块：（a）高质量的高维光子纠缠源，以及（b）一个完全可编程、最高支持维度11的高维多输出测量装置。利用这些组件，在公平采样假设下，我们在所有研究的维度中均获得了正密钥率，其中维度d=7时密钥率最高。最后，我们讨论了在现实损耗和噪声条件下实现无漏洞实用化1sDI-QKD所需的步骤。

**【核心创新点】**：  
**通过高维量子导引认证安全性，提出并实验验证了一种在噪声和损耗下更鲁棒的高维单边设备无关QKD协议，在维度d=7时获得最高密钥率。**

---

### 4. Continuous-Variable MIMO THz Quantum Secret Sharing: Gaussian-modulation and Passive-modulation

- **👨‍🔬 作者:** Leixin Wu, Jiayu Pan, Fangzhe Chen, Lingtao Zhang, Bowen Zheng, Tie Qiu
- **📅 时间:** 2026-07-09 06:51:15 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.08158v1) | [PDF直达](https://arxiv.org/pdf/2607.08158v1)

**【中文摘要】**：  
尽管量子密钥分发（QKD）能够实现信息论意义上的安全密钥分发，但其主要针对点对点通信设计，无法直接支持多用户协作场景。为克服这一局限，量子秘密共享（QSS）被提出以实现安全的多方密钥共享。然而，现有大多数QSS协议依赖于单输入单输出（SISO）信道，这限制了可达的密钥生成率（SKR）和传输距离。本文提出了一种基于太赫兹（THz）频段多输入多输出（MIMO）架构的连续变量（CV）QSS协议。在该方案中，发射-接收波束赋形将MIMO信道分解为多个并行的SISO子信道，从而同时提升了SKR和传输距离。我们描述了QSS的传输流程，并推导了八种协议变体在高斯集体攻击下的SKR表达式。具体而言，发射端考虑了高斯调制和无源调制，接收端考虑了零差探测和外差探测。分别推导了渐近极限和可组合有限码长下的SKR公式，以表征理想上界性能和有限资源下的可达性能。仿真结果表明，在理想假设（包括完美信道状态信息、完美相位同步和理想波束赋形）下，采用32×32天线配置的高斯调制协议和采用1024×1024天线配置的无源调制协议，在大气信道中分别实现了14.99米和160米的传输距离。这些结果为评估MIMO辅助太赫兹CV-QSS在室内及短距离室外无线网络中的潜在性能增益提供了理想化的理论基准。

**【核心创新点】**：  
**本文提出基于太赫兹MIMO架构的连续变量量子秘密共享协议，通过波束赋形将MIMO信道分解为并行SISO子信道，显著提升了密钥生成率和传输距离，并在理想条件下实现了最高160米的大气信道传输。**

---

### 5. Secret Key Rate Analysis of Distribution Matching Algorithms for Discrete-Modulated CV-QKD

- **👨‍🔬 作者:** Micael Dias, Caroline Alves, Gabrielly Roman, Søren Forchhammer
- **📅 时间:** 2026-07-07 20:24:04 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.06783v1) | [PDF直达](https://arxiv.org/pdf/2607.06783v1)

**【中文摘要】**：  
采用离散调制的连续变量量子密钥分发协议（CV-QKD）已被广泛研究，以弥合理想高斯调制与现代相干光通信系统之间的差距。为减轻离散调制带来的性能损失，概率星座整形（PCS）被应用于调制格式，并通常通过分布匹配（DM）算法实现。本文探讨了在CV-QKD协议中应用DM算法执行PCS的问题。我们研究了基于霍夫曼码（HDM）和恒定组合码（CCDM）的DM算法在近似优化麦克斯韦-玻尔兹曼分布时，对协议密钥率（SKR）及超额噪声容忍度的影响。结果表明，逐符号的HDM会使SKR降低至少30%，而CCDM在码长达到10³个符号或以上时能匹配最优SKR。此外，我们还对两种方法的符号依赖性进行了统计分析，表明CCDM需在至少10⁵个符号的块长下操作才能使相关性可忽略。最后，我们提出了一种生成遵循近最优分布的独立符号的算法。

**【核心创新点】**：  
**通过对比霍夫曼码与恒定组合码在CV-QKD概率星座整形中的性能，发现CCDM在足够码长下能实现最优密钥率，并提出了生成近最优独立符号的算法。**

---

### 6. Semi-Device-Independent Quantum Key Distribution from Operational Assumptions

- **👨‍🔬 作者:** Anubhav Chaturvedi, Giuseppe Viola, Ekta Panwar, Tushita Prasad, Debashis Saha
- **📅 时间:** 2026-07-07 18:01:48 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.06682v1) | [PDF直达](https://arxiv.org/pdf/2607.06682v1)

**【中文摘要】**：  
半设备无关量子密钥分发不对测量设备进行表征，但要求对Alice的源施加可信假设。我们以四个物理动机源任务之一（完整标签猜测、奇偶性猜测，或它们与标签排除的归一化复合任务）的标量界，操作性地将这一源假设施加于Alice的四制备系综。对于两比特随机存取码，我们推导了四种源假设下精确的经典边界。数值结果表明，BB84策略在所有四个边界上均达到最大量子偏离，而制备退极化BB84族与直和标签泄漏族在两种排除辅助假设下，描绘了任意维度量子边界的互补分支。由于所有四个任务值在输入无关量子信道下是单调的，相同的标量源界约束了所有与完整观测行为兼容的Bob–Eve扩展。通过使用一个将RAC测试与密钥生成分离的三设置扩展，我们在此可行集上获得了两个与维度无关的安全证书：条件最小熵与条件冯·诺依曼熵的下界，分别通过直接优化Eve的密钥猜测概率和基于Brown–Fawzi–Fawzi变分界的制备-测量半定松弛得到。排除辅助假设能在制备可见度几乎为零时仍认证正密钥率，远超单独使用完整标签猜测或奇偶性猜测的能力。在直和标签泄漏下，所有四个独立优化的速率界在每一个采样的不完全泄漏点均为正，仅在完全标签揭示时归零。这些结果表明，鲁棒的半设备无关安全性不仅取决于Eve能识别什么，还取决于她能够排除什么。

**【核心创新点】**：  
**通过引入“标签排除”辅助的源假设，半设备无关QKD能在极低制备可见度下仍保持正密钥率，揭示了安全性不仅依赖于Eve能识别什么，更依赖于她能排除什么。**

---

### 7. Simplified quantum key distribution implementation secure in the presence of state preparation flaws

- **👨‍🔬 作者:** Ainhoa Agulleiro, Fadri Grünenfelder, Raphaël Houlmann, Ana Blázquez, Hugo Zbinden, Davide Rusca
- **📅 时间:** 2026-07-07 09:13:58 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.06038v1) | [PDF直达](https://arxiv.org/pdf/2607.06038v1)

**【中文摘要】**：
我们提出了一种基于时间比特编码的三态BB84协议的实现方案，该方案采用一个诱骗态（decoy state）以及一种利用被动基矢选择的简化测量结构。与先前的迭代版本相比，我们的系统简化了态的表征过程。同时，我们将容错方法（loss-tolerant method）适配到该协议中，从而处理测量态制备缺陷。我们比较了在考虑态不完美和假设完美态两种情况下获得的相位错误率和密钥生成率。我们的结果突显了态表征与实现安全性的重要性。

**【核心创新点】**：
**通过引入简化被动基矢选择与容错方法，实现了对三态BB84协议中态制备缺陷的有效处理，并揭示了态表征对实际安全性的关键影响。**

---

### 8. Real-Time VPN Traffic over ETSI GS QKD 014 Key Delivery with a LuxQuanta NOVA QKD Platform

- **👨‍🔬 作者:** Felipe Paixão, Anderson Altair Tomkelski, Marcus Elias Silva Freire, Isys Nogueira de Sant'Anna, Adriano Humberto de Oliveira Maia, Reinan da Silva Salazar, Ney Ricardo Lopez Junior, João Marcelo Silva Souza
- **📅 时间:** 2026-07-07 01:05:41 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.06602v1) | [PDF直达](https://arxiv.org/pdf/2607.06602v1)

**【中文摘要】**：  
本报告介绍了一种原型VPN，它使用通过ETSI GS QKD 014 API分发的QKD生成密钥。该VPN采用AES-256-GCM对IP流量进行加密，在带内传输ETSI密钥标识符，并从本地KME（密钥管理实体）中检索匹配的密钥。在经过受控KME模拟器验证后，该系统在两台连接到LuxQuanta NOVA QKD平台的Jetson Xavier NX设备上进行了测试。实验成功实现了通过该VPN连续八小时的双向实时音视频流量传输，证明了通过标准化密钥分发接口将经典VPN应用与QKD基础设施集成的可行性。

**【核心创新点】**：  
**通过标准化ETSI QKD 014 API实现QKD密钥与经典VPN的集成，并在真实QKD硬件上验证了连续八小时实时音视频传输的可行性。**

---

### 9. Characterisation of a satellite-to-ground channel for continuous variable quantum key distribution protocol

- **👨‍🔬 作者:** Emma Tien Hwai Medlock, Vinod N. Roa, Timothy Spiller, Rupesh Kumar
- **📅 时间:** 2026-07-06 14:04:08 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.05109v1) | [PDF直达](https://arxiv.org/pdf/2607.05109v1)

**【中文摘要】**：  
在基于空间的量子密钥分发（QKD）协议中，量子信道具有动态特性，其信道损耗会随天顶角的变化而改变。在连续变量（CV）-QKD的背景下，这将导致参数估计问题，特别是对于传输的本地振荡器而言，还会引起散粒噪声的波动。因此，表征这种信道损耗及其来源至关重要。本文在实际假设下对变化的信道损耗进行了表征，并展示了不同场景、湍流强度以及波长下的结果。研究表明，在所考虑的信道参数下，若采用受限的Eve安全性假设，则有可能生成正的安全密钥。

**【核心创新点】**：  
**本文首次在实际条件下系统表征了空间CV-QKD中随天顶角变化的动态信道损耗，并证明在受限Eve安全性假设下仍可生成正的安全密钥。**

---

### 10. Noise-limited secret key agreement with twin optical physically unclonable functions

- **👨‍🔬 作者:** Georgios M. Nikolopoulos
- **📅 时间:** 2026-07-06 11:07:30 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2607.04936v1) | [PDF直达](https://arxiv.org/pdf/2607.04936v1)

**【中文摘要】**：
我们研究了利用源自相关物理不可克隆函数（PUF）的双光学指纹，作为基于硬件的密钥生成与分发平台。每个指纹与一个随机但可复现的散斑图案相关联，该图案由相干光在无序光学结构中散射产生。我们考虑一对相关的光学PUF，并研究在制造变异与环境噪声存在的情况下，两个诚实方建立共享秘密密钥的条件。我们开发了一个显式的信息论密钥协商协议，该协议整合了安全草图、错误协调与隐私放大。我们量化了因公开辅助数据导致的信息泄露，并推导出最终秘密密钥长度的下界。该分析识别了安全密钥协商可行的噪声区间，并考察了实用型与接近容量型协调方案的性能。最后，我们讨论了如何将双光学PUF集成到量子密钥分发（QKD）网络中，作为一种在两个诚实用户之间建立初始预共享秘密密钥的机制，且无需依赖计算假设或可信第三方。

**【核心创新点】**：
**提出利用相关光学PUF的双指纹作为硬件信任根，结合信息论密钥协商协议，可在不依赖计算假设或可信第三方的情况下，为QKD网络提供初始预共享密钥。**

---

