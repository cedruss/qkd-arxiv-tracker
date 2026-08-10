# 🔐 arXiv 每周追踪：量子密钥分发 (QKD)

> **生成日期:** 2026-08-10 | **本周更新:** 5 篇

---

### 1. Demonstration of an LLO CV-QKD system over 12 km of optical fiber

- **👨‍🔬 作者:** Christiano M. S. Nascimento, Artur A. Matoso, Gustavo C. Amaral, Guilherme P. Temporão
- **📅 时间:** 2026-08-07 14:37:33 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2608.07277v1) | [PDF直达](https://arxiv.org/pdf/2608.07277v1)

**【中文摘要】**：  
连续变量量子密钥分发（CV-QKD）有望实现高密钥率，并可在单根光纤中与经典光束无缝集成。多年来，实际系统通常通过量子信道同时传输本振光参考，这为窃听者留下了安全漏洞，也限制了潜在应用场景。本文报告了一种采用完全独立的发射端和接收端激光器（即本振光源）的高斯CV-QKD实现，并在12公里光纤线轴上进行了实验验证。系统采用包含约10^7个相干态的逻辑帧进行实验评估，每帧由十个独立处理的子帧组成，每个子帧约含10^6个态；在可信设备模型下，分别从渐近和有限尺寸两种安全分析框架下评估了系统安全性。完整的经典后处理流程能够恢复信道参数，并在渐近条件下提取5.11 Mbit/s的密钥率，在有限尺寸条件下提取4.67 Mbit/s的密钥率，与理论预测高度一致。该工作为在严格安全约束下实现城域光纤CV-QKD部署奠定了基础。

**【核心创新点】**：  
实现了发射端与接收端激光器完全独立的CV-QKD系统，在12公里光纤上达到渐近5.11 Mbit/s和有限尺寸4.67 Mbit/s的密钥率，消除了本振光传输带来的安全漏洞。

---

### 2. Diversity in Coded TE-QKD Channels: Achieving Infinite Diversity out of Finite System Resources

- **👨‍🔬 作者:** Shaikha S. Al-Qahtani, Siyao Li, Joseph J. Boutros
- **📅 时间:** 2026-08-05 21:56:29 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2608.05432v1) | [PDF直达](https://arxiv.org/pdf/2608.05432v1)

**【中文摘要】**：  
我们建立了纠错码在时间纠缠量子密钥分发（TE-QKD）协调中实现无限分集阶数的条件并给出了证明。这一结果在编码与通信理论文献中前所未见，令人震惊：在信道具有有限分集且码长相对较短的情况下，译码器却展现出无限分集阶数。本文研究了编码TE-QKD协调的分集阶数，其定义为高信噪比下错误概率的渐近斜率。对于有界距离代数译码，我们以每码字光子数和译码半径为变量，推导了充要条件。对于软判决译码，我们引入了最大有限分集（MFD）性质，并证明当且仅当码为MFD缺陷时才能实现无限分集。TE-QKD中的无限分集在经典衰落信道中没有对应物——在经典信道中，译码只能将有限分集阶数乘以有限因子。基于Golay码、Reed-Solomon码、Bose-Chaudhuri-Hocquenghem（BCH）码和Reed-Muller码的短码示例验证了分析结果，并展示了TE-QKD系统参数及相对较短的码参数如何影响硬判决与软判决信息协调中可实现的分集性能。

**【核心创新点】**：  
**首次证明在时间纠缠QKD系统中，即使信道分集有限且码长较短，纠错码译码仍可实现无限分集阶数，这一现象在经典衰落信道中不存在。**

---

### 3. Poled-fibre phase modulator for efficient high-dimensional quantum measurements

- **👨‍🔬 作者:** Nayda Guerrero, Nelson Villalba, Gustavo H. dos Santos, Carlos J. Salazar, Cristobal Melo, Fernando Castillo, Jaime Cariñe, Guilherme B. Xavier, Esteban S. Gómez, Stephen P. Walborn, João Pereira, Gabriel Saavedra, Gustavo Lima
- **📅 时间:** 2026-08-04 18:06:35 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2608.04112v1) | [PDF直达](https://arxiv.org/pdf/2608.04112v1)

**【中文摘要】**：  
高效探测量子态是支撑先进设备无关量子信息协议的基础，这类协议为量子随机数生成和量子密钥分发（QKD）等任务提供了最高级别的安全性。高维编码是提升此类协议性能的自然途径，能够增强抗噪声能力并提高信息容量，但其实际实现仍面临挑战。在更高维度中，一个关键的实验瓶颈是基选择通常需要主动调制器，而这会引入显著的光学损耗和偏振敏感操作。极化光纤相位调制器（PFPM）作为一种光纤本征电光技术，天然解决了这些问题，兼具亚分贝插入损耗、内在偏振无关性以及与标准电信光纤的直接兼容性。本文首次报道了在全光纤集成平台中使用PFPM实现主动量子态测量。在我们的接收器中，四维量子态（qudit）的基选择仅需单个PFPM即可完成，大幅简化了接收器架构。作为基准测试，我们执行了一次四维QKD会话，获得的每脉冲有限密钥率，据我们所知，超过了此前所有已报道的QKD演示。我们的结果确立了极化光纤电光调制作为一种广泛适用的平台，可用于光纤集成量子信息处理中的高效探测。

**【核心创新点】**：  
首次利用极化光纤相位调制器（PFPM）实现全光纤集成平台中的主动量子态测量，以单调制器完成四维基选择，并在四维QKD中实现了迄今最高的每脉冲有限密钥率。

---

### 4. Beyond the QBER Threshold: A Temporal QBER Based Machine Learning Framework for Multi Attack Detection in BB84 QKD

- **👨‍🔬 作者:**  Isha, Deepak Singh, Devesh Kumar, S. K Pal, Praful Hambarde, Amit Shukla
- **📅 时间:** 2026-08-04 08:04:16 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2608.04047v1) | [PDF直达](https://arxiv.org/pdf/2608.04047v1)

**【中文摘要】**：  
传统BB84量子密钥分发（QKD）系统依赖固定的11%量子比特误码率（QBER）阈值来检测窃听行为。然而，隐蔽攻击可能在该阈值以下运作，同时仍危及信道安全。本文提出一种基于时间QBER的机器学习框架，用于BB84 QKD系统中窃听攻击的检测与分类。该框架不依赖平均会话级QBER，而是提取63个物理信息启发的时序特征，涵盖突发行为、时间不稳定性、基矢依赖不对称性以及QBER损失交互。研究在噪声和有损条件下，对七种窃听攻击及正常信道场景，评估了随机森林、XGBoost和径向基函数核支持向量机（SVM-RBF）分类器。在十次独立运行的平均结果中，XGBoost取得了最佳性能，准确率达88.01%（标准差0.47%），宏F1分数为0.8803；SVM-RBF表现相当，验证了所提特征的鲁棒性。作为二分类攻击-正常检测器与传统监测方式对比时，固定11% QBER阈值仅达到25.82%的准确率，漏报率（FNR）为0.8477；而所提框架将漏报率降至0.0198，显著提升了对规避阈值监测的隐蔽攻击的检测能力。基于SHapley Additive exPlanations（SHAP）的可解释性分析表明，物理信息启发的时序与信道派生特征对识别窃听策略具有高度判别力。这些结果证明，时间QBER驱动的机器学习为BB84 QKD系统提供了一种准确、可解释且实用的多攻击安全监测框架。

**【核心创新点】**：  
提出一种基于时间QBER时序特征与机器学习分类的框架，将隐蔽窃听攻击的漏报率从0.8477降至0.0198，显著优于传统固定阈值监测方法。

---

### 5. Ring Optimized M-APSK Modulation for Discrete Modulated CV-QKD

- **👨‍🔬 作者:** Seonguk Kim, Jun Heo
- **📅 时间:** 2026-08-03 05:42:32 (UTC)
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2608.01723v1) | [PDF直达](https://arxiv.org/pdf/2608.01723v1)

**【中文摘要】**：  
本文提出了一种面向离散调制连续变量量子密钥分发（QKD）的多环M-APSK星座优化方法。与固定环间距和预设环概率的传统APSK结构不同，所提方法通过优化环半径比和环概率来提升有限尺寸下的安全密钥率。利用基于Gram矩阵的方法计算平均态\( \tau \)的非零谱，并通过保真度将优化后的离散平均态与高斯平均态进行比较。结果表明，与传统二项式APSK结构相比，所提结构将16-APSK的最大传输距离延长了约15%。对于小尺寸APSK星座，优化增益更大，因为其平均态与高斯调制之间的结构差距更大。

**【核心创新点】**：  
通过优化多环APSK的环半径比与环概率，显著提升离散调制CV-QKD的有限尺寸安全密钥率，并将16-APSK最大传输距离延长约15%。

---

